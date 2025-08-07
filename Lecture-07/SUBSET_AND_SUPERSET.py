# กำหนดเซ็ตต่างๆ
set_a = {1, 2, 3, 4}
set_b = {2, 3}
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 4, 5}

# Supersets และ Subsets
# ตรวจสอบว่า set_a เป็น superset ของ set_b หรือไม่
print("Is set_a a superset of set_b?:", set_a >= set_b)  # ผลลัพธ์: True
# ตรวจสอบว่า set_b เป็น subset ของ set_a หรือไม่
print("Is set_b a subset of set_a?:", set_b <= set_a)  # ผลลัพธ์: True

# Proper Superset และ Proper Subset
# ตรวจสอบว่า set_a เป็น proper superset ของ set_b หรือไม่ (เป็น superset แต่ไม่เท่ากัน)
print("Is set_a a proper superset of set_b?:", set_a > set_b)  # ผลลัพธ์: True
# ตรวจสอบว่า set_b เป็น proper subset ของ set_a หรือไม่ (เป็น subset แต่ไม่เท่ากัน)
print("Is set_b a proper subset of set_a?:", set_b < set_a)  # ผลลัพธ์: True

# Equal Sets
# ตรวจสอบว่า set_a และ set_c เท่ากันหรือไม่
print