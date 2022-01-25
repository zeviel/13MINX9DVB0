import amino
from pyfiglet import figlet_format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.DARK_ORANGE + style.BOLD}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminoadvbo", font="chunky"))
old = []
def advertise(data: str):
    users_list = []
    for user_id in data.profile.userId:
        users_list.append(user_Id)
    return users_list

client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")    
while True:
	try:
		print("-- Sending advertise...")
		online_users = advertise(sub_client.get_online_users(size=100))
		for user_id in old:
			if user_id in users:
				users.remove(user_id)
		sub_client.start_chat(userId=online_users, message=message)
		with ThreadPoolExecutor(max_workers=100) as executor:
			_ = [executor.submit(sub_client.start_chat, online_users, message) for user_id in users]
	except amino.lib.util.exceptions.VerificationRequired as e:
		print(f"-- VerificationRequired::: {e.args[0]['url']}")
		verification = input("-- Press enter after verification!")
	except Exception as e:
		print(e)
