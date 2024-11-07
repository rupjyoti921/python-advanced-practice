"""Heading - This practice is from Udemy Fast Api Course and Video number is 39.
Desc - In this video we learned about Imports in python"""

import imports.Cal_Ave as calAve

# from imports.Cal_Ave import Calculate_Average
 
homework_assignment_grades={
    "homework_1": 89,
    "homework_2": 90,
    "homework_3": 75
}

ave_grade=calAve.Calculate_Average(homework_assignment_grades)

# ave_grade=Calculate_Average(homework_assignment_grades)
print("Average Grade of all the subject is : ", ave_grade)