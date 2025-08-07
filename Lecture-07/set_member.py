# การสร้างเซ็ต
fruits = {"apple", "banana", "cherry"}

# การเพิ่มรายการใหม่ลงในเซ็ตด้วยเมธอด .add()
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# การลบรายการที่ระบุด้วยเมธอด .remove()
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# การลบรายการที่ระบุด้วยเมธอด .discard()
# หากรายการนั้นไม่มีอยู่ในเซ็ต จะไม่มีข้อผิดพลาดเกิดขึ้น
fruits.discard("grape")
print(fruits)  # Output: {'apple', 'cherry', 'orange'} (no error raised)

# การลบรายการแบบสุ่มและส่งคืนค่าที่ถูกลบด้วยเมธอด .pop()
removed_item = fruits.pop()
print(removed_item)
print(fruits)  # Output: {'cherry', 'orange'} (an arbitrary item removed)

# การลบทุกรายการออกจากเซ็ตด้วยเมธอด .clear()
fruits.clear()
print(fruits)  # Output: set() (empty set)