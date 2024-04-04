from db import db_connection
from controller import youtube_controller

def main():
    
    conn,cursor = db_connection.dbConnection("youtube_video.db")
    
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exist the app")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                youtube_controller.list_all_videos(cursor)
            case '2':
                youtube_controller.add_video(cursor,conn)
            case '3':
                youtube_controller.update_video(cursor,conn)
            case '4':
                youtube_controller.delete_video(cursor,conn)
            case '5':
                break
            case _:
                print("Invalid Choice !")
    
    conn.close()

if __name__ == "__main__":
    main()
