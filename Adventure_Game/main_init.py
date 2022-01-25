########################################################################################################
########################################################################################################
########################################################################################################
#
import os
import cmd
import time
import random
#
# this will be the main looping file that will run everything jumping through the other files and worlds.
#
# the code below is importing all of the local files used in the program and the main loop.
# the code below is getting all of the game settings files used in the game
from Game_Settings.User_Settings.user_main import *
from Game_Settings.Enviroment_Settings.enviro_main import *
from Game_Settings.World_Settings.world_settings_main import *
#
#
# the code below is getting/+ all of the world 1 files needed
from Game_Settings.Wrlds.World_1.wrld1_level_one import *
from Game_Settings.Wrlds.World_1.wrld1_level_two import *
from Game_Settings.Wrlds.World_1.wrld1_level_three import *
#
#
# the code below is getting all the code needed for world 2
from Game_Settings.Wrlds.World_2.wrld2_level_one import *
from Game_Settings.Wrlds.World_2.wrld2_level_two import *
from Game_Settings.Wrlds.World_2.wrld2_level_three import *
#
#
# The code below is getting all the world 3 files needed
from Game_Settings.Wrlds.World_3.wrld3_level_one import *
from Game_Settings.Wrlds.World_3.wrld3_level_two import *
from Game_Settings.Wrlds.World_3.wrld3_level_three import *
#
#
# the code below is importing the Regular enemies into the game
from Game_Files.reg_enemies.easy_enemy import *
from Game_Files.reg_enemies.medium_enemy import *
from Game_Files.reg_enemies.hard_enemy import *
#
#
# The code below imports all the world bosses
from Game_Files.bosses.wrld_one_boss import *
from Game_Files.bosses.wrld_two_boss import *
from Game_Files.bosses.wrld_three_boss import *
########################################################################################################
# This section is for the settings portion
########################################################################################################
########################################################################################################
# the code below is for initilazing each class
hero = user_class
hero.hp = user_health
hero.dmg = user_damage
#
easy_enemy = easy_enemy_class
easy_enemy.hp = easy_enemy_hp
easy_enemy.dmg = easy_enemy_dmg
#
medium_enemy = medium_enemy_class
medium_enemy.hp = medium_enemy_hp
medium_enemy.dmg = medium_enemy_dmg
#
hard_enemy = hard_enemy_class
hard_enemy.hp = hard_enemy_hp
hard_enemy.dmg = hard_enemy_dmg
#
# the code below is for the bosses classes
wrld_one_boss = wrld_one_boss_class
wrld_two_boss = wrld_two_boss_class
wrld_three_boss = wrld_three_boss_class
#
def main_settings():
    print('User Settings')
    print('back')
    main_settings_loop = True
    while main_settings_loop:
        main_settings_input = input('# ')
        if main_settings_input == 'user':
            user_settings()
        elif main_settings_input == 'back':
            main_menu()
        else:
            print('sorry not an option provided')

###################################################################################################
###################################################################################################
# This section is for the main loop
###################################################################################################
###################################################################################################
def main_menu():
    print('Start')
    print('Settings')
    print('Exit')
    # The code below makes a loop for the main menu
    menu_loop = True
    while menu_loop:
        menu_input = input('# ')
        if menu_input == 'start':
            world_one_lvl_one_start()
        elif menu_input == 'exit':
            quit()
        elif menu_input == 'settings':
            main_settings()
        else:
            print('Not an option provided')
    

def mainloop():
    main_menu()

mainloop()
###################################################################################################
###################################################################################################