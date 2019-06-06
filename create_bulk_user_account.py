# Mass generate user information, and write into a csv file for later use.

# Column name, number of user accounts, are user-defined.
# We are going to have some randomness in the generated user information.
# Google: python write cvs file -> https://docs.python.org/zh-cn/3/library/csv.html
#-> https://realpython.com/python-csv/
#-> https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/

# @Author: Aaron Law
# @Last Update: 2019-06-06

### Variables that can be changed on demand
filename = 'useraccount.csv'
num_user = 1000
column_list = { # A dict representing AD field and column head pairs. 
                # Format: AD-field : Column-name (where Column-name exact match to powershell's variables)
    'First-name' : 'fn',  
    'Last-name' : 'ln', 
    'email' : 'email', 
    'displayname' : 'Displayname', 
    'password' : 'pwd',
    }

# For generated randomness
name_prefix = 'Aauser'
firstname_list = ['John', 'Peter', 'Hello', 'Net', 'Aaron', 'David', 'Jade', 'Susan', 'Doom']
lastname_list = ['Wick', 'Law', 'World', 'Lam', 'Law', 'Chan']
pwd_len = 18
email_endin = '@devcorp.hkjc.com'

import csv, random

### In memory
def create_user_info(column_list, num_user):
    '''A sample format of user information is:
    First-name,Last-name, Displayname, EmailAddress
    '''
    # Combian column-head + column-data => a big list
    whole_list = [] # 2-dimension

    # Column-head: get a list of columns from a dict => column heads
    columns = _get_columns(column_list)
    
    # Combian column-head + column-data => a big list
    whole_list.append(columns)

    # Column-data: generate user data => a 2-dimension list
    for i in range(num_user):
        # Generate user data according to columns, and append it to a big list
        firstname = _get_firstname(firstname_list) 
        lastname = _get_lastname(lastname_list) 
        password = _get_password(pwd_len)
        email = _get_email(firstname, lastname, email_endin, num_user)
        displayname = _get_displayname(firstname, lastname, num_user)
        
        whole_list.append([firstname,
                    lastname,
                    email,
                    displayname,
                    password,
        ])
    return whole_list

### On disk
def write_csv(list, filename):
    # Open an output csv file
    with open(filename, 'w', newline='') as csvfile:
        # Create a csv writer object for writting in
        writer = csv.writer(csvfile)
        # Write in the first row as column header
        #     (writer.writerow(['Name', 'height', 'Weight'])
        #     writer.writerow(['AB', 165, 57]))
        # Write to csv file row by row
        writer.writerows(list)

### Private functions
def _get_random_item(list) -> str:
    '''Get an item of a list from a random position.'''
    return list[random.randint(0, len(list)-1)]

def _get_firstname(firstname_list) -> str:
    return _get_random_item(firstname_list)

def _get_lastname(lastname_list) -> str:
####    if RANDOM_MODE:
    return _get_random_item(lastname_list)

def _get_password(pwd_len):
    return generate_password(pwd_len)

def _get_email(firstname, lastname, email_endin, last_digit):
    series = random.randint(0, last_digit)
    return f"{firstname}.{lastname}-{series}{email_endin}"

def _get_displayname(firstname, lastname, last_digit):
    series = random.randint(0, last_digit)
    return f"{firstname}.{lastname}-{series}"
    

def generate_password(len):
# Reference:
# Google: python generate random password -> https://www.practicepython.org/solution/2014/06/06/16-password-generator-solutions.html
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = len
    p =  "".join(random.sample(s,passlen ))
    return p

def _get_columns(column_list):
    columns =  column_list.values()
    return (list(columns)) #convert dict to list

if __name__ == "__main__":
    list = create_user_info(column_list, num_user)
    write_csv(list, filename)
    # print(list)
    # print(_get_random_item(firstname_list))
    # print(_get_firstname(firstname_list))
    # print(_get_password(18))
