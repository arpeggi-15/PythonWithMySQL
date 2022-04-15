from dbhelper import DBHelper
from requests import delete

def main():
    db=DBHelper()
    while True:
        print("******WELCOME******")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter user id: "))
                username=int(input("Enter user name: "))
                userphone=int(input("Enter user phone: "))
                db.insert_user(uid, username, userphone )
            elif choice==2:
                #display user
                db.fetch_all()
            elif choice==3:
                #delete user
                userid=int(input("Enter user id: "))
                db.delete_user(userid)
            elif choice==4:
                #update user
                uid=int(input("Enter user id: "))
                username=int(input("Enter new user name: "))
                userphone=int(input("Enter new user phone: "))
                db.insert_user(uid, username, userphone )
                db.update_user(uid. username, userphone)
            elif choice==5:
                break
            else:
                print("Invalid Input!!")
        except Exception as e:
            print("Try Again!!")




# #main coding
# helper = DBHelper()
# # helper.insert_user(147,"Priyanshu","9982027028")
# # helper.insert_user(157,"Ayush","9982027028")
# # helper.insert_user(189,"Sayan","9982027028")
# # helper.insert_user(1785,"Ankit","9982027028")
# #helper.fetch_all()
# # helper.delete_user(1452)
# # helper.fetch_all()
# helper.update_user(157, 'Ayush Kumar', '6296058532')
 

