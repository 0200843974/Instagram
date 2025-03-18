import json
import re
import time
from output import *

#IMPORTANT#To every One Who is reading this please dont forget to use a m_success or m_error when user does something!

#This section reads information from the "users.json" and stores it in var "Users"
with open("database/users.json","r") as jsonFile:
    Users = json.load(jsonFile)

#This section reads information from the "posts.json" and stores it in var "Posts"
with open("database/posts.json","r") as jsonFile:
    Posts = json.load(jsonFile)

def DataSaver(): ##VERY IMPORTANT## This function is for saving data call it after every data change
    with open("database/users.json", "w") as jsonfile:
        json.dump(Users, jsonfile, indent=4)
    with open("database/posts.json", "w") as jsonfile:
        json.dump(Posts, jsonfile, indent=4)



#SHAYAN
def Sign():
    return Home("iust.instagram")

#SHOKRI
def Home(username):
    #Use "Users[username]" to access a specific user's information
    while(True):
        try:
            t_header("Home page")
            t_select("Stories" , "Posts" , "Chat" , "Search" , "Add content" , "Request" , "Profile" )
            
            command = COMMAND()
            
            space()

            if command == "exit":
                quit()
            elif command == "0":
                #codes here
                m_info("Stories")
            elif command == "1":
                #codes here
                m_info("Posts")
            elif command == "2":
                #codes here
                m_info("Chat")
            elif command == "3":
                #dont touch
                return Search(username)
            elif command == "4":
                #codes here
                m_info("Add content")
            elif command == "5":
                #codes here
                m_info("Request")
            elif command == "6":
                #dont touch
                return Profile(username,username)
            else:
                raise Exception()
            space()

        except Exception:
            m_error("Invalid input!")
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
            command = COMMAND()
            space()

            if command == "exit":
                quit()
            elif command == "0":
                return Home(username)
            elif command in Users.keys():
                return Profile(username,command)
            else:
                raise Exception()

        except Exception:
            m_error("Username does not exist.")
            space()
            continue

