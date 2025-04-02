import json
from output import *
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

with open("database/chats.json", "r", encoding="utf-8") as jsonFile:
    chats = json.load(jsonFile)
    
with open("database/users.json", "r", encoding="utf-8") as jsonFile:
    users = json.load(jsonFile)
    
def chat(username,message):
    
    while True:
        
        counter=1
        for i in chats :
            
            users_chats=[]
            chat = chats[i]
            if username in chat["users"]:
                
                if len(chat["users"]) == 2 :
                    
                    for k in chat["users"]:
                    
                        if username != k :   
                            m_info(counter ,"." ,k)
                            
                else :
                    m_info(counter ,"." ,chat["name"])
                    
                counter += 1
                users_chats.append(chat)
                    
        t_select("which chat? \n if you want to go back write \"back\"")
        t_select("to create a group write \"create\"")
        t_select("to a convo with a new follower press 0")
        choice=input()
        if choice == "back":
            clear_console()
            break
        
        elif choice == "create" :
            t_select("who would you like to add?")
            t_header("your followings:")
            counter=1
            
            for k in users[username]["folloing"]:
                m_info(counter,k)
                counter+=1
                
            t_description("write down the numbers you would like to add with a space in between")
            add = list(map,int(input().split()))
            groupusers = []
            
            for i in add :
                groupusers.append(users[username]["folloing"][i-1])
                
            t_description("what should the name be?")
            name = input()
            chats[f"{len(chats)}"] = { "users":groupusers,
            "content":[],
            "name":name }
        
        elif choice == "0" :
            t_header("your followings:")
            counter=1
            for k in users[username]["folloing"]:
                m_info(counter,k)
                counter+=1
            t_description("who would you like to text?")
            newconvo = int(input())
            chats[f"{len(chats)}"] = { "users": [username,users[username]["folloing"][newconvo-1] ] ,
            "content":[],
            "name":"" }  
            m_success("chat added successfully")  
            input("press anything")
            clear_console()   
        
            
        else:
            
            try:
                choice = int(choice)
                clear_console()
                for k in users_chats[choice-1]["content"]:
                    m_info(k[0] ,":" ,k[1])
                    
            except:
                m_error("wrong input")
                input("press anything to try again")
                clear_console()
                continue

            if message is str:
                t_select("press 1 to send \npress anything to go back")
                decision = input()
                if decision == 1 :
                    users_chats[choice-1]["content"].append([username,message])
                    m_success("message sent successfuly!")
                    input("press anything to continue")
                    clear_console()
                
            else:
                t_description("type what you want to send and press enter to send the message")
                text = input()
                users_chats[choice-1]["content"].append([username,message])
                m_success("message sent successfuly!")
                input("press anything to continue")
                clear_console()
                
