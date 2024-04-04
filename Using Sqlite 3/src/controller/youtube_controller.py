
def list_all_videos(cursor):
    try:
        cursor.execute("SELECT * FROM videos")
        print("\n")
        print("*" * 70)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")
        print("*" * 70)    
    except Exception as e:
        print("Something went wrong !",e)


def add_video(cursor,conn):
    try:
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time,))
        conn.commit()
        print("Added Successfully ")
    except Exception as e:
        print("Something went wrong !",e)


def update_video(cursor,conn):
    try:
        list_all_videos(cursor)
        index = int(input("Enter the video number to update: "))
        if 1 <= index:
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name,time,index,))
            conn.commit()
            print("Updated Successfully")
    except Exception as e:
        print("Something went wrong !",e)


def delete_video(cursor,conn):
    try:
        list_all_videos(cursor)
        index = int(input("Enter the video number to Delete: "))
        if 1 <= index:
            cursor.execute("DELETE FROM videos where id = ?",(index,))
        conn.commit()
        print("Deleted Successfully")
    except Exception as e:
        print("Something went wrong !",e)
