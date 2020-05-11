
d = [{'value': 1}, {'value': 3}, {'value': 2}]

s = sorted(d, key=lambda x : x['value'], reverse=False)
print(s)