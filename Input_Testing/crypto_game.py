import time
import os
import datetime
#
#
#
global creds
creds = 0
#
global drill_val
global drill_upg
drill_val = 1
drill_upg = 10
drill_num = 1
global sleep_time
sleep_time = 2
global sleep_time_upg
sleep_time_upg = 50

def crypto_drill():
    drilling = True
    global creds
    try:
        while drilling:
            creds += drill_val
            print(creds)
            time.sleep(sleep_time)
            os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        drilling = False
        main_menu()
#
#
def shop_menu():
    print('1) Upgrade Drill amount $' + str(drill_upg))
    print('2) Upgrade time between each drill $' + str(sleep_time_upg))
    print('Back')
    print('$' + str(creds))
#
def shop():
    global creds
    global drill_upg
    global drill_val
    global sleep_time_upg
    global sleep_time
    #
    os.system('cls' if os.name == 'nt' else 'clear')
    #
    print('1) Upgrade Drill amount $' + str(drill_upg))
    print('2) Upgrade time between each drill $' + str(sleep_time_upg))
    print('Back')
    print('$' + str(creds))
    shop_running = True
    while shop_running:
        shop_input = input('# ')
        if shop_input == '1':
            if creds >=  drill_upg:
                creds -= drill_upg
                drill_upg += 150
                drill_val += 2
                print('drill val ' + str(drill_val))
                #print('drill upg val ' + str(drill_upg))
                #print('creds ' + str(creds))
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                shop_menu()
            else:
                print('Sorry you need $' + str(drill_upg-creds) + ' to upgrade')
        elif shop_input == '2':
            if creds >= sleep_time_upg:
                creds -= sleep_time_upg
                sleep_time_upg += 250
                sleep_time -= 0.2
                print(str(sleep_time))
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                shop_menu()

            else:
                print('You need $' + str(sleep_time_upg-creds) + ' to upgrade your time intervals')
        elif shop_input == 'back':
             main_menu()
        else:
            print('not an option that is allowed')
#
#
#
#
def main_menu():
    main_running = True
    print('$' + str(creds))
    print('1) drill')
    print('2) shop')
    while main_running:
        main_menu_input = input('# ')
        if main_menu_input == '1':
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            crypto_drill()
        elif main_menu_input == '2':
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            shop()
        else:
            print('wasnt an option provided!')
#
#
# main_menu()