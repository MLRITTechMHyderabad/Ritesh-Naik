customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

x=list(map(lambda cus :{ 'name' : cus["name"],'age' : cus["age"],'total_purchase': cus["total_purchase"] - (cus["total_purchase"] * 0.1)} ,filter(lambda x : x["age"]>=18 and x["age"]<=25,customers)))

print(x)
