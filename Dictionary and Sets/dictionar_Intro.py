#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and they have keys and values.
#they are unordered, changeable, and do not allow duplicates.

dict = {
    "name": "suraj",
    "age": 20,
    "city": "Delhi",
    "marks": [1,2,3,4,5]
}

print(dict.keys())
print(dict.values())

print(dict.get("name"))
print(dict.get("marks")[1])

info ={
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
print(info)

print(info["Subjects"]["English"])
print(info["topics"][2])
print(info["name"])
print(info.get("name"))
print(info.get("Subjects").get("English"))


info["Subjects"]["English"] = 100
print(info["Subjects"]["English"])

null_dict = {}
print(null_dict)

null_dict["name"] = "suraj"
print(null_dict)

# nested dictionary
student = {
    "name": "suraj",
    "Subjects": {
        "Maths": 90,
        "Science": 80,
        "English": 70
    }
}

print(student["Subjects"]["English"])