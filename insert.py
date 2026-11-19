from db_connect import myself
def insert_data():
    conn=myself()
    cursor=conn.cursor()
    
    roll_no=int(input("ENTER YOUR ROLL NUMBER:"))
    name=input("ENTER YOUR NAME:")
    age=int(input("ENTER YOUR AGE:"))
    course=input("ENTER YOUR COURSE:")

    query="insert into students(roll_no,name,age,course)values(%s,%s,%s,%s)"
    data=(roll_no,name,age,course)

    cursor.execute(query,data)
    conn.commit()
    print("inserted")
    conn.close()

