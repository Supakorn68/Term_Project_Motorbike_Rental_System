# สร้างพจนานุกรม
student = {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

# เมธอดของพจนานุกรม
print(student.keys())      # แสดงคีย์ทั้งหมด  → ผลลัพธ์: dict_keys(['name', 'age', 'major'])
print(student.values())    # แสดงค่าทั้งหมด  → ผลลัพธ์: dict_values(['Alice', 26, 'Computer Science'])
print(student.items())     # แสดงคู่คีย์-ค่า  → ผลลัพธ์: dict_items([('name', 'Alice'), ('age', 26), ('major', 'Computer Science')])

# การใช้เมธอด get()
print(student.get("name"))                 # ดึงค่าของคีย์ "name" → ผลลัพธ์: Alice
print(student.get("grade", "Not Found"))   # หากไม่มีคีย์ "grade" ให้แสดง "Not Found" → ผลลัพธ์: Not Found

# การใช้เมธอด pop()
major = student.pop("major")       # ลบคีย์ "major" และคืนค่าของมัน
print(major)                       # ผลลัพธ์: Computer Science
print(student)                     # พจนานุกรมหลังจากลบ → ผลลัพธ์: {'name': 'Alice', 'age': 26}

# การใช้เมธอด popitem()
last_item = student.popitem()     # ลบรายการสุดท้ายออก (key-value สุดท้าย)
print(last_item)                  # ผลลัพธ์: ('age', 26)
print(student)                    # ผลลัพธ์: {'name': 'Alice'}

# การใช้เมธอด clear()
student.clear()                   # ลบข้อมูลทั้งหมดในพจนานุกรม
print(student)                    # ผลลัพธ์: {}
