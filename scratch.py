name = input("Enter your full name: ")
section = input(f"Hi {name}! Enter your Section: ")

prelim_grade = float(input("Enter your Grade in Preliminary Period: "))
midterm_grade = float(input("Enter your Grade in Midterm Period: "))
final_grade = float(input("Enter your Grade in Final Period: "))

final_total_grade = prelim_grade + midterm_grade  + final_grade 
final_total_grade_percentage = round(final_total_grade/3)

if 40 <= prelim_grade and midterm_grade and final_grade <=100:
    if final_total_grade_percentage >= 99 and final_total_grade_percentage <= 100:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.00")
    elif final_total_grade_percentage >= 96 and final_total_grade_percentage <= 98:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.25")
    elif final_total_grade_percentage >= 93 and final_total_grade_percentage <= 95:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.50")
    elif final_total_grade_percentage >= 90 and final_total_grade_percentage <= 92:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.75")
    elif final_total_grade_percentage >= 87 and final_total_grade_percentage <= 89:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.00")
    elif final_total_grade_percentage >= 84 and final_total_grade_percentage <= 86:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.25")
    elif final_total_grade_percentage >= 81 and final_total_grade_percentage <= 83:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.50")
    elif final_total_grade_percentage >= 78 and final_total_grade_percentage <= 80:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.75")
    elif final_total_grade_percentage >= 75 and final_total_grade_percentage <= 77:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 3.00")
    elif final_total_grade_percentage <75:
        print(f"\nName of a Student: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 5.00")   
else:
    print("Error! Grade input must be between the range of 40 - 100")
