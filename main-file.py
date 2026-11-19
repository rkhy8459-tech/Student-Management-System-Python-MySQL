from db_connect import myself
from insert import insert_data
from view import view_data
from update import update_data
from delete import delete_data

print("""                  -STUDENT MANGEMENT SYSTEM-


          PRESS 1 FOR DATA INSERT-DAT
          PRESS 2 FOR DATA VIEW-DATA
          PRESS 3 FOR DATA UPDATE-DATA
          PRESS 4 FOR DATA DELETE-DATA
          PRESS 5 FOR DATA -EXIT-               """)
while True:
    char=int(input("ENTER NUMBER : "))

    if char==1:
        insert_data()
    elif char==2:
        view_data()
    elif char==3:
        update_data()
    elif char==4:
        delete_data()
    elif char==5:
        print("THANK YOU")
        break
    else:
        print("INVALID NUMBER PLEASE ENTER A VALID DATA")
        
