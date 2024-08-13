from enum import Enum

class Menu(Enum):
    ADD = 1
    REMOVE = 2
    CHECK = 3
    ORDER = 4
    END = 5

class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def check_items(self):
        return self.items

    def clear_items(self):
        self.items = []

def select():
    print("메뉴를 선택하세요:")
    print("1. 아이템 추가")
    print("2. 아이템 제거")
    print("3. 아이템 확인")
    print("4. 주문하기")
    print("5. 종료하기")

def add_menu(item_list):
    item = input("추가할 아이템 이름을 입력하세요: ")
    item_list.add_item(item)
    print(f"{item}이(가) 추가되었습니다.")

def remove_menu(item_list):
    item = input("제거할 아이템 이름을 입력하세요: ")
    if item_list.remove_item(item):
        print(f"{item}이(가) 제거되었습니다.")
    else:
        print(f"{item}이(가) 목록에 없습니다.")

def check_menu(item_list):
    items = item_list.check_items()
    if items:
        print("현재 목록에 있는 아이템들:")
        for item in items:
            print(f"- {item}")
    else:
        print("목록이 비어 있습니다.")

def order(item_list):
    items = item_list.check_items()
    if items:
        print("주문할 아이템들:")
        for item in items:
            print(f"- {item}")
        confirm = input("주문을 완료하시겠습니까? (y/n): ")
        if confirm.lower() == 'y':
            item_list.clear_items()
            return True
    else:
        print("목록이 비어 있어 주문할 수 없습니다.")
    return False

def main():
    item_list = ItemList()
    while True:
        select()
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
                print("주문 완료. 프로그램을 종료합니다.")
                break
            else:
                print("주문 보류!")
                print("\n\n")
        elif choice == Menu.END.value:
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못된 입력입니다. 동작을 취소합니다.")
            break

if __name__ == "__main__":
    main()