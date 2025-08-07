# เซ็ตเริ่มต้น
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# &= Intersection Update: set1 จะถูกอัปเดตให้เหลือเฉพาะสมาชิกที่มีอยู่ในทั้งสองเซ็ต
set1 &= set2
print("After &= operation:", set1)  # Output: {4, 5}

# รีเซ็ต set1 ให้กลับสู่ค่าเริ่มต้น
set1 = {1, 2, 3, 4, 5}

# -= Difference Update: set1 จะถูกอัปเดตเพื่อลบสมาชิกที่มีอยู่ใน set2 ออก
set1 -= set2
print("After -= operation:", set1)  # Output: {1, 2, 3}

# รีเซ็ต set1 ให้กลับสู่ค่าเริ่มต้น
set1 = {1, 2, 3, 4, 5}

# ^= Symmetric Difference Update: set1 จะถูกอัปเดตเพื่อคงไว้เฉพาะสมาชิกที่อยู่ในเซ็ตใดเซ็ตหนึ่งเท่านั้น
set1 ^= set2
print("After ^= operation:", set1)  # Output: {1, 2, 3, 6, 7}