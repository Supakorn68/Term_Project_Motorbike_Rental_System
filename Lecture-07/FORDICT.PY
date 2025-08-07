# สร้างพจนานุกรมของหมายเลขโทรศัพท์
phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333'}

# เพิ่มข้อมูลของ Bart เป็นลิสต์
phonebook['Bart'] = [1, 3, 5]

# นับจำนวนชื่อในสมุดโทรศัพท์
elements = len(phonebook)
print('มีทั้งหมด ', elements, ' รายชื่อในสมุดโทรศัพท์')

# แสดงชื่อและหมายเลขโทรศัพท์ของแต่ละคน
for key in phonebook:
    print(key, 'หมายเลขโทรศัพท์คือ: ', phonebook[key])

# เปลี่ยนค่าลำดับที่ 1 ในลิสต์ของ Bart เป็น 9
phonebook['Bart'][1] = 9
print(phonebook)
