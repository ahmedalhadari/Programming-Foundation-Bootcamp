student = {
    "name": "Ahmed",
    "age": 17,
    "city": "Riyadh",
    "email": "ahmed@gmail.com"
}
empty_dict = {}
employee = dict(name="Mohammed", age=22, emp_id=10001)
key_value = [("Car model", "TOYOTA"), ("Car name", "Corolla")]
car_dict = dict(key_value)

print("Student Dictionary", student)
print("Employee Dictionary", employee)
print("Car Dictionary", car_dict)
print(student["name"])
# print (student["score"]) | KeyError
print(student.get("score"))
student["score"] = 3.78
print(student)
del student["score"]
print(student)
print(type(car_dict))
print(student.keys())
print(list(student.keys()))
print(student.values())
city = student.pop("city")
print(city)
# print (student["city"]) | Error, No city key
student["score"] = 3.59
print(student)
student.popitem()
print(student)
student.popitem()
print(student)
student.clear()
print(student)
student = {
    "name": "Ahmed",
    "age": 17,
    "city": "Riyadh",
    "email": "ahmed@gmail.com"
}
student2 = {
    "name": "Mohammed",
    "age": 22,
    "city": "Dammam",
    "email": "mohammed@gmail.com"
}

print(student.items())
student.update(student2)
print(student)
student2["name"] = "Ali"
student_copy = student.copy()
print(student_copy)

print("name" in student)
print("name" not in student)
print(len(student))
# Nested Dictionaries
students = {
    "S001": {"name": "Ahmed", "age": 18, "grade": 3.20},
    "S002": {"name": "Mohammed", "age": 22, "grade": 2.50},
    "S003": {"name": "Ali", "age": 25, "grade": 3.90}
}
print (students["S001"]["name"])
schedule = {
    "Sunday": ["Programming", "Networks", "Cybersecurity"],
    "Monday": ["HTML", "Python", "C#"],
    "Tuesday": ["SQL", "MySQL", "SQL Server"]
}
print (schedule["Sunday"][0])