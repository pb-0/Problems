import json
import string

x = '{"a":1, "b":2}'

j_dict = json.loads(x)

print("json_loads:",j_dict)

y = {x:ord(x)-96 for x in string.ascii_lowercase[:10][::-1]}
print(y)
j_json = json.dumps(y, sort_keys=True, separators=(', ',': '))

print("json_dumps", j_json)

j_dict_json = json.loads(j_json)

print("json_dumps_loads", j_dict_json)