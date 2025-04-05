import json
import re
import time
import os
from output import *


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#This section reads information from the "users.json" and stores it in var "Users"
with open("database/users.json","r") as jsonFile:
    Users = json.load(jsonFile)
users = Users

#This section reads information from the "posts.json" and stores it in var "Posts"
with open("database/posts.json","r") as jsonFile:
    Posts = json.load(jsonFile)
posts=Posts
    
with open("database/chats.json", "r", encoding="utf-8") as jsonFile:
    chats = json.load(jsonFile)
    
with open("database/stories.json", "r", encoding="utf-8") as jsonFile:
    stories = json.load(jsonFile)
    


#SHAYAN
def Sign():
    return Home("iust.instagram")

#SHOKRI
def Home(username):
    #Use "Users[username]" to access a specific user's information
    while(True):
        try:
            t_header("Home page")
            t_description("if you want quit enter 'exit'")
            t_select("1.Stories")
            t_select("2.Posts")
            t_select("3.Chat")
            t_select("4.Search") #dont touch
            t_select("5.Add content")
            t_select("6.Request")
            t_select("7.Profile") #dont touch
            command = input()
            space()

            if command == "exit":
                quit()
                
            elif command == "1":
                m_info("Stories")
                
            #moving over existing stories 
                for l in stories:
                    
                    flag=False
                    k = stories[l]
                    while (users[stories["author"]]["type"] == "public" and \
                        username in users[k["author"]]["followers"] ) or \
                        (users[k["author"]] in users[username]["followers"] and \
                        username in users[k["author"]]["followers"]) or \
                        f"#{users[k["author"][1:len(k["author"])-1]]["type"]} " in k["caption"]:

            #checking if the story still exixts
                        if time.time() - k[time] > 86400 :
                            m_info(k["caption \n"])
                            m_info("------------------------------------------")
                            m_info(f"\nlike : {k["like"]} ")
                            space()
                            t_select("press 1 to like \n press 2 to see the next story")
                            t_select("press 3 to go back to menu")
                            press = input()
                        
            #liking 
                            if press == 1 :
                                
                                if username not in  k["like"][1] :
                                    
                                    k["like"][0]+=1
                                    k["like"][1].append(username)
                                    m_success("you liked this story ")
                                    input("press anything to continue")
                                    
                                else :
                                    
                                    t_description("you have already liked this story")
                                    t_select("press 1 to take the like back \
                                            \npress anything to continue")
                                    decision=input()
                                    
                                    if decision == "1" :
                                        k["like"][0]-=1
                                        k["like"][1].remove(username)
                                clear_console()
                
            #going to next story                     
                            elif press == 2 :
                                
                                if stories.index(k) != len(stories) - 1:
                                    clear_console()
                                    break
                            
                                else:
                                    t_description("you have seen all the stories ")
                                    input("press anything")
                                    flag=True
                                
                            elif press == 3 :
                                break
                            
                            else :
                                raise Exception("The input is invalid try again")
            
            #removing the story if one day has passed           
                        else:
                            stories.remove(k)   
                        
            #getting out of the story section     
                        if press == 4 or flag :
                            
                            with open("stories.json", "w", encoding="utf-8") as file:
                                json.dump(stories, file, indent=4, ensure_ascii=False)
                            with open("users.json", "w", encoding="utf-8") as file:
                                json.dump(users, file, indent=4, ensure_ascii=False)
                            clear_console()
                            break
            

            
            elif command == "2":
                m_info("Posts")
                #viewing posts 
                def post(username) :
                    
                #moving over posts one by one
                    for key in posts :

                #doing the appropriate stuff on every post        
                        while (users[posts[key]["author"]]["type"] == "public" and \
                            username in users[posts[key]["author"]]["followers"] ) or \
                            (users[posts[key]["author"]] in users[username]["followers"] and \
                            username in users[posts[key]["author"]]["followers"]) or \
                            f"#{users[posts[key]["author"]]}" in posts[key]["caption"] :
                            
                #showing the post   
                            flag = False        
                            flag1 = True
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
                            
                #commenting            
                            if press == "1" :
                                
                                cmnt = input("type '' to go back or \n type your comment here :")
                                if cmnt != '':
                                    posts[key]["comments"] = [username , cmnt]
                                    posts[key]["comment"] += 1
                                    print(m_success("comment added successfully"))
                                    input("press anything to continue")
                                clear_console()
                        
                #like                
                            elif press == "2" :
                                
                                if username not in  posts[key]["like"][1] :
                                    
                                    posts[key]["like"][0]+=1
                                    posts[key]["like"][1].append(username)
                                    m_success("you liked this post ")
                                    input("press anything to continue")
                                    
                                else :
                                    
                                    t_description("you have already liked this post")
                                    t_select("press 1 to take the like back \npress anything to continue")
                                    decision=input()
                                    if decision == "1" :
                                        posts[key]["like"][0]-=1
                                        posts[key]["like"][1].remove(username)

                                clear_console()

                #saving the post       
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
                                
                #sharing                    
                            elif press == "4" :
                                
                                for k in users[username]["folloing"]:
                                    print(f"{users[username]["folloing"].index(k)+1}.{k}")
                                    
                                t_description("to whom would you like to send this post?")
                                t_select("just type the corresponding number down:")
                                num = input()
                                try:
                                    num = int(num)
                                    sent = users[username]["folloing"][num-1]
                                    chat.chat(username,f"{post["author"]}:{post["caption"]}")
                                    posts[key]["share"] += 1
                                    
                                except:
                                    m_error("invalid input press anything to go back ")
                                    input()
                                    
                                clear_console()

                #going to the next post
                            elif press ==  "5" :
                                
                                if posts.index(posts[key]) != len(posts)-1:
                                    clear_console()
                                    break
                            
                                else:
                                    t_description("you have seen all the posts ")
                                    input("press anything")
                                    flag=True
                            
                #getting out of the post section
                            elif press == "6" :
                                break
                                
                            else:
                                raise Exception("The input is invalid try again")
                    
                        if press == 6 or flag:
                            
                            with open("posts.json", "w", encoding="utf-8") as file:
                                json.dump(posts, file, indent=4, ensure_ascii=False)
                            with open("users.json", "w", encoding="utf-8") as file:
                                json.dump(users, file, indent=4, ensure_ascii=False)
                            clear_console()
                            break
                
                post(username)
            
            elif command == "3":
                #codes here
                m_info("Chat")
                #all kind of chats function
                def chat(username,message):
                    
                    while True:
                        
                #showing user chats 
                        counter=1
                        for i in chats :
                            users_chats=[]
                            chat = chats[i]
                            
                            if username in chat["users"]:
                                
                #deciding weather the chat is group or a private chat
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
                        t_select("to start a convo with a new follower press 0")
                        choice=input()
                        
                #leading back to menu
                        if choice == "back":
                            clear_console()
                            break
                        
                #creating a new group chat with followings
                        elif choice == "create" :
                            t_select("who would you like to add?")
                            t_header("your followings:")
                            counter=1
                            
                            for k in users[username]["folloing"]:
                                m_info(counter,k)
                                counter+=1
                                
                            t_description("write down the numbers you \
                                        would like to add with a space in between")
                            add = list(map,int(input().split()))
                            groupusers = []
                            
                            for i in add :
                                groupusers.append(users[username]["folloing"][i-1])
                                
                            t_description("what should the name be?")
                            name = input()
                            chats[f"{len(chats)}"] = { "users":groupusers,
                            "content":[],
                            "name":name }
                        
                #starting a chat with a new following
                        elif choice == "0" :
                            t_header("your followings:")
                            counter=1
                            for k in users[username]["folloing"]:
                                m_info(counter,k)
                                counter+=1
                            t_description("who would you like to text?")
                            newconvo = int(input())
                            chats[f"{len(chats)}"] = { 
                            "users": [username,users[username]["folloing"][newconvo-1] ] ,
                            "content":[],
                            "name":"" }  
                            m_success("chat added successfully")  
                            input("press anything")
                            clear_console()   
                        
                            
                        else:
                            
                #texting in the existing chats
                            try:
                                choice = int(choice)
                                clear_console()
                                for k in users_chats[choice-1]["content"]:
                                    m_info(k[0] ,":" ,k[1])
                                    
                #managing invalid inputs        
                            except:
                                m_error("wrong input")
                                input("press anything to try again")
                                clear_console()
                                continue
                            
                # checking if the func has a message beforehand 
                            if message is str:
                                t_select("press 1 to send \npress anything to go back")
                                decision = input()
                                if decision == 1 :
                                    users_chats[choice-1]["content"].append([username,message])
                                    m_success("message sent successfuly!")
                                    input("press anything to continue")
                                    clear_console()
                                break
                            
                #texting
                            else:
                                t_description("type what you want to send\
                                            and press enter to send the message")
                                text = input()
                                users_chats[choice-1]["content"].append([username,message])
                                m_success("message sent successfuly!")
                                input("press anything to continue")
                                clear_console()
                                
                #updating the database                 
                        with open("chats.json", "w", encoding="utf-8") as file:
                            json.dump(chats, file, indent=4, ensure_ascii=False)
                        with open("users.json", "w", encoding="utf-8") as file:
                            json.dump(users, file, indent=4, ensure_ascii=False)
                        clear_console()
                chat(username)
                
            elif command == "4":
                #dont touch
                return Search(username)
            
            elif command == "5":
                #codes here
                m_info("Add content")
                #description   
                t_header("creation")
                t_select("press 1 to add a story")
                t_select("press 2 to add a post")
                t_select("press anything else to go back  to menu")
                choice = input()
                
            #adding stories
                if choice == "1" :
                    caption = input("please enter the text")
                    check = input ("press 1 to submit \n press anything to cancel")
                    
                    if check == "1" :
                        stories[f"{len(stories)}"] = {
                            "author":username ,
                            "caption":caption,
                            "like":[0,[]] ,
                            "time": time.time()}
                        m_success("added successfully")
                        
            #adding posts
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
            
            #updating database  
                with open("posts.json", "w", encoding="utf-8") as file:
                    json.dump(posts, file, indent=4, ensure_ascii=False)
                with open("users.json", "w", encoding="utf-8") as file:
                    json.dump(users, file, indent=4, ensure_ascii=False)
                with open("stories.json", "w", encoding="utf-8") as file:
                    json.dump(stories, file, indent=4, ensure_ascii=False)
                clear_console()
                
            elif command == "6":
                #codes here
                m_info("Request")
                while True :
        
            #printing the requests 
                    counter = 1
                    if  len(users[username]["request"]) != 0:
                        for i in users[username]["request"]:
                            m_info(i) 
                            counter += 1
                        t_description("which one do you want to respond to ?")
                        t_description("write back to go back")
                        choice = input()
                        
            #going back
                        if choice == "back":
                            clear_console()
                            break
                        
            #responding to arequest
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
                            
            #accepting
                            if decision == "1" :
                                users[username]["request"].remove(req)
                                users[username]["followers"].append(req)
                                users[username]["followers_count"] += 1
                                users[req]["folloing"].append(username)
                                users[req]["following_count"] +=1
                                m_success("accepted the request")
                                input("press anything to continue")
                                clear_console()
                    
            #rejecting      
                            elif decision == "2" :
                                users[username]["request"].remove(req)
                                m_error("request rejected")
                                input("press anythinng to continue")
                                clear_console()
                        
            #invalid input        
                            else:
                                raise Exception("The input is invalid try again")
                            
                            space()

                    else:
                        t_description("no following requests yet")
                        input("press anything")
                
            #updating database
                with open("users.json", "w", encoding="utf-8") as file:
                    json.dump(users, file, indent=4, ensure_ascii=False)
                clear_console() 
                
            elif command == "7":
                #dont touch
                return Profile(username,username)
            
            else:
                raise Exception("The input is invalid try again")
            space()

        except Exception as e:
            m_error(e)
            space()
            continue

