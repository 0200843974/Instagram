import json
from output import *
import time 
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

with open("database/stories.json", "r", encoding="utf-8") as jsonFile:
    stories = json.load(jsonFile)
    
with open("database/users.json", "r", encoding="utf-8") as jsonFile:
    users = json.load(jsonFile)
    
def stories(username) :
    
    for l in stories:
        
        k = stories[l]
        while (users[stories["author"]]["type"] == "public" and \
            username in users[k["author"]]["followers"] ) or \
            (users[k["author"]] in users[username]["followers"] and \
            username in users[k["author"]]["followers"]) or \
            f"#{users[k["author"][1:len(k["author"])-1]]["type"]} " in k["caption"]:

            if time.now() - k[time] > 86400 :
                m_info(k["caption \n"])
                m_info("------------------------------------------")
                m_info(f"\nlike : {k["like"]} ")
                space()
                t_select("press 1 to like \n press 2 to see the next story")
                t_select("press 3 to go back to menu")
                press = input()
                
                if press == 1 :
                    
                    if username not in  k["like"][1] :
                        
                        k["like"][0]+=1
                        k["like"][1].append(username)
                        m_success("you liked this story ")
                        input("press anything to continue")
                        
                    else :
                        
                        t_description("you have already liked this story")
                        t_select("press 1 to take the like back \npress anything to continue")
                        decision=input()
                        
                        if decision == "1" :
                            k["like"][0]-=1
                            k["like"][1].remove(username)
                    clear_console()
                            
                elif press == 2 :
                    clear_console()
                    break
                    
                elif press == 3 :
                    break
                
                else :
                    raise Exception("The input is invalid try again")
                
            if press == 4 :
                
                with open("stories.json", "w", encoding="utf-8") as file:
                    json.dump(stories, file, indent=4, ensure_ascii=False)
                with open("users.json", "w", encoding="utf-8") as file:
                    json.dump(users, file, indent=4, ensure_ascii=False)
                clear_console()
                break
