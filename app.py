import json
import os

def verify(json_file):

    try:
        f = open(json_file, 'r')
    except FileNotFoundError:
        print(f"Could not read the file {json_file}")
        return True

    with f:
        file_size = os.path.getsize(json_file)
        if (file_size == 0):
            print("File is empty")
            return True
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Invalid json file")
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

json_file = '/home/nastia/remitly/test.json'
result = verify(json_file)
print(result)