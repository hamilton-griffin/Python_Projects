import datetime
import os
import sys
import time
import getpass
import socket
import random
import urllib
from crypto_game import *
#
#
#
#
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()
#
user_index = []
pass_index = []
#
#
username_DB_LOG_PATH = 'PROJECTS\GAMES\Python\userDB.txt'
dataDB = open(username_DB_LOG_PATH, 'r')
dataDB_populate = dataDB.readlines()
user_index.append(dataDB_populate)
#
#
admin_user = 'admin'
admin_password = 'admin'
#
#
database_obj = open('data.txt','r+')
# account1 = user_index[1], pass_index[1]
#
#
#
filename = 'data.txt'
file_path = "data.txt"
file_exists = os.path.exists(file_path)
#
#
#
log_filename = 'data_log.txt'
log_file_path = 'data_log.txt'
logFile_exists = os.path.exists(log_file_path)
database_log_obj = open(log_file_path, 'r+')
#
#
passDB_filename = 'passDB.txt'
password_database = open(passDB_filename, 'r+')
#
# website_max = 5
# websites_found = 0
#
#
#
def website():
    websites_found = 0
    website_find = True
    while website_find:
        websites_found = websites_found + 1
        if websites_found == 6:
            website_find = False
            break;
        ip0 = str(random.randint(0, 255))
        ip1 = str(random.randint(0, 255))
        ip2 = str(random.randint(0, 255))
        ip3 = str(random.randint(0, 255))
        url = 'http://' + ip0 + '.' + ip1 + '.'+ ip2 + '.'+ ip3
        print(url)
        try:
            urlContent = urllib.urlopen(url).read()
            if urlContent.find('<html')> -1 or urlContent.find('<HTML')> -1:
                break
        except:
            pass
            print("Found URL: " + url)
            os.system('start ' + url)
#
#
def user_server_connect():
    with open(log_filename, 'a') as log_file:
        date = str(datetime.datetime.now())
        log_file.write('Admin Logged In @ ' + server_ip + ' time: ' + date)
        log_file.write('\n')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('ssh admin@132.95.172.171 -p 22')
    time.sleep(2)
    print('Username: ')
    time.sleep(0.5)
    print('password: ')
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Exchanging keychain at data center NA 132.95.172.171 Time: ' + str(datetime.datetime.now()))
    time.sleep(2.5)
    print('Validating Keychain')
    time.sleep(2)
    print('connnected....')
    time.sleep(2)
    os.system('cls' if os.name =='nt' else 'clear')
    print(user_index)
