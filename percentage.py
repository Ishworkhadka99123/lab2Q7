#2.WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint: more than 70%–>distinction, more than 60%–>first, more than 40%–>pass,
# less than 40%–>fail

Math=int(input("The first subject, Math:"))
Science=int(input("The second subject, Science:"))
English=int(input("The third subject,English:"))
Nepali=int(input("The fourth subject,Nepali:"))

Total_marks=(Math+Science+English+Nepali)
print("The total_marks")

Total_percentage=(Math+Science+English+Nepali)/4.0
print("The Total_percentage")

if Total_percentage > 70:
    print("Its a distinction")
elif Total_percentage > 60:
    print("Its a first division")
elif Total_percentage > 40:
    print("Its just pass")
elif Total_percentage < 40:
    print("Its fail")