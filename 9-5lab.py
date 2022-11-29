dict1 = {'name': 'KIM', 'ZIP': 94598, 'address': '1234 Grand ave'}
dict2 = {'score': [100, 90], 'Grade': 'Senior'}
dict3 = {**dict1, **dict2}

print(dict3)
#########

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
