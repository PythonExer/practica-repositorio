import json
with open("api/api.json","r") as api:
    data = api.read()

print(data)