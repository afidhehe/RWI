import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])
import json

# a Python object (dict):
p = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
q = json.dumps(p)

# the result is a JSON string:
print(p)
