

class Admin : 

    def selectMenu():
        print("다음 중 원하는 텝을 선택해주세요")
        print("1.메뉴 추가하기")
        print("2.메뉴 삭제하기")
        answer = int(input(">>"))

        if(answer==1):
            return answer

        elif answer ==2:
            return answer
        elif answer ==3:
            return answer
        else:
            print("존재하지 않는 텝을 선택하셨습니다. 다시 선택해주세요.")
            Admin.selectMenu()
    def addMenu():
        
            print("--추가할메뉴입력--")
            name = input("메뉴명:")
            price = int(input("금액(숫자):"))
            time = int(input("소요시간(숫자)"))


            prev_data = {
                "name" : name,
                "price" : price,
                "time" : time
            }
            return prev_data

    def removeMenu():
        print("--삭제할 메뉴명을 입력해주세요.--")

        name = input("메뉴명 : ")
        print(f"삭제하려는 메뉴가 {name}이 맞습니까?")
        print("1.삭제")
        print("2.취소")

        answer = int(input(">>"))

        flag = True if answer==1 else False

        return_data = {
            "name" : name,
            "flag":flag
        }


        return return_data

        

