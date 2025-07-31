# grades = [85, 90, 78, 92, 88]
# third_grade = grades.pop(2)
# grades.append(third_grade)
# print(f"Grader after pop: {grades}")

grades = [85, 90, 78, 92, 88]
max_grade = max(grades)
grades.append(grades.index(max_grade))
print(f"Grader after pop: {grades}")