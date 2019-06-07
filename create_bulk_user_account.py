# Mass generate user information, and write into a csv file for later use.

# Column name, number of user accounts, are user-defined.
# We are going to have some randomness in the generated user information.
# Google: python write cvs file
#   -> https://docs.python.org/zh-cn/3/library/csv.html
#   -> https://realpython.com/python-csv/
#   -> https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/

# @Author: Aaron Law
# @Last Update: 2019-06-07
# -----------------------------------------------------------------------------
### Variables that can be changed on demand
filename = 'useraccount.csv'
num_user = 1000
column_list = {
    # A dict representing AD field and column head pairs. 
    # Format: AD-field : Column-name (where Column-name exact match to variables in powershell)
        'First name' : 'FirstName',  
        'Last name' : 'LastName', 
        'E-mail' : 'EmailAddress', 
        'Display name' : 'DisplayName', 
        'Password' : 'Password',
        }
email_endin = '@corpdev.hkjc.com'
pwd_len = 8

# For generated randomness
name_prefix = 'AaUser'
firstname_list = ['John', 'Peter', 'Hello', 'Net', 'Aaron', 'David', 'Jade', 'Susan', 'Doom']
lastname_list = ['Wick', 'Law', 'World', 'Lam', 'Law', 'Chan']
# -----------------------------------------------------------------------------
import csv, random

### In memory
def create_column_head(column_list):
    '''Generate column head from a dict.
    A sample format of user information is:
    FirstName, LastName, DisplayName, EmailAddress, Password.
    '''
    # Column-head: get a list of columns from a dict => column heads
    columns =  column_list.values()
    return (list(columns)) #convert dict to list

def create_user_info(column_list, num_user):
    '''Column-data: generate user data => a 2-dimension list'''
    whole_list = [] # 2-dimension
    for i in range(num_user):
        series_number = generate_series_number(num_user)

        # Generate user data according to columns, and append it to a big list
        firstname = _get_random_item(firstname_list)
        lastname = _get_random_item(lastname_list) 
        password = _get_password(pwd_len)
        # email = _get_email(firstname, lastname, email_endin, series_number)
        # displayname = _get_displayname(firstname, lastname, series_number)
        
        firstname = f"{firstname}{series_number}"
        email = f"{firstname}.{lastname}-{series_number}{email_endin}"
        displayname = f"{firstname} {lastname} {series_number}"
        
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
    '''Get an item from a list in a random position.'''
    return list[random.randint(0, len(list)-1)]

# def _get_firstname(firstname_list) -> str:
#     return _get_random_item(firstname_list)

# def _get_lastname(lastname_list) -> str:
#     return _get_random_item(lastname_list)

def _get_password(pwd_len):
    return generate_password(pwd_len)

def generate_password(len):
    '''Generate a password in random in len.'''
    # Reference:
    # Google: python generate random password -> https://www.practicepython.org/solution/2014/06/06/16-password-generator-solutions.html
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = len
    p =  "".join(random.sample(s,passlen ))
    return p

def generate_series_number(last_num):
    # if random_mode:
    return random.randint(0, last_num)
    # else:
        # series_number += 1
        # return series_number

def make_table(column_head, user_info):
    whole_list = [] # 2-dimension
    whole_list.append(column_head)
    for row in user_info:
        whole_list.append(row)
    return whole_list

if __name__ == "__main__":
    column_head = create_column_head(column_list)
    user_info = create_user_info(column_list, num_user)
    # Combian column-head + column-data => a big list
    whole_list = make_table(column_head, user_info)
    write_csv(whole_list, filename)
    # print(list)
    # print(_get_random_item(firstname_list))
    # print(_get_firstname(firstname_list))
    # print(_get_password(18))
    print(f"{len(whole_list)} row has been written into {filename}.")
# TODO:
# RANDOM_MODE
# exception on file write