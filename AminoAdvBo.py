import concurrent.futures
import amino
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.RED)
print(Style.NORMAL)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoadvbo", font="cricket"))
print("Advertise Bot Amino")
lz = []
def advertise(data):
    listusers = []
    for userId in data.profile.userId:
        listusers.append(userId)
    return listusers

client = amino.Client()    
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
msg = input("Message/Сообщение: ")
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
while True:
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        _ = [executor.submit(sub_client.start_chat, user, msg) for userId in user]
