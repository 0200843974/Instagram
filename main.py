import json
import re
import time
from output import *


#This section reads information from the "users.json" and stores it in var "Users"
with open("database/users.json","r") as jsonFile:
    Users = json.load(jsonFile)

#This section reads information from the "posts.json" and stores it in var "Posts"
with open("database/posts.json","r") as jsonFile:
    Posts = json.load(jsonFile)

#regex var
userPat = "^[a-zA-Z0-9_.]{3,20}$"
emailPat = "^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$"
passPat = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

#SHAYAN
def Sign():

    while(True):
        try:
            t_header("Instagram")
            t_description("If you want quit enter 'exit'")
            t_select("1.Sign in")
            t_select("2.Sign up")
            command = input()
            space()

            if command == "exit":
                quit()

            elif command == "1":
                #SignIn enter username
                while(True):
                    try:
                        t_header("Enter your username...")
                        t_description("If you want quit enter 'exit' and if you want back enter 0")
                        command = input()
                        space()

                        if command == "exit":
                            quit()

                        elif command == "0":
                            break

                        elif command in Users.keys():
                            username = command
                            #SignIn enter password
                            while(True):

                                try:
                                    t_header("Enter your password...")
                                    t_description("If you want quit enter 'exit' and if you want back enter 0")
                                    command = input()
                                    space()

                                    if command == "exit":
                                        quit()

                                    elif command == "0":
                                        break

                                    elif command == Users[username]["password"]:
                                        #Successful login
                                        m_success(f"Wellcome {Users[username]['name']}")
                                        space()
                                        return Home(username)
                                    
                                    else:
                                        raise Exception("Password is incorrect!")
                                    
                                except Exception as e:
                                    m_error(e)
                                    space()
                                    continue
                        else:
                            raise Exception("Username does not exist!")
                        
                        space()

                    except Exception as e:
                        m_error(e)
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
                        
                        elif re.match(userPat, command):
                            if command not in Users.keys():
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
                                        
                                        elif re.match(emailPat, command):
                                            if command not in Users[command]["email"]:
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
                                                        
                                                        elif re.match(passPat, command):
                                                            #Successful registration
                                                            password = command
                                                            Users[username] = {
                                                                                "name": username,
                                                                                "email": email,
                                                                                "password": password,
                                                                                "bio": "",
                                                                                "followers_count": 0,
                                                                                "following_count": 0,
                                                                                "posts_count": 0,
                                                                                "followers": [],
                                                                                "folloing": [],
                                                                                "posts": [],
                                                                                "saves": [],
                                                                                "type": "public",
                                                                                "blocked": []
                                                                              }
                                                            #Add user to database users
                                                            with open("database/users.json","w") as json_file:
                                                                json.dump(Users, json_file, indent=3)

                                                            m_success(f"Wellcome {username}")
                                                            space()
                                                            return Home(username)
                                                        
                                                        else:
                                                            raise Exception("Password syntax is invalid!")
                                                        space()

                                                except Exception as e:
                                                    m_error(e)
                                                    space()
                                                    continue
                                                
                                            else:
                                                raise Exception("Email address must be unique!")

                                        else:
                                            raise Exception("Email address syntax is invalid!")
                                        space()

                                except Exception as e:
                                    m_error(e)
                                    space()
                                    continue

                            else:
                                raise Exception("Username must be unique!")
                            
                        else:
                            raise Exception("username syntax is invalid!")
                        space()

                    except Exception as e:
                        m_error(e)
                        space()
                        continue

            else:
                raise Exception("The input is invalid try again!")

        except Exception as e:
            m_error(e)
            space()
            continue
        
    #return Home("iust.instagram")

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
                #codes here
                m_info("Stories")
            elif command == "2":
                #codes here
                m_info("Posts")
            elif command == "3":
                #codes here
                m_info("Chat")
            elif command == "4":
                #dont touch
                return Search(username)
            elif command == "5":
                #codes here
                m_info("Add content")
            elif command == "6":
                #codes here
                m_info("Request")
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

            except Exception as e:
                m_error(e)
                space()
                Profile(username,user_spect)

#The program starts here
Sign()