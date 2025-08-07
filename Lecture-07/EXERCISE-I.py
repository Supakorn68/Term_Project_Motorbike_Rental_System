# ผลสำรวจ (แต่ละลิสต์แสดงตัวเลือกของผู้เข้าร่วม)
survey_results = [
    ["Python", "JavaScript", "C++"],          # ผู้เข้าร่วม 1
    ["Python", "JavaScript", "C#"],           # ผู้เข้าร่วม 2
    ["Python", "Java"],                       # ผู้เข้าร่วม 3
    ["Python", "C++", "JavaScript"],          # ผู้เข้าร่วม 4
    ["Python", "JavaScript", "C++", "Java"],  # ผู้เข้าร่วม 5
]

# แปลงผลสำรวจเป็นเซ็ตเพื่อให้ง่ายต่อการประมวลผล
choices_sets = [set(p) for p in survey_results]

# 1. ระบุภาษาที่ผู้เข้าร่วมทุกคนเลือก
common_languages = set.intersection(*choices_sets)
print("1. Languages chosen by all participants:", common_languages)

# 2. หาภาษาที่ถูกเลือกโดยผู้เข้าร่วมเพียงคนเดียว
# ใช้การนับความถี่ของแต่ละภาษา
language_counts = {}
for lang_set in choices_sets:
    for lang in lang_set:
        language_counts[lang] = language_counts.get(lang, 0) + 1

only_one_choice = {lang for lang, count in language_counts.items() if count == 1}
print("2. Languages only chosen by one participant:", only_one_choice)

# 3. คำนวณจำนวนภาษาที่ไม่ซ้ำกันทั้งหมดที่กล่าวถึงในการสำรวจ
unique_languages = set.union(*choices_sets)
print("3. Number of unique languages:", len(unique_languages))

# 4. แสดงลิสต์ภาษาที่ถูกเลือกโดยผู้เข้าร่วมเพียง 2 คน
exactly_two_choices = {lang for lang, count in language_counts.items() if count == 2}
print("4. Languages chosen by exactly two participants:", exactly_two_choices)

# 5. หาผู้เข้าร่วมที่มีชุดภาษาโปรดเหมือนกัน
# ใช้พจนานุกรมเพื่อเก็บผู้เข้าร่วมที่มีเซ็ตเหมือนกัน
matching_participants = {}
for i, s in enumerate(choices_sets):
    # ใช้ tuple ของเซ็ตที่เรียงแล้วเป็นคีย์
    key = tuple(sorted(list(s)))
    if key not in matching_participants:
        matching_participants[key] = []
    matching_participants[key].append(i + 1)

same_sets = [participants for participants in matching_participants.values() if len(participants) > 1]
print("5. Participants with the same set of languages:", same_sets)