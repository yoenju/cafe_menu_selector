from admin import Admin
from order import Order


cafe_menus = [
    {
        "name" : "아메리카노",
        "price" : 2700,
        "time" : 60
    },
    {
        "name" :"카페라떼",
        "price" : 3200,
        "time" : 90 
    },
]


print(cafe_menus)



# cafe_menus의 0번 index의 금액 출력

# print(cafe_menus[0]["price"])


def store():
 



    print("ALL MENUS✌")
    for menu in cafe_menus:
        print (menu["name"])
        print(menu["price"])
        print("😊😊😊😊😊😊😊")

    print("다음 중 원하는 텝을 선택해주세요.")
    print("1.음료주문하기")
    print("2.관리자모드")
    print("3.종료하기")

    answer = int(input(">>"))

    if answer==1 :
        print(">음료주문하기")
        Order.selectOrder(cafe_menus)
    elif answer==2:
        print(">관리자모드")
        ans=Admin.selectMenu()

        if(ans==1):
            prev_data=Admin.addMenu()

            cafe_menus.append(prev_data)
            print("새로운 메뉴가 추가되었습니다.")

            store()             
        elif ans ==2:
            re_data = Admin.removeMenu()

            if re_data["flag"]==False:
                print("메뉴 삭제가 취소되었습니다.")
                store()
            else:
                str_data = re_data["name"]

                list_index = 0

                for menu in enumerate(cafe_menus):
                    if menu[1]["name"] == str_data :
                        list_index =menu[0]

                del cafe_menus [list_index]




               
                print("입력하신 메뉴가 삭제되었습니다.")
                store()

        elif ans ==3:
            print("--관리자모드가 종료되었습니다.--")
            store()

        else:
            print("존재하지 않는 텝을 선택하셨습니다. 다시 선택해주세요.")
            store()

       
    elif answer ==99:
        print(">프로그램 종료")
    else :
        print("존재하지 않는 텝을 선택하셨습니다. 다시 선택해주세요.")
        store()


store()








