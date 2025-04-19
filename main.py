"""
IMPORTANT To every One Who is reading this
please dont forget to use a m_success or m_error when user does something!
and the imports below are the libaries we are going to use in our code
"""
import os
import json
import re
import time
from output import space , user_input
from output import t_header , t_description , t_select
from output import m_error , m_success , m_info , m_post

def clear_console() :
    '''This function clears the console'''
    os.system('cls')

#This section reads information from the "users.json" and stores it in var "users"
with open("database/users.json","r" , encoding='utf-8') as jsonFile:
    users = json.load(jsonFile)

#This section reads information from the "posts.json" and stores it in var "posts"
with open("database/posts.json","r" , encoding='utf-8') as jsonFile:
    posts = json.load(jsonFile)

with open("database/chats.json", "r", encoding="utf-8") as jsonFile:
    chats = json.load(jsonFile)

with open("database/stories.json", "r", encoding="utf-8") as jsonFile:
    stories = json.load(jsonFile)

def data_saver():
    """
    VERY IMPORTANT This function is for saving data call it after every time that data changes
    """
    with open("database/users.json", "w" , encoding='utf-8') as jsonfile:
        json.dump(users, jsonfile, indent=4)

    with open("database/posts.json", "w" , encoding='utf-8') as jsonfile:
        json.dump(posts, jsonfile, indent=4)

    with open("database/stories.json", "w", encoding="utf-8") as file:
        json.dump(stories, file, indent=4, ensure_ascii=False)

    with open("database/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

#regex var
USER_PAT = r"^[a-zA-Z0-9_.]{3,20}$"
EMAIL_PAT = r"^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$"
PASS_PAT = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

#SHAYAN
def sign():
    '''This is the function for sign page'''
    while True:
        try:
            t_header("Instagram")
            t_description("If you want quit enter 'exit'")
            t_select("Sign in","Sign up" , s=1)
            command = user_input()
            space()

            if command == "exit":
                quit()

            elif command == "1":
                #SignIn enter username
                while True:
                    try:
                        t_header("Enter your username...")
                        t_description("If you want quit enter 'exit' and if you want back enter 0")
                        command = input()
                        space()

                        if command == "exit":
                            quit()

                        elif command == "0":
                            break

                        elif command in users.keys():
                            username = command
                            #SignIn enter password
                            while True:

                                try:
                                    t_header("Enter your password...")
                                    t_description("If you want quit enter 'exit' and if you want back enter 0")
                                    command = input()
                                    space()

                                    if command == "exit":
                                        quit()

                                    elif command == "0":
                                        break

                                    elif command == users[username]["password"]:
                                        #Successful login
                                        m_success(f"Wellcome {users[username]['name']}")
                                        space()
                                        return home(username)

                                    else:
                                        raise Exception()

                                except Exception:
                                    m_error("Password is incorrect!")
                                    space()
                                    continue
                        else:
                            raise Exception()

                        space()

                    except Exception:
                        m_error("Username does not exist!")
                        space()
                        continue

            elif command == "2":
                #SignUp enter Username
                while(True):
                    try:
                        t_header("Enter a username...")
                        t_description("The username must only contain uppercase and lowercase English letters, numbers, and underline '_'")
                        t_description("If you want quit enter 'exit' and if you want back enter 0")
                        command = input()
                        space()

                        if command == "exit":
                            quit()

                        elif command == "0":
                            break
                        
                        elif re.match(USER_PAT, command):
                            if command not in users.keys():
                                #Sign In enter email address
                                username = command
                                try:
                                    while(True):
                                        t_header("Enter an email address...")
                                        t_description("If you want quit enter 'exit' and if you want back enter 0")
                                        command = input()
                                        space()

                                        if command == "exit":
                                            quit()

                                        elif command == "0":
                                            break
                                        
                                        elif re.match(EMAIL_PAT, command):
                                            if command not in [user["email"] for user in users.values()]:
                                                #SignUp enter password
                                                email = command
                                                try:
                                                    while(True):
                                                        t_header("Enter an password...")
                                                        t_description("The password must contain at least 8 characters, including uppercase and lowercase English letters and numbers")
                                                        t_description("If you want quit enter 'exit' and if you want back enter 0")
                                                        command = input()
                                                        space()

                                                        if command == "exit":
                                                            quit()

                                                        elif command == "0":
                                                            break
                                                        
                                                        elif re.match(PASS_PAT, command):
                                                            #Successful registration
                                                            password = command
                                                            users[username] = {
                                                                                "name": username,
                                                                                "email": email,
                                                                                "password": password,
                                                                                "bio": "",
                                                                                "followers_count": 0,
                                                                                "following_count": 0,
                                                                                "posts_count": 0,
                                                                                "followers": [],
                                                                                "following": [],
                                                                                "posts": [],
                                                                                "saves": [],
                                                                                "type": "public",
                                                                                "blocked": []
                                                                              }
                                                            #Add user to database users
                                                            data_saver()

                                                            m_success(f"Wellcome {username}")
                                                            space()
                                                            return home(username)
                                                        
                                                        else:
                                                            raise Exception("Password syntax is invalid!")
                                                        space()

                                                except Exception:
                                                    m_error("Password syntax is invalid!")
                                                    space()
                                                    continue
                                                
                                            else:
                                                raise Exception()

                                        else:
                                            raise Exception()
                                        space()

                                except Exception:
                                    m_error("The Email alreay exists or the syntax is invalid!")
                                    space()
                                    continue

                            else:
                                raise Exception("Username must be unique!")
                            
                        else:
                            raise Exception("username syntax is invalid!")
                        space()

                    except Exception:
                        m_error("The Username alreay exists or the syntax is invalid!")
                        space()
                        continue

            else:
                raise Exception("The input is invalid try again!")

        except Exception:
            m_error("The input is invalid try again!")
            space()
            continue
        
    #return Home("iust.instagram")


#SHOKRI
def home(username):
    """#Use "users[username]" to access a specific user's information"""
    #Use "users[username]" to access a specific user's information
    while(True):
        try:
            t_header("Home page")
            t_description("if you want quit enter 'exit'")
            t_select("Stories" , "Posts" , "Chat" , "Search" , "Add content" , "Request" , "Profile", s=1)
            command = user_input()
            space()

            if command == "exit":
                quit()
                
            elif command == "1":
                m_info("Stories")
                
                if len(stories) == 0 :
                    m_info("no stories from your followings") 
                    
                else:
                #moving over existing stories 
                    cont = 0
                    for l in stories:
                        
                        k = stories[l]   
                        if users[k["author"]]["type"] == "public" or \
                            (users[k["author"]] in users[username]["followers"] and \
                            username in users[k["author"]]["followers"]) or \
                            f"#{users[k["author"][1:len(k["author"])-1]]["type"]} " in k["caption"] :

                #checking if the story still exixts
                            tim = time.time()
                            if not(tim - k["time"]) > 86400 :
                                
                                m_info(k["caption"])
                                m_info("------------------------------------------")
                                m_info(f"\nlike : {k["like"][0]} ")
                                space()
                                t_select("Like " , "Next Story" , "press 3 to go exit to menu" , s=1)
                                press = user_input()
                            
                #liking 
                                if press == "1" :
                                    
                                    if username not in  k["like"][1] :
                                        
                                        k["like"][0] += 1
                                        k["like"][1].append(username)
                                        m_success("you liked this story ")
                                        input("press anything to continue")
                                        
                                    else :
                                        
                                        t_description("you have already liked this story")
                                        t_select("press 1 to take the like back" , "press anything to continue" , s=1)
                                        decision = user_input()
                                        
                                        if decision == "1" :
                                            k["like"][0] -= 1
                                            k["like"][1].remove(username)
                                    clear_console()
                    
                #going to next story                     
                                elif press == 2 :
                                    cont += 1
                                    clear_console()
                                    break
                                    
                                elif press == 3 :
                                    clear_console()
                                    break
                                
                                            #getting out of the story section     
                                elif press == 4 :
                                    data_saver()
                                    clear_console()
                                    break
                                
                                else :
                                    raise Exception()

                    if cont != 0 :
                        m_success("you have seen all the stories press anything  to continue" )
                        user_input()
                        
                    elif cont == 0 :
                        m_error("no stories that you can see")
                        t_description("press anything to continue")
                        user_input()
                        
            elif command == "2":
                m_info("posts")
                #viewing posts 
                def post(username) :
                    
                    counter = 0
                #moving over posts one by one
                    for key in posts :
                            
                #doing the appropriate stuff on every post        
                        while (users[posts[key]["author"]]["type"] == "public" and \
                            username in users[posts[key]["author"]]["followers"] ) or \
                            (users[posts[key]["author"]] in users[username]["followers"] and \
                            username in users[posts[key]["author"]]["followers"]) or \
                            f"#{users[posts[key]["author"]]}" in posts[key]["caption"] :
                            
                #showing the post           
                            flag1 = True
                            post = posts[key]
                            m_post(post)
                            
                            for comment in post["comments"] :
                                print(f"{comment[0]} : {comment[1]}")
                                
                #navigating through menu    
                            t_select("Comment" , "Like" , "Save" , "Share" , "Next Post" , s=1)
                            press = user_input()
                            
                #commenting
                            if press == "1" :
                                
                                cmnt = input("type '' to go exit  type your comment here :")
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
                                    t_select("Takeback the like" , "press anything to continue" , s=1)
                                    decision = user_input()
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
                                    t_select("Remove from saves" , "press anything to continue:" , s=1)

                                    decision = user_input()
                                    
                                    if decision == 1 :
                                        users[username]["saves"].remove(key)
                                        posts[key]["save"] -= 1
                                        m_success("removed successfully")
                                        input("press anything to continue")
                                        flag1 = True
                                clear_console()
                                
                #sharing                    
                            elif press == "4" :
                                
                                for k in users[username]["following"]:
                                    print(f"{users[username]["following"].index(k)+1}.{k}")
                                    
                                t_description("to whom would you like to send this post?")
                                t_select("just type the corresponding number down:")
                                num = user_input()
                                try:
                                    num = int(num)
                                    sent = users[username]["following"][num-1]
                                    chat(sent,f"{post["author"]}:{post["caption"]}")
                                    posts[key]["share"] += 1
                                    
                                except Exception:
                                    m_error("invalid input press anything to go exit ")
                                    user_input()
                                    
                                clear_console()

                #going to the next post
                            elif press ==  "5" :
                                counter += 1
                                clear_console()
                                break
                            
                #getting out of the post section
                            elif press == "exit" :
                                break
                                
                            else:
                                raise Exception("The input is invalid try again")
                    
                            if press == 6 :
                                data_saver()
                                clear_console()
                                break
                    
                    if counter != 0 :
                        m_success("you have seen all the stories press anything to continue")
                        user_input()
                    elif counter == 0 :
                        m_error("no posts that you can see press anything to continue")
                        user_input()
                     
                post(username)
            
            elif command == "3":
                #codes here
                m_info("Chat")
                #all kind of chats function
                def chat(username, message = ""):
                    
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
                                            m_info(f"{counter} . {k}")
                                            
                                else :
                                    m_info(f"{counter} : {chat["name"]}")
                                    
                                counter += 1
                                users_chats.append(chat)
                                    
                        t_select("which chat? enter the number" , "to create a group write \"create\"" , "to start a convo with a new follower press 0" , s=1) 
                        choice = user_input()
                        
                #leading exit to menu
                        if choice == "exit":
                            clear_console()
                            break
                        
                #creating a new group chat with followings
                        elif choice == "create" :
                            t_select("who would you like to add?")
                            t_header("your followings:")
                            counter=1
                            
                            for k in users[username]["following"]:
                                m_info(f"{counter},{k}")
                                counter+=1
                                
                            t_description("write down the numbers you would like to add with a space in between")
                            add = list(map(int,input().split()))
                            groupusers = []
                            
                            for i in add :
                                groupusers.append(users[username]["following"][i-1])
                                
                            name = input("what should the name be?")
                            chats[f"{len(chats)}"] = { "users":groupusers,
                            "content":[],
                            "name":name }
                        
                #starting a chat with a new following
                        elif choice == "0" :
                            t_header("your followings:")
                            counter = 1
                            for k in users[username]["following"]:
                                m_info(f"{counter}{k}")
                                counter+=1
                            t_description("who would you like to text?")
                            newconvo = int(input())
                            chats[f"{len(chats)}"] = { 
                            "users": [username,users[username]["following"][newconvo-1] ] ,
                            "content":[],
                            "name":"" }  
                            m_success("chat added successfully")  
                            input("press anything")
                            clear_console()   
                         
                        else:
                            
                #texting in the existing chats
                            try:
                                p = int(choice)
                                clear_console()
                                k = users_chats[p - 1]
                                for messag in k["content"] :
                                    m_info(f"{messag[0]}:{messag[1]}")
                                    
                #managing invalid inputs        
                            except Exception:
                                m_error("wrong input")
                                input("press anything to try again")
                                clear_console()
                                continue
                            
                # checking if the func has a message beforehand
                            if message != "":
                                t_select("Send" , s=1)
                                decision = input()
                                if decision == 1 :
                                    i = 1
                                    while i < int(choice):
                                        if username in chats[f"{i}"]["users"] :
                                            i += 1                                    
                                    m_success("message sent successfuly!")
                                    chats[f"{i}"]["content"].append([username, message])
                                    input("press anything to continue")
                                    clear_console()
                                break

                #texting
                            else:
                                t_description("type what you want to send\
                                            ,press enter to send the message")
                                text = user_input()
                                i = 1
                                while i < int(choice):
                                    if username in chats[f"{i}"]["users"] :
                                        i += 1
                                chats[f"{i}"]["content"].append([username, text])
                                m_success("message sent successfuly!")
                                input("press anything to continue")
                                clear_console()
                                
                #updating the database                 
                            data_saver()
                        clear_console()
                chat(username)
                
            elif command == "4":
                #dont touch
                return search(username)
            
            elif command == "5":
                #codes here
                m_info("Add content")
                #description   
                t_header("creation")
                t_select("Add Story" , "Add posts" , "press anything else to go exit  to menu" , s=1)
                choice = user_input()
                
            #adding stories
                if choice == "1" :
                    caption = input("please enter the text :")
                    check = input("press 1 to submit press anything to cancel :")
                    
                    if check == "1" :
                        stories[f"{len(stories)}"] = {
                            "author":username ,
                            "caption":caption,
                            "like":[0,[]] ,
                            "time": time.time()}
                        m_success("added successfully")
                        input("press anything to continue")
                        
            #adding posts
                elif choice == "2" :
                    
                    t_description("please enter the text")
                    caption = user_input()
                    t_description("what year is it?")
                    year = user_input()
                    t_description("what month is it ?")
                    month = user_input()
                    t_description("what day is it ?")
                    day = user_input()
                    t_select(" press 1 to submit press anything to cancel" , s=1)
                    check = user_input ()
                    
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
                    data_saver()
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
                        t_description("write exit to go exit")
                        choice = input()
                        
            #going exit
                        if choice == "exit":
                            clear_console()
                            break
                        
            #responding to arequest
                        else :
                            try :
                                req = users[username]["request"][int(choice)-1] 
                            except Exception:
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
                                users[req]["following"].append(username)
                                users[req]["following_count"] +=1
                                m_success("accepted the request")
                                input("press anything to continue")
                                clear_console()
                                
            #rejecting      
                            elif decision == "2" :
                                users[username]["request"].remove(req)
                                m_success("request rejected")
                                input("press anythinng to continue")
                                clear_console()
                            
            #invalid input        
                            else:
                                raise Exception("The input is invalid try again")
                            
                            space()
                            break

                    else:
                        t_description("no following requests yet")
                        input("press anything")
                        break
                
            #updating database
                data_saver()
                clear_console() 
                
            elif command == "7":
                #dont touch
                return profile(username,username)
            
            else:
                raise Exception("The input is invalid try again")
            space()

        except Exception:
            m_error("SomeThing went wrong!")
            space()
            input()
            clear_console()
            continue

    # while True:
    #     try:
    #         t_header("Home page")
    #         t_select("Stories", "posts" , "Chat" , "Search" , "Add content" , "Request" , "Profile" , "Sign out", s=1)
    #         command = user_input()
    #         space()

    #         if command == "exit":
    #             quit()
    #         elif command == "1":
    #             m_info("Stories")
    #         elif command == "2":
    #             m_info("posts")
    #         elif command == "3":
    #             m_info("Chat")
    #         elif command == "4":
    #             return search(username)
    #         elif command == "5":
    #             m_info("Add content")
    #         elif command == "6":
    #             m_info("Request")
    #         elif command == "7":
    #             return profile(username,username)
    #         elif command == "8":
    #             return sign()
    #         else:
    #             raise Exception()
    #         space()

    #     except Exception:
    #         m_error("Invalid input!")
    #         space()
    #         continue

#SHAYAN
def search(username):
    """#Use "users[username]" to access a specific user's information"""
    while True:
        try:
            t_header("Search")
            t_description("Search for the username of the persons")
            t_description("if you want quit enter 'exit' and if you want back enter 0")
            command = user_input()
            space()

            if command == "exit":
                quit()
            elif command == "0":
                return home(username)
            elif command in users.keys():
                return profile(username,command)
            else:
                raise Exception()

        except Exception:
            m_error("Username does not exist.")
            space()
            continue

#PEYKAN
def profile(username,user_spect):
    """#Use "users[username]" to access a specific user's information"""

    t_header(users[user_spect]["name"])
    t_description(users[user_spect]["bio"])
    t_description(f"following: {users[user_spect]['following_count']}")
    t_description(f"followers: {users[user_spect]['followers_count']}")
    t_description(f"posts: {users[user_spect]['posts_count']}")
    space()
    if username != user_spect:
        while True:
            #Determining if the guys is followed or not before and it does the same with block
            if user_spect in users[username]["followers"]:
                follow_text = "Unfollow"
            else:
                follow_text = "Follow"
            if user_spect in users[username]["blocked"]:
                block_text = "Unblock"
            else:
                block_text = "Block"
            try:
                t_select("Back" , "View posts" , f"{follow_text}" , f"{block_text}")
                command = user_input()
                space()

                if command == "exit":
                    quit()
                elif command == "0":
                    return home(username)
                elif command == "1": #viewing the posts
                    while True:
                        try:
                            for post in users[user_spect]["posts"]: # for loop for showing the posts
                                m_post(posts[post])
                            t_select("Back , Enter a posts name to contribute to the post")
                            command2 = user_input()
                            if command2 == 'exit':
                                quit()
                            elif command2 == '0':
                                break
                            elif ( command2 in posts ) and posts[command2]['author'] == user_spect :
                                m_post(posts[command2])
                                t_select("Back" , "Like" , "Comment" , "Save" , "Share" )
                                command = user_input()

                                if command == 'exit':
                                    quit()
                                elif command == '0':
                                    break
                                elif command == '1': #handling likes
                                    posts[command2]["like"] += 1
                                    m_success(f"{command2} Was Liked Succesfully")
                                elif command == '2': #Handling Comments
                                    the_comment = input("Enter Your comment : ")
                                    posts[command2]["comments"].append([f"{username}", the_comment])
                                    posts[command2]["comment"] += 1
                                    m_success("Comment added to the Post Succesfully")
                                elif command == '3':#Handles saving a post
                                    users[username]["saves"].append(command2)
                                    posts[command2]["save"] += 1
                                elif command == '4':
                                    pass #After the Home page
                                data_saver()
                            space()
                            m_info("View posts")
                        except Exception:
                            m_error("invalid input.")
                            space()
                    m_info("View posts")
                elif command == "2":
                    #Follow & Unfollow
                    if follow_text == "Unfollow":
                        users[user_spect]["followers"].remove(f"{username}")
                        users[user_spect]["followers_count"] -= 1
                        users[username]["following"].remove(f"{user_spect}")
                        users[username]["following_count"] -= 1
                    elif follow_text == "Follow":
                        users[user_spect]["followers"].append(f"{username}")
                        users[user_spect]["followers_count"] += 1
                        users[username]["following"].append(f"{user_spect}")
                        users[username]["following_count"] += 1
                    data_saver()
                    m_info("Follow")
                    #Blocking & Unblocking
                elif command == "3":
                    if block_text == "Unblock":
                        users[username]["blocked"].remove(f"{user_spect}")  #unblock the guy
                    elif block_text == "Block":
                        users[username]["blocked"].append(f"{user_spect}")  #block the guy
                    data_saver()
                    m_info("unfollow")
                else:
                    raise Exception()
                space()

            except Exception:
                m_error("The input is invalid try again")
                space()
                continue
    #if username == user_spect , it was our own account
    else:
        while True:
            try:
                t_select("Back" , "Edit profile" , "View posts" , "Setting")
                command = user_input()
                space()

                if command == "exit":
                    quit()
                elif command == "0":
                    return home(username)
                elif command == "1":
                    while True:
                        try:
                            t_select("Back" ,
                                     "Change Your Name" ,
                                     "Change Your email" ,
                                     "Change Your Password" ,
                                     "Change Your bio")

                            command = user_input()
                            if command == "exit":
                                quit()
                            elif command == '0':
                                break
                            elif command == '1':
                                new_name = user_input()
                                users[username]["name"] = new_name
                                m_success("Your Name Changed succesfully")
                            elif command == '2':
                                new_email = user_input()
                                users[username]["email"] = new_email
                                m_success("Your Email Changed succesfully")
                            elif command == '3':
                                new_password = user_input()
                                users[username]["password"] = new_password
                                m_success("Your Password Changed succesfully")
                            elif command == '4':
                                new_bio = user_input()
                                users[username]["bio"] = new_bio
                                m_success("Your bio Changed succesfully")
                            else:
                                raise Exception()
                            data_saver()
                            space()
                            m_info("Edit profile")
                        except Exception:
                            m_error("The input is invalid!")
                            space()
                elif command == "2":
                    while True:
                        try:
                            t_select("Back")
                            for post in users[username]["posts"]: # for loop for showing the posts
                                m_post(posts[post])
                            command2 = user_input()
                            if command2 == 'exit':
                                quit()
                            elif command2 == '0':
                                break
                            space()
                            m_info("View posts")
                        except Exception:
                            m_error("invalid input!")
                            space()
                elif command == "3":
                    while True:
                        try:
                            t_select("Back" ,
                                     "Change Your Account Type" ,
                                     "Saved posts" ,
                                     "Blocked list" )
                            command2 = user_input()
                            if command2 == 'exit':
                                quit()
                            elif command2 == '0':
                                break
                            elif command2 == '1':
                                if users[username]["type"] == "private":
                                    users[username]["type"] = "public"
                                    m_success(f"Account type Changed to {users[username]['type']}!")
                                elif users[username]["type"] == "public":
                                    users[username]["type"] = "private"
                                    m_success(f"Account type Changed to {users[username]['type']}!")
                            elif command2 == '2':
                                for saved_posts in users[username]["saves"]:
                                    m_post(posts[saved_posts])
                            elif command2 == '3':
                                for blocked_users in users[username]["blocked"]:
                                    t_description(blocked_users , "Blocked User")
                                while True:
                                    try:
                                        t_select("Back" , "Change a Blocked users statement")
                                        command3 = user_input()
                                        if command3 == 'exit':
                                            quit()
                                        elif command3 == '0':
                                            break
                                        elif command3 == '1':
                                            while True:
                                                try:
                                                    t_select("Back" ,
                                                             "Type the Username to unblock")
                                                    user = user_input()
                                                    if user == 'exit':
                                                        quit()
                                                    elif user == '0':
                                                        home(username)
                                                    else:
                                                        if user in users[username]['blocked']:
                                                            users[username]['blocked'].remove(user)
                                                    data_saver()
                                                except Exception:
                                                    m_error("invaid input")
                                        else:
                                            m_error("Wrong input!")
                                    except Exception:
                                        m_error("invalid input!")
                            data_saver()
                            space()
                            m_info("Setting")
                        except Exception:
                            m_error("invalid input")
                            space()
                    m_info("Setting")
                else:
                    raise Exception()
                space()

            except Exception:
                m_error("invalid input")
                space()
                profile(username,user_spect)

#The program starts here
sign()
