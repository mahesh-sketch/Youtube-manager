import json

#load data
def load_data(filename,mode):
    try:
        with open(filename,mode) as file:
            test =  json.load(file)
            return test
    except FileNotFoundError:
        return []

#save data in file
def save_data_helper(videos):
    try:
        with open("Youtube.txt",'w') as file:
            json.dump(videos,file)
    except:
        print("Something error occured")

#List all videos
def list_all_videos(videos):
    try:
        print("\n")
        print("*" * 70)
        for index, video in enumerate(videos,start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']} ")
        print("\n")
        print("*" * 70)
    except:
        print("Something error occured")

#add videos
def add_video(videos):
   try:
       name = input("Enter video name: ")
       time = input("Enter video time: ")
       videos.append({'name': name, 'time':time})
       save_data_helper(videos)
       print("Added Successfully")

   except:
       print("Something error occured")
       
#update videos
def update_video(videos):
    try:
        list_all_videos(videos)
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            videos[index-1] = {'name': name,'time': time}
            save_data_helper(videos)
            print("Updated Successfully")
        else:
            print("Invalid index selected !")
    except:
        print("Something error occured")
        
#delete videos
def delete_video(videos):
    try: 
        list_all_videos(videos)
        index = int(input("Enter the video number to delete: "))
        if 1 <= index <= len(videos):
            del videos[index-1]
            save_data_helper(videos)
            print("Deleted Successfully")
        else:
            print("Invalid index selected !")
    except:
        print("Something error occured")
