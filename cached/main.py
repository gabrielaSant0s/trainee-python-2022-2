from asyncore import write
import os
import sys
import csv
import requests

class User:
    def __init__(self, username):
        self.email = ""
        self.username = username
        self.website = ""
        self.lat = ""
        self.hemisphere = ""
    
    def req_user(self):
        users = requests.get(f'https://jsonplaceholder.typicode.com/users')
        data = users.json()
        for user in data:
            if user["username"] == self.username:
                self.email = user["email"]
                self.website = user["website"]
                self.lat = user["address"]["geo"]["lat"]
    
    def discovery_hemisphere(self):
        self.req_user()
        float_lat = float(self.lat)
        if float_lat >= 0:
            self.hemisphere = "North"
        else:
            self.hemisphere = "South"
        return self.hemisphere
 
    def __repr__(self):
        self.discovery_hemisphere()
        return f'{self.email},{self.website},{self.hemisphere},{self.username}'


def cached_users(username):
    aux = 0 
    try:
        with open('cache.csv', 'r', newline='') as f:
            csv_cache = csv.reader(f, delimiter=',')
            for line in csv_cache:
                if username in line:
                    aux = 1
                    return print(f'{line[0]},{line[1]},{line[2]},{line[3]}')
        if aux == 0:
            with open('cache.csv', 'a', newline='') as f:
                user = User(username)
                f.write(str(user)+'\n')
                return print(user)
    except:
        with open('cache.csv', 'w', newline='') as f:
            f.write('mail,website,hemisferio,username'+'\n')
            print('arquivo não existia')
            user = User(username)
            f.write(str(user)+'\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        cached_users(username)
    else:
        print("passe um username")
