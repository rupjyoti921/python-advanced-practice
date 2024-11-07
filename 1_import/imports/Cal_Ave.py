def Calculate_Average(grades):
    total_grade=0
    subject=0
    for grade in grades.values():
        total_grade+=grade
        subject+=1
    ave_grade=round((total_grade/subject),2)
    return ave_grade
