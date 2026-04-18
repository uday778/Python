# file= open('youtube.txt','w')
# try:
#     file.write('This is a youtube manager app')
#     print('File written successfully')
# except Exception as e:
#     print(f'An error occurred: {e}')
# finally:
#     file.close()
# with open('youtube.txt','w') as file:
#     file.write('chai aur python')


import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
          
            test= json.load(file)
            
            return test
    except (FileNotFoundError,json.JSONDecodeError):
        return []


def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)



def list_allVideos(videos):
    print("\n" + "*" * 70)
    for index,video in  enumerate(videos,start=1):
        
        print(f"{index}. {video['name']}, Buration:{video['time']}")
    print("*" * 70)


def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)


def update_video(videos):
    list_allVideos(videos)
    index=int(input("Enter the Video number to Update"))
    if 1<=index <=len(videos):
        name=input("Enter the new Video name")
        time=input("Enter the new Video time")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index Selected")


def delete_video(videos):
    list_allVideos(videos)
    index=int(input("Enter the video number to Delete"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Video Index Selected")


def main():
        
    videos=load_data()

    while True:
        print("\n Youtube Manager App | Choose an Option ")
        print("1. List All Youtube Videos ")
        print("2. Add a Youtube Video ")
        print("3. Update a Youtube Video Details ")
        print("4. Delete a Youtube Video ")
        print("5. Exit the App ")
        choice=input("Enter your Choice")
        # print(videos)


        match choice:
            case "1":
                list_allVideos(videos)
                
            case "2":
                add_video(videos)
                
            case "3":
                update_video(videos)
                
            case "4":
                delete_video(videos)
                
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()

