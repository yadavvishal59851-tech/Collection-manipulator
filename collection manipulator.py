students = []

while True:
    print("\n1. Add Student")
    print("2.display all students ")
    print("3.update student information ")
    print("4.delete student ")
    print("5.display subjects offered ")
    print("6 .exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
       
        s = {"student id": input("student id: "),"Name": input("Name: "),"Age": input("Age: "),"DOB":input("DOB: "),"grade":input("enter grade : "),
             "Subjects": input("Subjects: ").split(',')}
        students.append(s)
        print("Students are Added")
    elif choice == "2":
        if not students:
            print("student does not have record")
        else:
            print("if students have record")
            for s in students:
                 print(f"Name:{s['Name']}, age:{s['Age']},DOB:{s['DOB']},grade:{s['grade']},std id:{s['student id']},Subjects:{s['Subjects']}")

    elif choice =="3" :
        studentid = input("enter student id to update:")
        for s in students:
            if s["student id"] ==studentid:
                s["Name"] = input("enter new name: ")
                s["Age"] = input("enter new age: ")
                s["DOB"] = input("enter new date of birth: ")
                s["grade"] = input("enter new grade: ")
                s["Subjects"] = input("enter new subjects :)").split(',')
                print("student information updated")
                break
            else:
                print("student not found")
    elif choice =="4":
        studentid =input("enter student id to delete: ")
        for s in students:
            if s["studentid"] ==studentid :
                students.remove(s)
                print("student deleted")
                break
            else:
                print("student not found")
    
        
    
    elif choice == "5":
        Subjects = set()
        for s in students:
            for sub in s["Subjects"]:
                Subjects.add(sub.strip())
        if Subjects:
            print("subject offered ")
            for sub in Subjects:
                print('=',sub)
        else:
            print("subject not found")     

    elif choice =="6":
            print("exit")
            break
    else:
        print("choice doesn't exist,try again")  
    
         