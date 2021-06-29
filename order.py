class Order:

    def selectOrder(all_menus):
        for menu in enumerate(all_menus) :
            menu_num = menu[0] +1
            menu_name = menu[1]["name"]
            print(f"[{menu_num}].{menu_name}")
        print("주문하실 메뉴 번호를 입력해주세요")
        select_answer = int(input(">>"))

        select_menu = all_menus[select_answer -1]
        print(f"{select_menu['name']}를 선택하셨습니다.")
        print(f"금액은 {select_menu['price']}원 입니다.")
        print(f"소요시간은 약 {select_menu['time']}초 입니다.")

        print("금액을 투입해주세요") 
        pay = int(input(" : "))

        if select_menu["price"]==pay : 
            print("감사합니다.😍")
            print("거스름 돈은 0원입니다.")

        elif select_menu["price"]>pay :
            print("죄송합니다")
            print("투입금액이 부족합니다. 다시 이용해주세요")

            Order.selectOrder(all_menus)
        elif select_menu["price"]<pay :
            change = pay - select_menu ["price"]
            print("감사합니다.")
            print(f"거스름돈은 {change}원 입니다")