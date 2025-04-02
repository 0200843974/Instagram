import json
import re
import time
from output import *
import posts



#This section reads information from the "users.json" and stores it in var "Users"
with open("database/users.json","r") as jsonFile:
    Users = json.load(jsonFile)

#This section reads information from the "posts.json" and stores it in var "Posts"
with open("database/posts.json","r") as jsonFile:
    Posts = json.load(jsonFile)



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
                #codes here
                m_info("Stories")
                
            elif command == "2":
                #codes here
                m_info("Posts")
                posts.post(username)
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