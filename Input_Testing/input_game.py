# LIB
import json
import time
import datetime
import os
from login import *
#
#
#
filename = 'data.txt'
file_path = "data.txt"
file_exists = os.path.exists(file_path)
usersDB_FILE = 'userDB.txt'
#code below reads the data.json file
#file = open('data.json', 'r')
#data = json.load(file)
#print(data)
#
#print(db['info'][0]['name'])
#
#Code below will update the Json file.
#
def input_main_menu():
    file_check = True
    #
    while file_check == True:
        if os.stat(file_path).st_size == 0:
            print('File is empty!')
            print(file_exists)
            print('testing done moving along.')
            time.sleep(2)
            file_check = False
        else:
            print('File has data!')
            print(file_exists)
            print('testing done moving along.')
            time.sleep(2)
            file_check = False
            #
            #
    os.system('cls' if os.name == 'nt' else 'clear')
    #
    name = input('What is your name? ')
    #
    print('Hello ' + name + ' Its nice to meet you!')
    os.system('cls' if os.name == 'nt' else 'clear')
    #
    print('My name is Query!')
    # Information list
    info = []
    # Information list close
    running_loop = True
    collect_info = input("Can I ask you a few questions " + name + "?  Y/N ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('ANSWER WITH A Y OR AN N && IT HAS TO BE CAPITAL')
    while running_loop:
        if collect_info == "Y":
            # collect info accepted by user
            info.append(name)
            age = int(input("What is your age " + name + "? "))
            info.append(age)
            with open(usersDB_FILE, 'a') as user_tinyDB:
                user_tinyDB.write(str(name))
                user_tinyDB.write('\n')
            if age < 16 or age == 16:
                correct_age = input('So ' + name + " It looks like your " + str(age) + " Is this correct? Y/N ")
                if correct_age == "Y":
                    print('Sorry ' + name + " Youre to young to continue.")
                    time.sleep(3)
                    break;
            elif age == 17 or age > 17:
                correct_age = input("So " + name + " you are " + str(age) + "? Y/N ")
                if correct_age == "Y":
                    info.append(datetime.datetime.now())
                    print('It is currently Time: ' + str(datetime.datetime.now()) + " " + name + "!")
                    print("All info has been collected on you Thank you " + name + "!")
                    print(info)
                    #
                    # the code below will searialize the time for json dumping
                    now_time = datetime.datetime.now()
                    # EXPERMENTAL
                    with open(filename, 'a') as f:
                        f.write(str(info))
                        f.write('\n')
                        #
                        # testing login.py
                        running_loop = False
                        home_screen()
        else:
            print('Understood!')
            break;

#
input_main_menu()
#
# EXPERIMENTAL CODE