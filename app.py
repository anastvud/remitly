import json
from jsonschema import validate

def verify(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        
    resource = data['PolicyDocument']['Statement'][0]['Resource']
    
    if resource == '*':
        return False
    
    return True

json_file = '/home/nastia/remitly/test.json'
result = verify(json_file)
print(result)


# TODO: cornercases: resource doesn't exist, resource is empty, json isn't valid, 