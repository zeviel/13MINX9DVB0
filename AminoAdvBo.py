import amino
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_ORANGE + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoadvbo", font="chunky"))
lz = []
def advertise(data):
    listusers = []
    for userId in data.profile.userId:
        listusers.append(userId)
    return listusers

client = amino.Client()    
email = input("Email >> ")
password = input("Password >> ")
msg = input("Message >> ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community >> "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)

     
        
print("Sending Advertise")
while True:
	try:
		users = sub_client.get_online_users(size=1000)
		theusers = advertise(users)
		for i in lz:
			if i in theusers:
				theusers.remove(i)
		sub_client.start_chat(userId=theusers, message=msg)
		with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
			_ = [executor.submit(sub_client.start_chat, theusers, msg) for userId in theusers]
	except amino.lib.util.exceptions.VerificationRequired as e:
		print(f"VerificationRequired")
		link = e.args[0]['url']
		print(link)
		verify = input("Waiting for verification >> ")
	except Exception as e:
		print(e)
