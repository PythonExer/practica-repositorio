import json 
with open("api/userdata.json","r") as api:
    data = api.read()

print(json.loads(data)[1]['apellido'])