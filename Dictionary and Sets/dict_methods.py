# key() it will return the keys of the dictionary
# values() it will return the values of the dictionary
# items() it will return the keys and values of the dictionary
# get(key) it will return the value of the key
# clear() it will clear the dictionary
# pop(key) it will remove the key and return the value
# popitem() it will remove the last key and value   
# copy() it will return a copy of the dictionary
# update() it will update the dictionary

info = {
    "name": "suraj",
    "age": 20,
    "city": "Delhi",
    "marks": [1,2,3,4,5],
    "Subjects": {
        "Maths": 90,
        "Science": 80,
        "English": 70
    },
    "topics": ("dict", "list", "tupple", "set")
}

print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
print(info.get("marks")[1])


info.pop("name")
print(info)

info.popitem()
print(info)

# print(info.copy())

info.update({"name": "suraj kumar"})
print(info)