# กำหนดค่าเริ่มต้นของเซ็ต
setA = {1, 2, 3, 4}
setB = set([8, 9, 10])

# เพิ่มสมาชิก
setA.add(5)
setB.update({6, 7})

# ดำเนินการ Union
Uset = setA | setB
print(Uset)

# พิมพ์จำนวนสมาชิกในเซ็ต
print(len(Uset))

# อัปเดตเซ็ต A
setB.update('ABCD')
setA.update({6, 7, 8})
print(setB)

# ดำเนินการ Intersection
print(setA.intersection(setB))

# ดำเนินการ Symmetric Difference
print(setA ^ setB)

# ลบสมาชิกจากเซ็ต B
setB.remove('B')
setB.discard(10)
print(setB)

# ลบสมาชิกทั้งหมดจากเซ็ต A
print(setA.clear())

# วนลูปเพื่อพิมพ์สมาชิกใน Uset
for val in Uset:
    print(val)