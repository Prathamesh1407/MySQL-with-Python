from DBHelper import DBHelper

# helper=DBHelper()
# # helper.insert_user(452,"Yash","123422")
# # helper.insert_user(142,"Yashi","12342")
# # helper.insert_user(152,"Yasha","12422")
# # helper.fetch_all()
# # helper.delete_user(142)
# helper.update_user(452,"Swami")
# helper.fetch_all()


def main():
    
    ch = int(input("0 : New Database \n1 : Existing Database \n"))
    flag=1
    while flag==1:
        try:
            pword=input("Enter password to your Database ")
            db = DBHelper(ch,pword)
            flag=0
        except Exception as e:
            flag=1
            print(e)
    ch2 = int(input("0 : New Table \n1 : Existing Table \n"))
    tname = ""
    if ch2 == 0:
        tname = input("Enter New Table name ")
        db.create(tname)
    else:
        db.printTables()
        tname = input("Enter the Table name ")

    # print(db.showColumns(tname))
    while True:
        print("1:Insert")
        print("2:Display All user")
        print("3:Delete user")
        print("4:Update")
        print("5.Delete all")
        print("6.Search")
        print("7.Add Attribute")
        print("8.Remove Attribute")
        print("9.Exit")
        print()
        try:
            choice = int(input())
            if choice == 0:
                db.create()
                pass
            elif choice == 1:
                db.insert_user(tname)
                pass
            elif choice == 2:
                db.fetch_all(tname)
                pass
            elif choice == 3:
                db.delete_user(tname)
                pass
            elif choice == 4:
                db.update_user(tname)
                pass
            elif choice == 5:
                db.delete_all(tname)
                pass
            elif choice == 6:
                db.search(tname)
                pass
            elif choice == 7:
                db.addAtri(tname)
                pass
            elif choice == 8:
                db.delAtri(tname)
                pass
            elif choice == 9:
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
