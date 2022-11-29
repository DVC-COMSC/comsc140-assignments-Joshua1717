emp_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Key change
# salary -> wage 

emp_dict['wage'] = emp_dict.pop('salary')
print (emp_dict)

# or
