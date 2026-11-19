from db_connect import myself
def view_data():
    conn=myself()
    cursor=conn.cursor()

    query="select * from students"
    cursor.execute(query)
    record=cursor.fetchall()
    conn.commit()
    for i in record:
        print(i)
        conn.close()

