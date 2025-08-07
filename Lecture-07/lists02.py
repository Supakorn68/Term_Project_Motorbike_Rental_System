# ข้อมูลการเข้าเรียนประจำสัปดาห์ (แต่ละลิสต์แสดงการเข้าเรียนในแต่ละวัน)
attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],  # วันที่ 1
    ["Alice", "Charlie", "David"],        # วันที่ 2
    ["Alice", "Bob", "David"],            # วันที่ 3
    ["Alice", "David", "Eve"],            # วันที่ 4
    ["Bob", "Charlie", "David"]           # วันที่ 5
]

# แปลงลิสต์การเข้าเรียนแต่ละวันให้เป็นเซ็ต เพื่อให้ง่ายต่อการดำเนินการ
attendance_sets = [set(day) for day in attendance_week]

# 1. หาเซ็ตของนักเรียนที่มาเรียนทุกวัน
# เริ่มต้นด้วยเซ็ตของวันแรก จากนั้นหา Intersection กับเซ็ตของวันต่อๆ ไป
all_students = attendance_sets[0]
for day_set in attendance_sets[1:]:
    all_students &= day_set
print(f"1. นักเรียนที่มาเรียนทุกวัน: {all_students}")

# 2. หานักเรียนที่ขาดเรียนอย่างน้อยหนึ่งวัน
# ขั้นแรก หาเซ็ตของนักเรียนทั้งหมดที่มาเรียนอย่างน้อยหนึ่งวัน
all_unique_students = set().union(*attendance_sets)
# นักเรียนที่ขาดเรียนอย่างน้อยหนึ่งวัน คือนักเรียนที่ไม่ใช่นักเรียนที่มาเรียนทุกวัน
absent_at_least_once = all_unique_students - all_students
print(f"2. นักเรียนที่ขาดเรียนอย่างน้อยหนึ่งวัน: {absent_at_least_once}")

# 3. สร้างลิสต์ของนักเรียนที่มาเรียนวันแรกแต่ขาดเรียนวันที่สอง
# นักเรียนที่มาเรียนวันที่ 1 แต่ไม่มาวันที่ 2
present_day1_absent_day5 = set(attendance_week[0]) - set(attendance_week[1])
print(f"3. นักเรียนที่มาเรียนวันที่ 1 แต่ขาดเรียนวันที่ 5: {list(present_day1_absent_day5)}")

# 4. คำนวณจำนวนนักเรียนที่ไม่ซ้ำกันที่มาเรียนอย่างน้อยหนึ่งวัน
# ใช้ Union ของเซ็ตทั้งหมดเพื่อหาจำนวนนักเรียนที่ไม่ซ้ำกัน
all_unique_students = set().union(*attendance_sets)
print(f"4. จำนวนนักเรียนที่ไม่ซ้ำกันทั้งหมด: {len(all_unique_students)}")