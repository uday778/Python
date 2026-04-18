import sqlite3

con=sqlite3.connect("youtube_videos.db")
cursor=con.cursor()

cursor.execute('''
    CREATE TABLE  IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    con.commit()


def update_video(video_id,new_name,time):
    cursor.execute("UPDATE videos SET name=?,time=? where id=?",(new_name,time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id =?",(video_id,))
    con.commit()
    

def main():
    while True:
        print("\n Youtube Manager App With DB")
        print("1. List All Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete videos")
        print("5. Exit the App")

        choice= input("Enter your Choice :   ")

        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter The Video Name:  ")
            time=input("Enter the Viceo time:  ")
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter Video ID to update:  ")
            name=input("Enter The Video Name:  ")
            time=input("Enter the Viceo time:  ")
            update_video(video_id,name,time)
        elif choice=='4':
            video_id=input("Enter Video ID to delete:  ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid Choice Entered")

    con.close()





if __name__== "__main__":
    main()