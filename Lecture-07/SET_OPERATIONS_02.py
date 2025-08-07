# สร้างเซ็ต 2 ชุดสำหรับทดสอบ
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: ใช้สัญลักษณ์ |
union_set = set1 | set2
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: ใช้สัญลักษณ์ &
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: {3, 4}

# Difference: ใช้สัญลักษณ์ -
difference_set = set1 - set2
print("Difference:", difference_set)  # Output: {1, 2}

# Symmetric Difference: ใช้สัญลักษณ์ ^
sym_diff_set = set1 ^ set2
print("Symmetric Difference:", sym_diff_set)  # Output: {1, 2, 5, 6}