phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333', 'Pluto': '777-4444'}

heroesdict = {} # สามารถใช้ heroesdict = dict() ได้
heroesdict['Hulk'] = '888-1111'
heroesdict['Iron Man'] = '888-2222'

print(heroesdict.get('Halk', 'Key not found')) # ผลลัพธ์: Key not found
print(heroesdict.get('Hulk', 'Key not found')) # ผลลัพธ์: 888-1111

for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())
print(phonebook.values())

# ตัวอย่างการใช้ pop() และ popitem()
print(phonebook.pop('Mick', 'Element not found'))
print(phonebook.pop('Mickey', 'Element not found'))
print(phonebook)

print(phonebook.popitem())
print(phonebook)

# การล้างพจนานุกรมทั้งหมด
phonebook.clear()
print('After clear')
print(phonebook)