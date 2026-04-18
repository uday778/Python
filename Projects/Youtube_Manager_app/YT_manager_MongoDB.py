from bson import ObjectId
from  pymongo import MongoClient

client=MongoClient("mongodb+srv://udaysiddu492_db_user:9DNmKol4lIPdYpvQ@cluster0.txaipbd.mongodb.net/",5000)
db=client["YT_manager"]
video_collection=db["videos"]
print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name:{video['name']}, Time:{video['time']}")

def add_video(name,time):
    video_collection.insert_one({'name':name,'time':time})

def update_video(video_id,name,time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set":{"name":name,"time":time}}
        )

def delete_video(video_id):
     video_collection.delete_one(
        {'_id':ObjectId(video_id)}       
        )



def main():
    while True:
        print("\n Youtube Manager App With DB")
        print("1. List All Videos")
        print("2. Add New Videos")
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
            name=input("Enter The Updated Video Name:  ")
            time=input("Enter the Update Video time:  ")
            update_video(video_id,name,time)
        elif choice=='4':
            video_id=input("Enter Video ID to delete:  ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid Choice Entered")




if __name__ == "__main__":
    main()