#SHAYAN
def Search(username):
    #Use "Users[username]" to access a specific user's information
    while(True):
        try:
            t_header("Search")
            t_description("Search for the username of the persons")
            t_description("if you want quit enter 'exit' and if you want back enter 0")
            command = input()
            space()

            if command == "exit":
                quit()
            elif command == "0":
                return Home(username)
            elif command in Users.keys():
                return Profile(username,command)
            else:
                raise Exception("Username does not exist...")

        except Exception as e:
            m_error(e)
            space()
            continue

#PEYKAN
def Profile(username,user_spect):
    #Use "Users[username]" to access a specific user's information

    t_header(Users[user_spect]["name"])
    t_description(Users[user_spect]["bio"])
    t_description(f"following: {Users[user_spect]['following_count']}")
    t_description(f"follower: {Users[user_spect]['followers_count']}")
    t_description(f"Posts: {Users[user_spect]['posts_count']}")
    space()

    if username != user_spect:
        while(True):

            if user_spect in Users[username]["followers"]:
                follow_text = "Unfollow"
            else:
                follow_text = "Follow"
            
            if user_spect in Users[username]["blocked"]:
                block_text = "Unblock"
            else:
                block_text = "Block"
            try:
                t_description("if you want quit enter 'exit'")
                t_select("0.Back")
                t_select("1.View posts")
                t_select(f"2.{follow_text}")
                t_select(f"2.{block_text}")
                command = input()
                space()

                if command == "exit":
                    quit()
                elif command == "0":
                    return Home(username)
                elif command == "1":
                    #code here
                    m_info("View posts")
                elif command == "2":
                    #code here
                    m_info("View posts")
                elif command == "3":
                    #code here
                    m_info("View posts")
                else:
                    raise Exception("The input is invalid try again")
                space()

            except Exception as e:
                m_error(e)
                space()
                Profile(username,user_spect)

    else:
        while(True):
            try:
                t_description("if you want quit enter 'exit'")
                t_select("0.Back")
                t_select("1.Edit profile")
                t_select("2.View posts")
                t_select("3.Setting")
                command = input()
                space()

                if command == "exit":
                    quit()
                elif command == "0":
                    return Home(username)
                elif command == "1":
                    #codes here
                    m_info("Edit profile")
                elif command == "2":
                    #codes here
                    m_info("View posts")
                elif command == "3":
                    #codes here
                    m_info("Setting")
                else:
                    raise Exception("The input is invalid try again")
                space()

            except Exception as e:
                m_error(e)
                space()
                Profile(username,user_spect)

#The proggram starts here
Sign()