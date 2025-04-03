employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]



x=list(filter(lambda emp : emp["rating"]>=4,employees))
print(x)
updatedEmp=list(map(lambda emp : emp["salary"]+emp["salary"]*0.1,x))
print(updatedEmp)


