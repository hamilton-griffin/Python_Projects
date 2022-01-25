from main_init import main_settings, main_menu
# tjis section is for the user stats
user_health = 100
user_damage = 20
#
user_settings_options = ['hp', 'damage', 'back']
#

def user_settings():
    global user_health
    global user_damage
    print('health ' + str(user_health))
    print('Damage ' + str(user_damage))
    print('back')
    user_settings_loop = True
    while user_settings_loop:
        user_settings_input = input('# ')
        if user_settings_input not in user_settings_options:
            print('not an option not found')
        else:
            if user_settings_input == 'hp':
                change_user_hp = input('HP: ')
                user_health = int(change_user_hp)
                print('HP: ' + user_health)
            elif user_settings_input == 'damage':
                change_user_damage = input('Damage: ')
                user_damage = int(change_user_damage)
                print('Damage: ' + str(user_damage))
            elif user_settings_input == 'back':
                print('#')
                main_settings()
#
class user_class:
    def __init__(self, hp, dmg):
        self.hp = user_health
        self.dmg = user_damage