# พจนานุกรมเริ่มต้น
phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333'}

# แสดงเนื้อหาของพจนานุกรม
print(phonebook)

# ดึงค่าจากคีย์ที่เฉพาะเจาะจง
print(phonebook['Mickey'])
print(phonebook.get('Donald'))

# ตรวจสอบว่ามีคีย์อยู่หรือไม่ก่อนเข้าถึง
key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' not in phonebook')

# เพิ่มและอัปเดตคู่คีย์-ค่า
phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'
print(phonebook)

# ลบคู่คีย์-ค่า
del phonebook['Simpson']
print(phonebook)