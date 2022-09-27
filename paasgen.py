import os
import random
import string

settings = {
    'lower': True,
    'upper': True,
    'number': True,
    'symbol': True,
    'space': False,
    'length': 8
}

PASSWORD_MIN_LEN = 4
PASSWORD_MAX_LEN = 30

def clear_screen():
    
    os.system('cls')
    
def get_password_len(option, defualt, pw_min_len = PASSWORD_MIN_LEN
                     , pw_max_len = PASSWORD_MAX_LEN):
    while True:
        user_input = input(f'Enter your password. defualt is {defualt} :')
        
        if user_input == '':
            return defualt
        if user_input.isdigit():
            user_pass_len = int(user_input)
            
            if pw_min_len <= user_pass_len <= pw_max_len:
                return int(user_input)
            
            print(f"invalid input not between {pw_min_len} to {pw_max_len}.")
        else:    
            print("invalid number .please try again")
        
def yes_or_no(option, defualt):
    
    while True:
        user_input = input(f"Incloud {option} ?." 
                        f"(defualt is {defualt} )" 
                        "(y: yes and n: no and enetr: defualt):")
        if user_input == '':
            return defualt
        
        if user_input in ['y', 'n']:
            return user_input == 'y'
        
        print("invalid input.please try again.")
            
def get_settings_from_user(settings):
    
    for option, defualt in settings.items():
        if option != 'length':
            user_choise = yes_or_no(option, defualt)
            settings[option] = user_choise
        else:
            user_password_len = get_password_len(option, defualt)
            settings[option] = user_password_len
            
def ask_if_change_set(settings):
    
    while True:
        user_input = input("do you want to change the settings?" 
                        "(y : yes and n :no and enter :yes ) ")
        
        if user_input in ['y', 'n', '']:
            if user_input == 'n':
                return False 
            get_settings_from_user(settings)
            break
        else:
            print("invalid input . choose y or n or enter")
            print("please try again")
    
def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_numbers():
    return random.choice('0123456789')

def get_random_symbol():
    return random.choice('*&%$#@?><-?{[^=+!_')
        
def generate_random_char(choices):
    choice = random.choice(choices)
    
    if choice == 'upper':
        return get_random_upper_case()
    elif choice == 'lower':
        return get_random_lower_case()
    elif choice == 'symbol':
        return get_random_symbol()
    elif choice == 'number':
        return get_random_numbers()
    elif choice == 'space':
        return ' '
            
def password_generator(settings):
    
    final_password = ''
    password_len = settings['length']
    
    choices = list(filter(lambda x: settings[x] == True , ['lower', 'upper', 'number',
                                                      'symbol', 'space']))
    for i in range(password_len):
        final_password += generate_random_char(choices)
        
    return final_password

def ask_gen_pas():
    
    while True:
            want_another_password = input("Do you want another password?"
                                        "(y : yes and n : no and enter : yes")
            if want_another_password in ['y', 'n', '']:
                if want_another_password == 'n':
                    return False 
                return True
            else:
                print("invalid input . choose y or n or enter")
                print("please try again")
def password_generator_loop(settings):
      while True:
        
        print('-'*40)
        print(f"generated password: {password_generator(settings)}")
        
        if ask_gen_pas() == False:
            break
                                          
def run():
    clear_screen()
    ask_if_change_set(settings)
    password_generator_loop(settings)

run()    
        

