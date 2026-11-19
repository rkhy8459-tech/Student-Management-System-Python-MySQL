from db_connect import myself
def delete_data():
    conn=myself()
    cursor=conn.cursor()
    
    roll_no=int(input("ENTER YOUR ROLL NUMBER:"))
    query="delete from students where roll_no=%s"
    data=(roll_no,)

    cursor.execute(query,data)
    conn.commit()
    if cursor.rowcount>0:
        print("DELETED")
    else:
        print("NOT FOUND")
    conn.close()



