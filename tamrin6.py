my_dict = {"name": "Mohammad", "age": 23, "city": "Tabriz"}

print(len(my_dict))

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print(my_dict.get("name"))
print(my_dict.get("job"))

my_dict.update({"job": "Engineer", "age": 26})
print(my_dict)

removed_value = my_dict.pop("city")
print(removed_value)
print(my_dict)

my_dict.clear()
print(my_dict)