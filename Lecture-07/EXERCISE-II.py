# ข้อมูลตัวอย่างผลการปฏิบัติงานของพนักงาน
performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

# 1. คำนวณคะแนนเฉลี่ยของพนักงานแต่ละคน
employee_averages = {}
for department, employees in performance_data.items():
    # สร้าง dict ย่อยสำหรับเก็บคะแนนเฉลี่ยของพนักงานในแผนกนั้นๆ
    employee_averages[department] = {}
    for employee_name, scores in employees.items():
        average = sum(scores) / len(scores)
        employee_averages[department][employee_name] = average

# 2. หาพนักงานที่ทำผลงานดีที่สุดในแต่ละแผนก
top_performers_by_dept = {}
for department, employees in employee_averages.items():
    # หาชื่อพนักงานที่มีคะแนนเฉลี่ยสูงสุดในแผนก
    top_employee_name = max(employees, key=employees.get)
    top_performers_by_dept[department] = {
        "name": top_employee_name,
        "average_score": employees[top_employee_name]
    }

# 3. หาแผนกที่มีคะแนนผลงานเฉลี่ยสูงสุด
department_averages = {}
for department, employees in performance_data.items():
    # รวบรวมคะแนนทั้งหมดในแผนกมาไว้ใน list เดียว
    all_scores_in_dept = [score for score_list in employees.values() for score in score_list]
    dept_average = sum(all_scores_in_dept) / len(all_scores_in_dept)
    department_averages[department] = dept_average

# หาชื่อแผนกที่มีคะแนนเฉลี่ยสูงสุด
best_department_name = max(department_averages, key=department_averages.get)

# 4. ค้นหาพนักงานที่มีผลงานดีขึ้นอย่างต่อเนื่อง
def has_continuous_improvement(scores):
    """
    ฟังก์ชันตรวจสอบว่าคะแนนมีการพัฒนาต่อเนื่อง (ไม่ลดลง) หรือไม่
    จะคืนค่า True หากคะแนนเพิ่มขึ้นหรือคงที่, False หากมีคะแนนลดลง
    """
    for i in range(len(scores) - 1):
        if scores[i+1] < scores[i]:
            return False
    return True

improving_employees = []
for department, employees in performance_data.items():
    for employee_name, scores in employees.items():
        if has_continuous_improvement(scores):
            improving_employees.append(employee_name)

# 5. สร้างรายงานสรุป 📊
print("="*40)
print("## รายงานสรุปผลการปฏิบัติงานประจำปี ##")
print("="*40)

# --- ส่วนที่ 1: คะแนนเฉลี่ยของพนักงาน ---
print("\n## 1. คะแนนเฉลี่ยของพนักงาน (รายบุคคล) ##")
for department, employees in employee_averages.items():
    print(f"\n**แผนก: {department}**")
    for employee_name, average in employees.items():
        print(f"- {employee_name}: {average:.2f} คะแนน")

print("\n" + "-"*40)

# --- ส่วนที่ 2: พนักงานดีเด่น ---
print("\n## 2. พนักงานดีเด่นประจำแผนก ##")
for department, top_performer_info in top_performers_by_dept.items():
    name = top_performer_info['name']
    score = top_performer_info['average_score']
    print(f"- แผนก {department}: **{name}** (เฉลี่ย {score:.2f} คะแนน)")

print("\n" + "-"*40)

# --- ส่วนที่ 3: แผนกยอดเยี่ยม ---
print("\n## 3. แผนกที่มีผลงานเฉลี่ยสูงสุด ##")
top_score = department_averages[best_department_name]
print(f"🏆 **{best_department_name}** (เฉลี่ย {top_score:.2f} คะแนน)")

print("\n" + "-"*40)

# --- ส่วนที่ 4: พนักงานที่มีการพัฒนาต่อเนื่อง ---
print("\n## 4. พนักงานที่มีการพัฒนาอย่างต่อเนื่อง ##")
if improving_employees:
    for name in improving_employees:
        print(f"- {name}")
else:
    print("ไม่มีพนักงานที่มีการพัฒนาอย่างต่อเนื่อง")

print("\n" + "="*40)