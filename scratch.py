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


      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
'''
    if midterm_grade == 99 or midterm_grade == 100:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.00")
    elif midterm_grade == 96 or midterm_grade == 97 or midterm_grade == 98:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.25")
    elif midterm_grade == 93 or midterm_grade == 94 or midterm_grade == 95:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.50")
    elif midterm_grade == 90 or midterm_grade == 91 or midterm_grade == 92:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.75")
    elif midterm_grade == 87 or midterm_grade == 88 or midterm_grade == 89:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.00")
    elif midterm_grade == 84 or midterm_grade == 85 or midterm_grade == 86:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.25")
    elif midterm_grade == 81 or midterm_grade == 82 or midterm_grade == 83:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.50")
    elif midterm_grade == 78 or midterm_grade == 79 or midterm_grade == 80:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.75")
    elif midterm_grade == 75 or midterm_grade == 76 or midterm_grade == 77:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 3.00")
    elif midterm_grade <75:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 5.00")
        
    
    if final_grade == 99 or final_grade == 100:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.00")
    elif final_grade == 96 or final_grade == 97 or final_grade == 98:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.25")
    elif final_grade == 93 or final_grade == 94 or final_grade == 95:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.50")
    elif final_grade == 90 or final_grade == 91 or final_grade == 92:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 1.75")
    elif final_grade == 87 or final_grade == 88 or final_grade == 89:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.00")
    elif final_grade == 84 or final_grade == 85 or final_grade == 86:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.25")
    elif final_grade == 81 or final_grade == 82 or final_grade == 83:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.50")
    elif final_grade == 78 or final_grade == 79 or final_grade == 80:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 2.75")
    elif final_grade == 75 or final_grade == 76 or final_grade == 77:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 3.00")
    elif final_grade <75:
        print(f"Name: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: 5.00")
else:
    print("Error! Grade input must be between the range of 40 - 100")
    
    

conclusion = print(f"\nName: {name}\nSection: {section}\nFinal Grade: {final_total_grade_percentage}\nGPA: ")

if final_total_grade_percentage == int:
    if final_total_grade_percentage == 99 or final_total_grade_percentage == 100:
        (print(f"1.00"))
    elif final_total_grade_percentage == 96 or final_total_grade_percentage == 97 or final_total_grade_percentage == 98:
        (print(f"1.25"))
    elif final_total_grade_percentage == 93 or final_total_grade_percentage == 94 or final_total_grade_percentage == 95:
        print(f"1.50")
    elif final_total_grade_percentage == 90 or final_total_grade_percentage == 91 or final_total_grade_percentage == 92:
        print(f"1.75")
    elif final_total_grade_percentage == 87 or final_total_grade_percentage == 88 or final_total_grade_percentage == 89:
        print(f"2.00")
    elif final_total_grade_percentage == 84 or final_total_grade_percentage == 85 or final_total_grade_percentage == 86:
        print(f"2.25")
    elif final_total_grade_percentage == 81 or final_total_grade_percentage == 82 or final_total_grade_percentage == 83:
        print(f"2.50")
    elif final_total_grade_percentage == 78 or final_total_grade_percentage == 79 or final_total_grade_percentage == 80:
        print(f"2.75")
    elif final_total_grade_percentage == 75 or final_total_grade_percentage == 76 or final_total_grade_percentage == 77:
        print(f"3.00")
    elif final_total_grade_percentage <75:
        print(f"5.00")

'''
