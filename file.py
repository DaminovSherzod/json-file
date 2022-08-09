import requests
import json
from pprint import pprint


def get_user(data):
    user = dict()

    user['Firstname'] = data['name']['first']
    user['lastname'] = data['name']['last']
    user['age'] = data['dob']['age']
    user['country'] = data['location']['country']

    return user


users = list()

while True:
    r = requests.get('https://randomuser.me/api/')
    
    if r.status_code == 200:
        data = r.json()['results'][0]
        
        if data['gender'] == 'male':
            user = get_user(data)
            users.append(user)

    if len(users) > 9:
        break
users_data = {
    'results': users
}

data_json = json.dumps(users_data, indent=4)
            
f = open('data.json', 'w')
f.write(data_json)
f.close()