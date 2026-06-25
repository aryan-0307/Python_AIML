##Students Marks Analyzer

import numpy as np
n = int(input("Enter the total number of subjects: "))

marks = []
for i in range(n):
    student_mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(student_mark)

x = np.array(marks)
print(x)

#Average Marks:
avg_marks = np.mean(x)
print(int(avg_marks))

#Highest and Lowest Marks:
highest_marks = np.max(x)
lowest_marks = np.min(x)
print("highest marks:",highest_marks)
print("lowest marks",lowest_marks)

#Standard Deviation
std_deviation=np.std(x)
print("Standard Deviation of marks:",std_deviation)

#Rank Students
rank_marks=np.sort(x)
print(rank_marks)
