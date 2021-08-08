import amino
import asyncio
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_ORANGE + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("AminoAdvBo", font="jazmine"))
lz = []
def advertise(data):
    listusers = []
    for userId in data.profile.userId:
        listusers.append(userId)
    return listusers

async def main():
	client = amino.Client()    
	email = input("Email >> ")
	password = input("Password >> ")
	msg = input("Message >> ")
	await client.login(email=email, password=password)
	clients = await client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	print("Sending Advertise")
	while True:
		try:
			users = await sub_client.get_online_users(size=100)
			theusers = advertise(users)
			for i in lz:
				if i in theusers:
					theusers.remove(i)
			await sub_client.start_chat(userId=theusers, message=msg)
			await asyncio.gather(*[asyncio.create_task(sub_client.start_chat(theusers, msg)) for _ in range(45)])
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"VerificationRequired")
			link = e.args[0]['url']
			print(link)
			verify = input("Waiting for verification >> ")
		except Exception as e:
			print(e)
			
asyncio.get_event_loop().run_until_complete(main())
