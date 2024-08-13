from enum import Enum

class Menu(Enum):
    ADD = 1
    REMOVE = 2
    CHECK = 3
    ORDER = 4
    END = 5

class Drinks(Enum):
    아메리카노 = 1
    카페라떼 = 2
    콜드브루 = 3
    에스프레소 = 4
    아이스티 = 5
    말차라떼 = 6

class ItemList:
    def __init__(self):
        self.menu = {
            Drinks.아메리카노: 4500,
            Drinks.카페라떼: 5000,
            Drinks.콜드브루: 4900,
            Drinks.에스프레소: 4000,
            Drinks.아이스티: 5900,
            Drinks.말차라떼: 6100
        }
        self.items = []

    def add_item(self, item):
        if len(self.items) >= 10:
            print("주문은 최대 10잔까지 가능합니다.")
            return
        if item in self.menu:
            self.items.append(item)
            print(f"{item.name}이(가) 추가되었습니다.")
        else:
            print(f"{item.name}은(는) 메뉴에 없습니다.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name}이(가) 제거되었습니다.")
            return True
        print(f"{item.name}이(가) 목록에 없습니다.")
        return False

    def check_items(self):
        return self.items

    def clear_items(self):
        self.items = []

    def get_total_price(self):
        return sum(self.menu[item] for item in self.items)

def select():
    print("음료 메뉴를 선택하세요:")
    for drink in Drinks:
        print(f"{drink.value}. {drink.name}")

def add_menu(item_list):
    print("========== Add Menu ==========")
    select()
    choice = int(input("추가할 음료 번호를 선택하세요: "))
    
    if choice in range(1, len(Drinks) + 1):
        item = Drinks(choice)
        item_list.add_item(item)
    else:
        print("잘못된 선택입니다.")

def remove_menu(item_list):
    print("========== Remove Menu ==========")
    item = input("제거할 음료 이름을 입력하세요: ")
    item_enum = getattr(Drinks, item, None)
    if item_enum:
        item_list.remove_item(item_enum)
    else:
        print(f"{item}은(는) 유효한 음료가 아닙니다.")

def check_menu(item_list):
    items = item_list.check_items()
    if items:
        print("현재 목록에 있는 음료들:")
        for item in items:
            print(f"- {item.name}: {item_list.menu[item]}원")
        total_price = item_list.get_total_price()
        print(f"총 가격: {total_price}원")
    else:
        print("목록이 비어 있습니다.")

def order(item_list):
    items = item_list.check_items()
    if items:
        print("주문할 음료들:")
        for item in items:
            print(f"- {item.name}: {item_list.menu[item]}원")
        total_price = item_list.get_total_price()
        print(f"총 가격: {total_price}원")
        confirm = input("주문하시겠습니까? (y/n): ")
        if confirm.lower() == 'y':
            item_list.clear_items()
            print("주문이 완료되었습니다. 이용해주셔서 감사합니다.")
            return True
    else:
        print("목록이 비어 있어 주문할 수 없습니다.")
    return False

def main():
    item_list = ItemList()
    while True:
        print("========== What Do You Want ==========")
        print("1. 음료 추가")
        print("2. 음료 삭제")
        print("3. 선택 음료 확인")
        print("4. 선택 음료 주문")
        print("5. 프로그램 종료")

        choice = int(input("선택: "))
        print("\n\n")

        if choice == Menu.ADD.value:
            add_menu(item_list)
            print("\n\n")
        elif choice == Menu.REMOVE.value:
            remove_menu(item_list)
            print("\n\n")
        elif choice == Menu.CHECK.value:
            check_menu(item_list)
            print("\n\n")
        elif choice == Menu.ORDER.value:
            if order(item_list):
                break
            else:
                print("주문이 보류되었습니다.")
                print("\n\n")
        elif choice == Menu.END.value:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 동작을 취소합니다.")
            break

if __name__ == "__main__":
    main()
