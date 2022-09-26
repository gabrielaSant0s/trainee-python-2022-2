import os
import sys
import csv
import requests

class User:
    def __init__(self, username, email, website, lat):
        self.email = email
        self.username = username
        self.website = website
        self.lat = lat
        self.hemisphere = self.hemisphere()

    def hemisphere(self):
        float_lat = float(self.lat)
        if float_lat >= 0:
            self.hemisphere = "North"
        else:
            self.hemisphere = "South"
        return self.hemisphere
    
    def __str__(self): 
        return f'{self.email},{self.website},{self.hemisphere},{self.username}'

def get_user_from_api(username):
    print("req user foi chamado")
    response = requests.get(f'https://jsonplaceholder.typicode.com/users?username={username}')
    data = response.json()
    user_data = data[0]

    email = user_data["email"]
    website = user_data["website"]
    lat = user_data["address"]["geo"]["lat"]
    
    user = User(username, email, website, lat)

    return user

def get_user_from_csv(username): 
    try:
        with open('cache.csv', 'r', newline='') as f:
            csv_cache = csv.reader(f, delimiter=',')
            for line in csv_cache:
                if username in line:
                    email = line[0]
                    website = line[1]
                    hemisphere = line[2]
                    if hemisphere == "North":
                        lat = 1
                    else:
                        lat = -1
                    user = User(username, email, website, lat)
                    return user
    except:
        write_cache_to_csv(get_user_from_api(username))

def get_user(username):
    user_csv = get_user_from_csv(username)
    if user_csv == None:
        print('peguei da api')
        user_api = get_user_from_api(username)
        write_cache_to_api(user_api)
        return user_api
    else:
        print('peguei do csv')
        return user_csv

def write_cache_to_csv(user):
    with open('cache.csv', 'w', newline='') as f:
        f.write('mail,website,hemisferio,username'+'\n')
        print('arquivo não existia')
        f.write(str(user)+'\n')
    
def write_cache_to_api(user):
    with open('cache.csv', 'a', newline='') as f:
        f.write(str(user)+'\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        print(get_user(username))
    else:
        print("passe um username")
