# การสร้างพจนานุกรมโดยใช้วงเล็บปีกกา {}
student = {"name": "Alice", "age": 25, "grade": "A"}
print(student)
# ผลลัพธ์: {'name': 'Alice', 'age': 25, 'grade': 'A'}

# การสร้างพจนานุกรมโดยใช้ dict() ด้วย keyword arguments
student = dict(name="Alice", age=25, grade="A")
print(student)
# ผลลัพธ์: {'name': 'Alice', 'age': 25, 'grade': 'A'}

# การสร้างพจนานุกรมโดยใช้ dict() ด้วยลิสต์ของทูเพิล
student = dict([("name", "Alice"), ("age", 25), ("grade", "A")])
print(student)
# ผลลัพธ์: {'name': 'Alice', 'age': 25, 'grade': 'A'}