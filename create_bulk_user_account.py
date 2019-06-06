# Generate a .csv file containing lots of user information.
# Column name, number of user accounts, are user-defined.
# We are going to have some randomness in the generated user info.
# Google: python write cvs file -> https://docs.python.org/zh-cn/3/library/csv.html
#-> https://realpython.com/python-csv/
#-> https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/

# @Author: Aaron Law
# @Last Update: 2019-06-06
import csv

filename = 'useraccount.csv'
num_user = 1000
column_list = []

def create_user_info(column_list, num_user):
    '''A sample format of user information is:
    First-name,Last-name, Displayname, EmailAddress
    '''
    # Made the 1st line as column head.
    # Made the following lines.
    pass

def write_csv(column_list, filename):
    '''Write lists as a csv file.
    '''
    # 開啟輸出的 CSV 檔案
    with open(filename, 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        # 寫入一列資料
        writer.writerow(['Name', 'Height', 'Weight'])

        # 寫入另外幾列資料
        writer.writerow(['Aa1', 175, 60])
        writer.writerow(['Aa2', 165, 57])

if __name__ == "__main__":
    create_user_info(column_list, num_user)
    write_csv(list, filename)
    # print(list)