from colorama import init, Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.RED)
print(Style.NORMAL)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ ▄▀▄ █▀▄ ▐▌░▐▌ █▀▄ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█ █▀█ █░█ ░▀▄▀░ █▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀░▀ ▀▀░ ░░▀░░ ▀▀░ ░▀░")
print("Advertise Bot Amino")
lz = []
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import amino
def advertise(data):
    listusers = []
    for userId in data.profile.userId:
        listusers.append(userId)
    return listusers
    
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
msg = input("Message/Сообщение: ")
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
users = sub_client.get_online_users(size=1000)
user = advertise(users)
for i in lz:
        if i in user:
            user.remove(i)
     
        
print("Sending Advertise")
for _ in range(4000):
    with concurrent.futures.ThreadPoolExecutor(max_workers=40000) as executor:
        _ = [executor.submit(sub_client.start_chat, user, msg) for userId in user]

print("Sending Advertise 2")
for _ in range(4000):
    with concurrent.futures.ThreadPoolExecutor(max_workers=40000) as executor:
        _ = [executor.submit(sub_client.start_chat, user, msg) for userId in user]
