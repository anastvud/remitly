import os
import unittest
from unittest.mock import patch
from app import verify

class TestVerifyFunction(unittest.TestCase):
    def test_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = verify(f'{os.getenv("REPO_ROOT")}/resources/t.json')
            self.assertTrue(result)
    
    def test_empty_file(self):
        with patch('builtins.open', side_effect=[open('/dev/null', 'r'), IOError]):
            result = verify(f'{os.getenv("REPO_ROOT")}/resources/empty.json')
            self.assertTrue(result)

    def test_invalid_json(self):
        with patch('builtins.open', side_effect=[open(f'{os.getenv("REPO_ROOT")}/resources/invalid.json', 'r'), '{"invalid": "json"']):
            result = verify(f'{os.getenv("REPO_ROOT")}/resources/invalid.json')
            self.assertTrue(result)

    def test_missing_policy_document(self):
        with patch('builtins.open', side_effect=[open(f'{os.getenv("REPO_ROOT")}/resources/missing_policy.json', 'r'), '{"PolicyName": "test"}']):
            result = verify(f'{os.getenv("REPO_ROOT")}/resources/missing_policy.json')
            self.assertTrue(result)

    def test_resource_not_asterisk(self):
        with patch('builtins.open', side_effect=[open(f'{os.getenv("REPO_ROOT")}/resources/not_asterisk.json', 'r'), '{"PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Resource": "arn:aws:s3:::my_bucket"}]}}']):
            result = verify(f'{os.getenv("REPO_ROOT")}/resources/not_asterisk.json')
            self.assertTrue(result)

    def test_resource_is_asterisk(self):
        with patch('builtins.open', side_effect=[open(f'{os.getenv("REPO_ROOT")}/resources/test.json', 'r'), '{"PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Resource": "*"}]}}']):
            result = verify(f'{os.getenv("REPO_ROOT")}/resources/test.json')
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
