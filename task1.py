dict= {'a':43,'b':35,'c':34}
stu_input= input("Enter the student's name : ")
if stu_input in dict:
    print(f"{stu_input}'s marks :",dict[stu_input])
else:
    print("Student not found.")
