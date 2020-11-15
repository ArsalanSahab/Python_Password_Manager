########## LIBRARIES ############

import sqlite3
from hashlib import sha256 as cypher
import secrets




def admin_login() :
    
    admin_login = input("Enter Admin Password : ")
    
    if admin_login != secrets.ADMIN_PASSWORD:
        print('Sorry Wrong Password!')
        exit()
    else :
        display_main_menu()
    


def display_main_menu() :
    
    
    print("__________________________________________")
    print("Welcome to the Password Manager Interface")
    print("__________________________________________")
    print()
    print("Initialising Database .......")
    init_connection()
    print()
    display_commands_menu()
   
    
    
def display_commands_menu() :
    
    
    print("__________________________________________")
    print("________________ Menu ____________________ ")
    print("1. Create new password")
    print("2. show all records")
    print("3. update password")
    print("4. delete password")
    print("5. quit")
    print()
    
    commands_exec()
    
   
    

def init_connection():
    
   
    
    try : 
        
        conn.execute('''CREATE TABLE my_passwords (hex TEXT PRIMARY KEY NOT NULL, user_name VARCHAR(255) NOT NULL, website_name VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL);''')
        
    except :
        
         print("Done !")
         
         
def generate_hex_key(password) :
    
    return cypher(password.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()
    
        

def commands_exec() :
    
    choice = input(("Enter your choice : "))
    
    if int(choice) == 1 :
        user_name = input("Enter Username : ")
        password = input("Enter Password : ")
        website_name = input("Enter website name : ")
        pass_hex = generate_hex_key(password)
        
        print("Confirmation your values are : user_name : {} password : {} website : {} ".format(user_name, password, website_name))
        
        conn.execute('''INSERT INTO my_passwords VALUES({pass_hex},{user_name}, {password}, {website_name})'''.format(pass_hex=pass_hex, user_name=user_name, password=password, website_name=website_name))
        conn.execute('''commit;''')
        
    elif int(choice) == 2 :
        conn.execute('''SELECT * FROM my_passwords;''')
    elif int(choice) == 3 :
        pass
    elif int(choice) == 4 :
        pass
    elif int(choice) == 5 :
        exit()
    else :
        print('Wrong Choice !')
        display_commands_menu()
        

    
    
    
    






if __name__ == "__main__" :
    
    conn = sqlite3.connect('passwords.db')
    admin_login()
 

    
    
    
    
    