#PEYKAN
def Profile(username,user_spect):
    #Use "Users[username]" to access a specific user's information

    t_header(Users[user_spect]["name"])
    t_description(Users[user_spect]["bio"])
    t_description(f"following: {Users[user_spect]['following_count']}")
    t_description(f"followers: {Users[user_spect]['followers_count']}")
    t_description(f"Posts: {Users[user_spect]['posts_count']}")
    
    space()
    if username != user_spect: #This if is for when we are not on our account and we are checking somebody elses profile
        while(True):
            #Determining if the guys is followed or not before and it does the same with block
            if user_spect in Users[username]["followers"]:
                follow_text = "Unfollow"
            else:
                follow_text = "Follow"
            
            if user_spect in Users[username]["blocked"]:
                block_text = "Unblock"
            else:
                block_text = "Block"
                
            
            try:
                t_select("Back" , "View posts" , f"{follow_text}" , f"{block_text}")
                
                command = COMMAND()
                
                space()

                if command == "exit": 
                    quit()
                elif command == "0": 
                    return Home(username)
                elif command == "1": #viewing the posts
                    
                    while True:
                        try:
                            for post in Users[user_spect]["posts"]: # for loop for showing the posts
                                m_post(Posts[post])
                            
                            t_select("Back , Enter a posts name to contribute to the post")
                            
                            
                            command2 = COMMAND()
                                
                            if command2 == 'exit':
                                quit()
                            elif command2 == '0':
                                break
                            elif ( command2 in Posts ) and Posts[command2]['author'] == user_spect :
                                m_post(Posts[command2])
                                t_select("Back" , "Like" , "Comment" , "Save" , "Share" )
                                
                                command = COMMAND()

                                if command == 'exit':
                                    quit()
                                elif command == '0':
                                    break
                                elif command == '1': #handling likes
                                    Posts[command2]["like"] += 1
                                    m_success(f"{command2} Was Liked Succesfully")
                                elif command == '2': #Handling Comments
                                    the_comment = input("Enter Your comment : ")
                                    Posts[command2]["comments"].append([f"{username}" , the_comment])
                                    Posts[command2]["comment"] += 1
                                    m_success("Comment added to the Post Succesfully")
                                elif command == '3':#Handles saving a post
                                    Users[username]["saves"].append(command2)
                                    Posts[command2]["save"] += 1
                                elif command == '4':
                                    pass #At the momment of typing this the Home page is still not done yet so i'll do this part after the home page was complete
                                DataSaver()    
                            space()
                        
                            m_info("View posts")
                        except Exception:
                            m_error("invalid input.")
                            space()
                    m_info("View posts")
                elif command == "2":
                    #Follow & Unfollow
                    if follow_text == "Unfollow":
                        
                        Users[user_spect]["followers"].remove(f"{username}") 
                        Users[user_spect]["followers_count"] -= 1 
                        Users[username]["following"].remove(f"{user_spect}") 
                        Users[username]["following_count"] -= 1 
                        
                    elif follow_text == "Follow":
                        Users[user_spect]["followers"].append(f"{username}") 
                        Users[user_spect]["followers_count"] += 1 
                        Users[username]["following"].append(f"{user_spect}")
                        Users[username]["following_count"] += 1
                    DataSaver()
                    m_info("Follow")
                    #Blocking & Unblocking
                elif command == "3":
                    if block_text == "Unblock":
                        Users[username]["blocked"].remove(f"{user_spect}")  #if we want to unblock the guy 
                    elif block_text == "Block":
                        Users[username]["blocked"].append(f"{user_spect}")  # if we want to block the guy
                    DataSaver()   
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
        while(True):
            try:
                t_select("Back" , "Edit profile" , "View posts" , "Setting")
                
                command = COMMAND()
                space()

                if command == "exit":
                    quit()
                elif command == "0":
                    return Home(username)
                elif command == "1":
                    while True:
                        try:
                            t_select("Back" , "Change Your Name" , "Change Your email" , "Change Your Password" , "Change Your bio")

                            command = COMMAND()
                            if command == "exit":
                                quit()
                            elif command == '0':
                                break
                            elif command == '1':
                                new_name = COMMAND()
                                Users[username]["name"] = new_name
                                m_success("Your Name Changed succesfully")
                            elif command == '2':
                                new_email = COMMAND()
                                Users[username]["email"] = new_email
                                m_success("Your Email Changed succesfully")
                            elif command == '3':
                                new_password = COMMAND()
                                Users[username]["password"] = new_password
                                m_success("Your Password Changed succesfully")
                            elif command == '4':
                                new_bio = COMMAND()
                                Users[username]["bio"] = new_bio
                                m_success("Your bio Changed succesfully")
                            else:
                                raise Exception()
                            DataSaver()
                            space()
                            
                            m_info("Edit profile")
                        except Exception:
                            m_error("The input is invalid!")
                            space()
                elif command == "2":
                    while True:
                        try:
                            t_select("Back")
                            
                            for post in Users[username]["posts"]: # for loop for showing the posts
                                m_post(Posts[post])
                            
                            command2 = COMMAND()
                            
                                
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
                            t_select("Back" , "Change Your Account Type" , "Saved Posts" , "Blocked list" )
                            
                            command2 = COMMAND()
                            
                            if command2 == 'exit':
                                quit()
                            elif command2 == '0':
                                break
                            elif command2 == '1':
                                if Users[username]["type"] == "private":
                                    Users[username]["type"] = "public"
                                    m_success(f"Your Account type Changed to {Users[username]["type"]} Succesfully")
                                elif Users[username]["type"] == "public":
                                    Users[username]["type"] = "private"
                                    m_success(f"Your Account type Changed to {Users[username]["type"]} Succesfully")
                                
                            elif command2 == '2':
                                
                                for saved_posts in Users[username]["saves"]:
                                    m_post(Posts[saved_posts])
                                    
                            elif command2 == '3':
                                
                                for blocked_users in Users[username]["blocked"]:
                                    t_description(blocked_users , "Blocked User")
                                while True:
                                    try:
                                        t_select("Back" , "Change a Blocked users statement")
                                                                                
                                        command3 = COMMAND()
                                        
                                        if command3 == 'exit':
                                            quit()
                                        elif command3 == '0':
                                            break
                                        elif command3 == '1':
                                            while True:
                                                try:
                                                    t_select("Back" , "Type the Username you wish to unblock")
                                                    
                                                    user_name = COMMAND()
                                                    if user_name == 'exit':
                                                        quit()
                                                    elif user_name == '0':
                                                        Home(username)
                                                    else:
                                                        if user_name in Users[username]['blocked']:
                                                            Users[username]['blocked'].remove(user_name)
                                                    DataSaver()
                                                except Exception:
                                                    m_error("invaid input")
                                        else:
                                            m_error("Wrong input!")
                                    except Exception:
                                        m_error("invalid input!")    
                            DataSaver()
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
                Profile(username,user_spect)

#The proggram starts here
Sign()