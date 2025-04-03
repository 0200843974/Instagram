import json
from output import *
import os
import time
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

with open("database/posts.json", "r", encoding="utf-8") as jsonFile:
    posts = json.load(jsonFile)
    
with open("database/users.json", "r", encoding="utf-8") as jsonFile:
    users = json.load(jsonFile)

with open("database/stories.json", "r", encoding="utf-8") as jsonFile:
    stories = json.load(jsonFile)


def create(username):
    
    t_header("creation")
    t_select("press 1 to add a story")
    t_select("press 2 to add a post")
    t_select("press anything else to go back  to menu")
    choice = input()
    
    if choice == "1" :
        caption = input("please enter the text")
        check = input ("press 1 to submit \n press anything to cancel")
        
        if check == "1" :
            stories[f"{len(stories)}"] = {
                "author":username ,
                "caption":caption,
                "like":[0,[]] ,
                "time": time.now()}
            m_success("added successfully")
            
    elif choice == "2" :
        
        t_description("please enter the text")
        caption = input()
        t_description("what year is it?")
        year = input()
        t_description("what month is it ?")
        month = input()
        t_description("what day is it ?")
        day = input()
        t_select(" press 1 to submit \n press anything to cancel")
        check = input ()
        
        if check == "1" :
            users[username]["posts_count"] += 1
            users[username]["posts"].append(f"{len(posts)}")
            posts[f"{len(posts)}"] =\
            {
            "author":"iust.instagram",
            "year": year,
            "month": month,
            "day": day,
            "caption":"today was a wonderful day",
            "like": [0,[]],
            "comment": 0,
            "save": 0,
            "share": 0,
            "comments": []
            }  
            m_success("added successfully")
     
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
    with open("stories.json", "w", encoding="utf-8") as file:
        json.dump(stories, file, indent=4, ensure_ascii=False)
    clear_console()
    
    