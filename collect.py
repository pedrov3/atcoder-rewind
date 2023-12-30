import re
from datetime import datetime
import requests
import json

#user_tag = ['user-brown', 'user-yellow', 'user-red', 'user-cyan', 'user-gray', 'user-orange', 'user-blue', 'user-nav', 'user-green']

# Devolve uma lista com todos os usuários brasileiros
def get_users():
    with open("data.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    pattern = r'<a href="/users/(\w+)" class="username">'
    matches = re.findall(pattern, html_content)
    return matches

# Devolve submissions de um usuario a partir de um timestamp
# Obs: Api limita em 500
def getSubmission(user, timestamp):
    #api_url = api_path + userID
    api_url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={user}&from_second={timestamp}"
    response = requests.get(api_url)
    jsonData = response.json()
    return jsonData



# Devolve todas as submissões de um usuario
def getAllSubmissions(sample_user):
    #sample_user = "pedrolino"
    data = datetime(2023, 1, 1)
    timestamp = int(data.timestamp())
    
    retval = []
    data = getSubmission(sample_user, timestamp)
    while (len(data) == 500):
        retval += data
        data = sorted(data, key=lambda x: x['epoch_second'])
        timestamp = data[-1]["epoch_second"]
        data = getSubmission(sample_user, timestamp)
    retval += data
    data = [dict(t) for t in set([tuple(d.items()) for d in retval])]

    return data

# Estatísticas baseadas na quantidade de AC's de um usuário para problemas em uma faixa de valores
def userAcCount(username):
    submissions = getAllSubmissions(username)

    stats = [set() for i in range(0, 6)]

    for sub in submissions:
        if sub["result"] != "AC":
            continue
        id = 0
        pts = sub["point"]
        if pts <= 100:
            id = 0    
        elif pts <= 200:
            id = 1
        elif pts <= 300:
            id = 2
        elif pts <= 400:
            id = 3
        elif pts <= 500:
            id = 4
        else:
            id = 5

        stats[id].add(sub["problem_id"])
    return stats


users = get_users()
cnt = 0;
stats = []

for user in users:
    print(len(users) - cnt) # Controlar o andamento
    info = userAcCount(user)
    total = 0
    for i in info:
        total += len(i)

    stats.append({'user_id' : user, 'ac' : total, '100' : len(info[0]), '200' : len(info[1]), '300' : len(info[2]), '400' : len(info[3]), '500' : len(info[4]), '+' : len(info[5])})
    #if (cnt == 4):
    #    break
    cnt += 1

sorted_data = sorted(stats, key=lambda x: x['ac'], reverse=True)

print(f"username, total, <= 100, <= 200, <= 300, <= 400, <= 500, > 500")
for user in sorted_data:
    print(f"{user['user_id']} - {user['ac'] } - {user['100']} - {user['200']} - {user['300']} - {user['400']} - {user['500']} - {user['+']}")
