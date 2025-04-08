import json
from output import *
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

with open("database/users.json", "r", encoding="utf-8") as jsonFile:
    users = json.load(jsonFile)

def request(username) :
    while True :
    
        counter = 1
        if  len(users[username]["request"]) != 0:
            for i in users[username]["request"]:
                m_info(i) 
                counter += 1
            t_description("which one do you want to respond to ?")
            t_description("write back to go back")
            choice = input()
            
            if choice == "back":
                clear_console()
                break
            
            else :
                try :
                    req = users[username]["request"][int(choice)-1] 
                except:
                    m_error("invalid input, press anythig to continue")
                    input()
                    continue
                t_description("to accept press 1")
                t_description("to reject press 2")
                decision = input() 
                
                if decision == "1" :
                    users[username]["request"].remove(req)
                    users[username]["followers"].append(req)
                    users[username]["followers_count"] += 1
                    users[req]["folloing"].append(username)
                    users[req]["following_count"] +=1
                    m_success("accepted the request")
                    input("press anything to continue")
                    clear_console()
                
                elif decision == "2" :
                    users[username]["request"].remove(req)
                    m_error("request rejected")
                    input("press anythinng to continue")
                    clear_console()
                    
                else:
                    raise Exception("The input is invalid try again")
                
                space()

        else:
            t_description("no following requests yet")
            input("press anything")
    
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
    clear_console() 