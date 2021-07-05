import boto3
from pprint import pprint
from random import choice
import random
import csv
Iam_session=boto3.session.Session(profile_name="applicationDev")
Iam_conn=Iam_session.resource(service_name="iam")

class user_creation:
    def get_password(self):
        password_len=8
        password=''
        alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ\
             abcdefghijklmnopqrstuvwxyz\
             1234567890!@#$%^&*(){}[]<>')
        for cnt in range(password_len):
            password +=random.choice(alpha)
        
        return password
    def get_user(self):
        list_user=['ku239','LF593','KY690','KJ231','OX581']
        list_len=len(list_user)
        dict_userpass={}
        for cnt in range(list_len):
                username=list_user[cnt]
                password=self.get_password()
                dict_userpass[username]=password
                
                        
                Iam_conn.create_user(UserName=username)
                Iam_conn.meta.client.create_login_profile(UserName=username,Password=password,PasswordResetRequired=False)
                Iam_conn.meta.client.attach_user_policy(UserName=username,PolicyArn='arn:aws:iam::571857357844:policy/Mypolicy')
        return dict_userpass
    def create_user_csv(self,dict_userpassword):
        file=open('/Users/sumedh/users.csv', 'a', newline='')
        dict_len=len(dict_userpassword)
        writer = csv.writer(file)
        for each_user in Iam_conn.users.all():
            for each_key in dict_userpassword:
                if each_user.user_name==each_key:
                    print(each_user.user_id,each_user.user_name,each_user.create_date.strftime('%m-%d-%Y'),dict_userpassword[each_key])
                    writer.writerow([each_user.user_id,each_user.user_name,each_user.create_date.strftime('%m-%d-%Y'),dict_userpassword[each_key]])        


temp=user_creation()
dict_userpassword=temp.get_user()
temp.create_user_csv(dict_userpassword)