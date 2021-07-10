DB_STUDENT = [
    {
        "name" : "도기",
        "code" : "#000000"
    },
    {
        "name" : "지섭",
        "code" : "#111111"
    }
]

def startApp():
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("1. student list")
    print("2. create student")
    print("3. delete student")
    print("4. exit program")
    print("+++++++++++++++++++++++++++++++++++++++++++++")

    answer = int(input(">>"))

    if answer == 1:
        view_student()
    elif answer == 2:
        create_student()
    elif answer == 3:
        delete_student()
    elif answer == 4:
        print("프로그램 종료할께요")
    else:
        print("[SYSTEM] 잘못입력하셨습니다")
        startApp()

def view_student():
    print("student list")
    for student in DB_STUDENT:
        print(f"학생 이름 : {student['name']}")
        print(f"학생 코드 : {student['code']}")
        print("--------------------------")
    startApp()

def create_student():
    input_name = input("학생이름을 입력해주세요. >>")
    input_code = input("학생 코드를 입력해주세요. >>")

    push_data = {
        "name" : input_name,
        "code" : input_code
    }
            
    DB_STUDENT.append(push_data )

    startApp()
    
def delete_student():
    for student in enumerate(DB_STUDENT):
        print(f"{student[0]} _ {student[1]['name']}")

    input_index = int(input("삭제할 학생의 번호를 선택해주세요. >>"))

    DB_STUDENT.pop(input_index)
    print("입력하신  색상이  삭제되었습니다.")

    startApp()





startApp()