grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
sr_grades = []
sr_grades.append(sum(grades[0]) / len(grades[0]))
sr_grades.append(sum(grades[1]) / len(grades[1]))
sr_grades.append(sum(grades[2]) / len(grades[2]))
sr_grades.append(sum(grades[3]) / len(grades[3]))
sr_grades.append(sum(grades[4]) / len(grades[4]))
students.sort()
st_gr = dict(zip(students, sr_grades))
print(st_gr)
