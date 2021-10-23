import aminofix, pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_ORANGE + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminoadvbo", font="chunky"))
default_list = [ ]
def advertise(data: str):
    users_list = [ ]
    for user_Id in data.profile.userId:
        users_list.append(user_Id)
    return users_list

client = aminofix.Client()
client.login(email=input("Email >> "), password=input("Password >> "))
message = input("Message >> ")
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_Id = clients.comId[int(input("Select the community >> "))-1]
sub_client = aminofix.SubClient(comId=com_Id, profile=client.profile)  
        
while True:
	try:
		print("Sending Advertise...")
		online_users = sub_client.get_online_users(size=100)
		users = advertise(online_users)
		for i in default_list:
			if i in users:
				users.remove(i)
		sub_client.start_chat(userId=users, message=message)
		with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
			_ = [executor.submit(sub_client.start_chat, users, message) for user_Id in users]
	except aminofix.lib.util.exceptions.VerificationRequired as e:
		print(f"VerificationRequired")
		link = e.args[0]['url']
		print(link)
		verify = input("Waiting for verification >> ")
	except Exception as e:
		print(e)
