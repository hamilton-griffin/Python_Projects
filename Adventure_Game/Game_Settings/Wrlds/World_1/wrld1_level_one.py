# This is world 1 level 1
#
from main_init import *
from Game_Files.reg_enemies.easy_enemy import *
from Game_Files.reg_enemies.medium_enemy import *
from Game_Files.reg_enemies.hard_enemy import *
from Game_Settings.User_Settings.user_main import *
from Game_Files.bosses.wrld_one_boss import *
import time
#
#
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
#
#
lvl_one_options = ['attack', 'heal']
#
def world_one_lvl_one_start():
    lvl_one_loop = True
    while lvl_one_loop:
        print('Youre commands are (attack, heal)')
        print('Hello hero!')
        print('We need your help. The sokato Tower (oil company) has become corrupte and we need to take them down!')
        time.sleep(2)
        print('Oh look its a Grunt go kill him!')
        lvl_one_input = input('| ')
        if lvl_one_input not in lvl_one_options:
            print('not an option provided!')
        elif lvl_one_input == 'attack':
            print('Enemies HP: ' + easy_enemy.hp)
            easy_enemy.hp -= hero.dmg
            print('You hit the enemy but the enemy also hit you')
            print('Youre HP: ' + hero.hp)
            print('Enemy HP: ' + easy_enemy.hp)
            time.sleep(2)
        elif lvl_one_input == 'heal':
            if hero.hp >= 100:
                print('full health')
            else:
                hero.hp += 25
                print('hero health restored by 25 points')

