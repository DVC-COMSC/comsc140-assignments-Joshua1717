emp_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

keys = ['name', 'salary']

for k in keys:
    emp_dict.pop(
        k)  # pop() returns a value and delete the item at the same time

print(emp_dict)

#########
emp_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

emp_dict = {k: emp_dict[k] for k in emp_dict.keys() - keys}

print(emp_dict)
