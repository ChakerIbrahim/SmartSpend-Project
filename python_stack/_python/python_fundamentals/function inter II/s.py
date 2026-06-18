# Update Values in Dictionaries and Lists

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

# x[1][0] = 15
# students[0]['last_name'] = "wasaya"
# students[0]['first_name'] = "Jalil"
# sports_directory['soccer'][0] = "Jalil"
# z[0]['y'] = 15

# print(x)
# print(students)
# print(sports_directory)
# print(z)


def iterateDictionary(students):
    students.append({"first_name": "Mark", "last_name": "Guillen"})
    students.append({"first_name": "KB", "last_name": "Tonel"})
    print(students)

    for i in students:
        print(i["first_name"])
    for i in students:
        print(i["last_name"])
    return students


iterateDictionary(students)