#
#
def password_server_connection():
    with open(log_filename, 'a') as log_file:
        date = str(datetime.datetime.now())
        log_file.write('Admin Logged In @ ' + server_ip + ' time: ' + date)
        log_file.write('\n')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('ssh admin@51.99.26.177 -p 22')
    time.sleep(2.5)
    print('connection tunnel created.')
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Username: ')
    time.sleep(1.4)
    print('Password: ')
    time.sleep(1.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('key creating at data center NA 51.99.26.177')
    time.sleep(1.3)
    print('log in successful.')
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(password_database.read())
#
#
def admin_functions():
    admin_logged_in = True
    print('---------------------------------------------------')
    print('Admin options:')
    time.sleep(2)
    print('1.) Database check')
    print('2.) Usernames database')
    print('3.) Password Database')
    print('4.) log check')
    print('5.) appending / removing to user database')
    print('6.) appending / removing to password database')
    print('7.) website finder')
    print('---------------------------------------------------')
    while admin_logged_in:
        admin_input = input('# ')
        #
        # option # 1
        #
        if admin_input == "1":
            file_check = True
            while file_check == True:
                if os.stat(file_path).st_size == 0:
                    print('File is empty!')
                    print(file_exists)
                    print('testing done moving along.')
                    time.sleep(5)
                    file_check = False
                else:
                    print('File has data!')
                    print(file_exists)
                    print(database_obj.read())
                    time.sleep(10)
                    print('testing done moving along.')
                    time.sleep(5)
                    file_check = False
        #
        # option # 2
        #
        elif admin_input == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            user_server_connect()
            time.sleep(5)
        #
        # option # 3
        #
        elif admin_input == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            password_server_connection()
            time.sleep(5)
        #
        # option # 4
        #
        elif admin_input == '4':
            log_file_check = True
            while log_file_check:
                if os.stat(log_file_path).st_size == 0:
                    print('File is empty')
                    print('file does exist')
                    time.sleep(2)
                    log_file_check = False
                else:
                    print('file has data')
                    print(logFile_exists)
                    time.sleep(2)
                    print(database_log_obj.read())
                    time.sleep(2)
                    log_file_check = False
                    # need the log functions set up first!
        # 
        # option # 5
        #
        elif admin_input == '5':
            print('appending / removing to the user database')
            append_or_remove = input('append or remove: ')
            if append_or_remove == 'append':
                new_user_append_input = input('Username: ')
                if new_user_append_input in user_index:
                    print(new_user_append_input + ' is already in the dataase.')
                elif new_user_append_input not in user_index:
                    user_index.append(new_user_append_input)
            elif append_or_remove == 'remove':
                username_remove_input = input('Username to remove: ')
                if username_remove_input not in user_index:
                    print(username_remove_input + ' does not exist.')
                elif username_remove_input in user_index:
                    print('found ' + username_remove_input)
                    user_index.remove(username_remove_input)
            else:
                print('not an option provided.')
        #
        # option # 6
        #
        elif admin_input == '6':
            print('appending / removing from the password database')
            append_or_remove_pass_input = input('append or remove: ')
            if append_or_remove_pass_input == 'append':
                new_password_input = input('Password: ')
                if new_password_input in pass_index:
                    print(new_password_input + ' is already in the database')
                elif new_password_input not in pass_index:
                    print(new_password_input + ' not in the database.')
                    print('appending ' + new_password_input + ' to the database now')
            elif append_or_remove_pass_input == 'remove':
                remove_pass_input = input('Password: ')
                if remove_pass_input not in pass_index:
                    print(remove_pass_input + ' was not found in the database')
                elif remove_pass_input in pass_index:
                    print(remove_pass_input + ' was found in the database')
                    print('removing ' + remove_pass_input + ' from the database now')
                    pass_index.remove(remove_pass_input)
            else:
                print('Not and option provided')
        #
        # option # 7
        elif admin_input == "7":
                website()
        #
        elif admin_input == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('---------------------------------------------------')
            print('Admin options:')
            time.sleep(2)
            print('1.) Database check')
            print('2.) Usernames database')
            print('3.) Password Database')
            print('4.) log check')
            print('5.) appending / removing to user database')
            print('6.) appending / removing to password database')
            print('7.) website finder')
            print('---------------------------------------------------')
        #
        #
        else:
            print('not an option provided.')
#
def logged_in():
    main_menu()

#
def new_account():
    new_user = input('New Username: ')
    new_password = input('password for ' + new_user + ': ')
    #
    user_index.append(new_user)
    pass_index.append(new_password)
    date_of_login = str(datetime.datetime.now())
    with open(passDB_filename, 'a') as passDB:
        passDB.write('\n')
        passDB.write('Password: ' + new_password + ' Time: ' + date_of_login)
        passDB.write('\n')
    time.sleep(2)
    print('Account succesfully created.')
    time.sleep(2)
    home_screen()
#
def login():
    running_login = True
    while running_login:
        ask_username = input('Username: ')
        if ask_username not in user_index:
            print('Sorry there is no account with that name.')
        else:
            ask_password = getpass.getpass(prompt = 'Password: ')
            if ask_password not in pass_index:
                print('Sorry there is no account with that password.')
                running_login = False
            else:
                date_of_user = str(datetime.datetime.now())
                with open(log_filename, 'a') as log_file:
                    log_file.write(ask_username + ' Logged In @ ' + server_ip + ' Time: ' + date_of_user)
                    log_file.write('\n')
                logged_in()
                running_login = False
#
#
def admin_login():
    admin_user_ask = input('Username: ')
    if admin_user_ask == admin_user:
        admin_pass_ask = getpass.getpass(prompt = 'Password: ')
        if admin_pass_ask == admin_password:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('You are now logged in as an admin!')
            print('wait as we transfer you to admin functions.')
            time.sleep(3)
            print('connecting to admin@34.58.143.229 -p 22')
            time.sleep(3)
            print('Username: ')
            time.sleep(2)
            print('password: ')
            time.sleep(2)
            print('validating Credintals for admin@34.58.143.229')
            time.sleep(5)
            print('connected to 34.58.143.229 on port 22 as user admin successfully!')
            time.sleep(5)
            with open(log_filename, 'a') as log_file:
                date = str(datetime.datetime.now())
                log_file.write('Admin Logged In @ ' + server_ip + ' time: ' + date)
                log_file.write('\n')
            admin_functions()
        else:
            print('Wrong.')
            quit()
    else:
        print('Wrong.')
        quit()
#
#
def home_screen():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print('connected @ ' + s.getsockname()[0])
    server_ip = s.getsockname()[0]
    s.close()
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    system_run = True
    while system_run:
        print('1.) Register')
        print('2.) login')
        print('3.) Admin')
        command = input('# ')
        if command == '1':
            new_account()
            system_run = False
        elif command == '2':
            login()
            system_run = False
        elif command == "3":
            admin_login()
            system_run = False
#
#
#
#
# home_screen()
#
#
#
# website()
#
################################################################
# all the code above is connected to the input.py file so do not run this file you would want to run the 'input_game.py'
# add code below that is experimental
################################################################
#
#
#
#############################################################################
################################EXPERIMENTAL#################################
# code below is going to try and populate the user index.
#
#
dataDB = open('userDB.txt', 'r')
dataDB_populate = dataDB.readlines()
#print(dataDB_populate)
user_index.append(dataDB_populate)
#print(user_index)
#website()