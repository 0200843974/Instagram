import json
from output import *
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

with open("database/posts.json", "r", encoding="utf-8") as jsonFile:
    posts = json.load(jsonFile)
with open("database/users.json", "r", encoding="utf-8") as jsonFile:
    users = json.load(jsonFile)

def post(username) :
    
    for key in posts :
        
        if users[posts["author"]]["type"] == "public" or \
           users[posts["author"]] in users[username]["followers"] or \
           f"#{users[posts["author"]]["type"]} " in posts[key]["caption"]:
            
            flag = True
            flag1 = True
            while True :
                
                post = posts[key]
                m_info(f"👤 {post["author"]}")
                m_info(f"{post["year"]}/{post["month"]}/{post["day"]}")
                m_info(f"\"{ post["caption"]}\" ✨ \n")
                m_info("------------------------------------\n")
                m_info(f"{post["comment"]} comments\t{post["like"]} ")
                m_info(f"likes {post["share"]} shares \t {post["save"]} saves \n ")
                m_info("------------------------------------\n")
                m_info("comments :")
                
                for comment in post["comments"] :
                    print(f"{comment[0]} : {comment[1]}")
                    
                #navigating through menu    
                m_info("====================================\n")
                t_select("press 1 to comment\npress 2 to like\npress 3 to save")
                t_select("press 4 to share\npress 5 to see the next post \n press 6 to exit")
                t_select("choice:")
                press = input()
                
                if press == "1" :
                    
                    cmnt = input("type '' to go back or \n type your comment here :")
                    if cmnt != '':
                        posts[key]["comments"] = [username , cmnt]
                        posts[key]["comment"] += 1
                        print(m_success("comment added successfully"))
                        input("press anything to continue")
                    clear_console()
                    
                elif press == "2" :
                    
                    if flag :
                        
                        posts[key]["like"]+=1
                        flag = False
                        m_success("you liked this post ")
                        input("press anything to continue")
                        
                    else :
                        
                        t_description("you have already liked this1 post")
                        t_select("press 1 to take the like back \npress anything to continue")
                        decision=input()
                        if decision == "1" :
                            posts[key]["like"]-=1
                            flag = True   
                            
                    clear_console()
                
                elif press == "3" :
                    
                    if flag1:
                        
                        users[username]["saves"].append(key)
                        posts[key]["save"] += 1
                        m_success("saved successfully")
                        input("press anything to continue")
                        flag1 = False
                        
                        
                    else :
                        
                        t_description("this post is already saved")
                        t_select("press 1 to remove from saves \npress anything to continue:")
                        decision = input()
                        
                        if decision == 1 :
                            users[username]["saves"].remove(key)
                            posts[key]["save"] -= 1
                            m_success("removed successfully")
                            input("press anything to continue")
                            flag1 = True
                    clear_console()
                        
                elif press == "4" :
                    
                    for k in users[username]["folloing"]:
                        print(f"{users[username]["folloing"].index(k)+1}.{k}")
                        
                    t_description("to whom would you like to send this post?")
                    t_select("just type the corresponding number down:")
                    num = input()
                    try:
                        sent = users[username]["folloing"][num-1]
                        chat()
                        posts[key]["share"] += 1
                        
                    except:
                        m_error("invalid input press anything to go back ")
                        input()
                        
                    clear_console()

                elif press ==  "5" :
                    clear_console()
                    break
                
                elif press == "6" :
                    break
                    
                else:
                    raise Exception("The input is invalid try again")
            if press == 6 :
                
                with open("posts.json", "w", encoding="utf-8") as file:
                    json.dump(posts, file, indent=4, ensure_ascii=False)
                with open("users.json", "w", encoding="utf-8") as file:
                    json.dump(users, file, indent=4, ensure_ascii=False)
                clear_console()
                break   

post()