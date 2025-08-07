# สร้างพจนานุกรม
student = {"name": "Alice", "age": 25, "grade": "A"}

# การเพิ่มและการอัปเดตค่า
student["age"] = 26
student["major"] = "Computer Science"
print(student)  # ผลลัพธ์: {'name': 'Alice', 'age': 26, 'grade': 'A', 'major': 'Computer Science'}

# ลบคู่คีย์-ค่าโดยใช้ del
del student["grade"]
print(student)  # ผลลัพธ์: {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

# ลบคู่คีย์-ค่าโดยใช้ pop และเก็บค่าที่ลบออกมา
removed_major = student.pop("major")
print(removed_major)  # ผลลัพธ์: 'Computer Science'
print(student)        # ผลลัพธ์: {'name': 'Alice', 'age': 26}
