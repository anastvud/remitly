import json
import os

def verify(json_file):

    try:
        with open(json_file, 'r') as f:
            file_size = os.path.getsize(json_file)
            if (file_size == 0):
                print("File is empty")
                return True
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Invalid json file")
                return True
    except FileNotFoundError:
        print(f"Could not read the file {json_file}")
        return True

    resource = None
    try:
        resource = data['PolicyDocument']['Statement'][0]['Resource']
    except KeyError:
        print('Some key in .json file is missing')

    if resource == '*':
        return False
    else:
        return True
    

if __name__ == '__main__':
    root = os.getenv('REPO_ROOT')
    json_file = root + '/resources/test.json'
    result = verify(json_file)
    print(result)