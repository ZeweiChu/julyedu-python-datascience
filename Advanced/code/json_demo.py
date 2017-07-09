import json

data = '{"name": "July", "salary": 999999, "title": "CEO", "manager": null}'

json_data = json.loads(data)

print(type(json_data))
print(json_data)

json_data = json.load(open("recursion-sort.ipynb", "r"))
print(type(json_data))
print(json_data)

dumped_json = json.dumps(json_data)
print(type(dumped_json))
print(dumped_json)

json.dump(json_data, open("out.json", "w"))


