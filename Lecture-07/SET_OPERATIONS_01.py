# สร้างเซ็ต 2 ชุดสำหรับทดสอบ
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: การรวมสมาชิกทั้งหมดจากทั้งสองเซ็ต
print(set1.union(set2))  # ผลลัพธ์: {1, 2, 3, 4, 5}

# Intersection: การหาสมาชิกที่ซ้ำกันของทั้งสองเซ็ต
print(set1.intersection(set2))  # ผลลัพธ์: {3}

# Difference: การหาสมาชิกในเซ็ตแรกที่ไม่มีในเซ็ตที่สอง
print(set1.difference(set2))  # ผลลัพธ์: {1, 2}

# Symmetric Difference: การหาสมาชิกที่อยู่ในเซ็ตใดเซ็ตหนึ่ง แต่ไม่อยู่ในทั้งสองเซ็ต
print(set1.symmetric_difference(set2))  # ผลลัพธ์: {1, 2, 4, 5}