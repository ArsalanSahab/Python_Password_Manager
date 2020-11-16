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
    

def display_single_record(user_name, website_name) :
    
    cursor = conn.execute('''SELECT hex, user_name, password, website_name FROM my_passwords
                              
                                 WHERE user_name = ? AND website_name = ?''', (user_name, website_name))
        
    for row in cursor:
                print()
                print("Hex_Key = " + row[0])
                print("Username = " + row[1])
                print("Password = " + row[2])
                print("Website Name = " + row[3])
                
                
                
            
    
    

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
            print("Done!")
            display_commands_menu()
            
        except :
            
            print("Data Already Exists")
            display_commands_menu()
        
       
        
    elif int(choice) == 2 :
        
        cursor = conn.execute('''SELECT hex, user_name, password, website_name FROM my_passwords;''')
        counter = 0
        for row in cursor:
                counter = counter + 1
                print()
                print("ID = " + str(counter))
                print("Hex_Key = " + row[0])
                print("Username = " + row[1])
                print("Password = " + row[2])
                print("Website Name = " + row[3])
                print()
            
        display_commands_menu()
            
    elif int(choice) == 3 :
        
        user_name = input("Please Enter Username : ")
        website_name = input("Please Enter Website Name : ")
        new_pass = input("Enter New Password : ")
        
        print()
        print("-------------------- OLD DETAILS -------------------------")
        print()
        
        display_single_record(user_name, website_name)
        
        try :
            
            conn.execute(''' 
                         UPDATE my_passwords
                         SET password = ?
                         WHERE user_name = ? AND website_name = ?;
                         ''', (new_pass, user_name, website_name))
            conn.commit()
            
            print()
            print("------------------ NEW DETAILS -------------------------")
            print()
            
            display_single_record(user_name, website_name)
            display_commands_menu()
            
        except :
            
            print("No Record Found!")
            display_commands_menu()
            
       
            
            
        
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
 

    
    
    
    
    