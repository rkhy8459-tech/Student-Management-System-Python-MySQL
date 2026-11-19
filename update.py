from db_connect import myself
def update_data():
    conn=myself()
    cursor=conn.cursor()
    
    roll_no=int(input("ENTER YOUR ROLL NUMBER:"))
    name=input("ENTER YOUR NAME:")
    age=int(input("ENTER YOUR AGE:"))
    course=input("ENTER YOUR COURSE:")

    query="update students set name=%s ,age=%s ,course=%s where roll_no=%s"
    data=(name,age,course,roll_no)

    cursor.execute(query,data)
    conn.commit()
    if cursor.rowcount>0:
        print("UPDATED")
    else:
        print("NOT FOUND")
    conn.close()

