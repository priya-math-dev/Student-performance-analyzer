#🎓Student performance Analyzer
#Student data
students=[{"name":"Arjun","marks":[85,78,90]},
         {"name":"Bala","marks":[40,35,30]},
        {"name":"chitra","marks":[95,92,96]},
        {"name":"Diya","marks":[60,65,58]}]
#Average Calculate function
def Calculate_average(marks):
    return sum(marks)/len(marks)
#Assign Grade Function
def Get_Grade(avg):
    if avg>=90:
        return "A"
    elif avg>=75:
        return "B"
    elif avg>=50:
        return "C"
    else:
        return "Fail"
#FindTopper Student Function
def Find_Topper(students):
    toper_name=""
    highest_avg=0
    for stu in students:
        avg=Calculate_average(stu["marks"])
        if avg>highest_avg:
            highest_avg=avg
            toper_name=stu["name"]
    return toper_name,highest_avg
#Fail Student function
def Find_Failstudent(students):
    fail_list=[]
    for stu in students:
        avg=Calculate_average(stu["marks"])
        if avg<50:
            fail_list.append(stu["name"])
    return fail_list

#Main program execution
print("Student Performance Report")
print("_____________________________")
for stu in students:
    avg=Calculate_average(stu["marks"])
    grade=Get_Grade(avg)

    print("name:",stu["name"])
    print("marks:",stu["marks"])
    print("Average:",round(avg,2))
    print("grade:",grade)
    print("__________________________")

#Topper details
topper,top_mark=Find_Topper(students)
print("Topper:",topper,"with average:",round(top_mark))
#Fail student List
fail_stu=Find_Failstudent(students)
print("Failstudent:",fail_stu)



