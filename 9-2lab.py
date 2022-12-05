emp_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

keys = ['name', 'salary']

new_dict = {}
for k in keys:
    try:
        new_dict[k] = emp_dict[k]
    except KeyError:
        pass
print(new_dict)

new_dict = { k:emp_dict[k] for k in keys}       # simple , but there is no error check
print (new_dict)