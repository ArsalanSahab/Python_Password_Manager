########## LIBRARIES ############

import sqlite3
import hashlib
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
        
        conn.execute(''' CREATE TABLE IF NOT EXISTS my_passwords (
	hex TEXT PRIMARY KEY,
	user_name VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	website_name TEXT VARCHAR(255) UNIQUE
);''')
       
            
    except :
        
         print("Done !")
         
         
def generate_hex_key(password) :
    
   return hashlib.md5(password.encode()).hexdigest()    
        

def commands_exec() :
    
    choice = input(("Enter your choice : "))
    
    if int(choice) == 1 :
        user_name = input("Enter Username : ")
        password = input("Enter Password : ")
        website_name = input("Enter website name : ")
        pass_hex = str(generate_hex_key(password))
        
        print("Confirmation your values are : user_name : {} password : {} website : {} ".format(user_name, password, website_name))
        
        try :
            
            conn.execute('''INSERT INTO my_passwords VALUES(?, ?, ?, ?)''', (pass_hex, user_name, password, website_name))
            conn.commit()
            
        except :
            
            cursor = conn.execute("SELECT user_name, password from my_passwords")
            for row in cursor:
                print("Name = " + row[0])
                print("Pass = " + row[1])
            
        
       
        
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
 

    
    
    
    
    