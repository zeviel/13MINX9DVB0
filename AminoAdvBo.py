import amino
from concurrent.futures import ThreadPoolExecutor
print(f"""\u001b[38;5;124m
Script by deluvsushi
Github : https://github.com/deluvsushi
╭━━━┳━╮╭━┳━━┳━╮╱╭┳━━━┳━━━┳━━━┳╮╱╱╭┳━━╮╭━━━╮
┃╭━╮┃┃╰╯┃┣┫┣┫┃╰╮┃┃╭━╮┃╭━╮┣╮╭╮┃╰╮╭╯┃╭╮┃┃╭━╮┃
┃┃╱┃┃╭╮╭╮┃┃┃┃╭╮╰╯┃┃╱┃┃┃╱┃┃┃┃┃┣╮┃┃╭┫╰╯╰┫┃╱┃┃
┃╰━╯┃┃┃┃┃┃┃┃┃┃╰╮┃┃┃╱┃┃╰━╯┃┃┃┃┃┃╰╯┃┃╭━╮┃┃╱┃┃
┃╭━╮┃┃┃┃┃┣┫┣┫┃╱┃┃┃╰━╯┃╭━╮┣╯╰╯┃╰╮╭╯┃╰━╯┃╰━╯┃
╰╯╱╰┻╯╰╯╰┻━━┻╯╱╰━┻━━━┻╯╱╰┻━━━╯╱╰╯╱╰━━━┻━━━╯
""")
client = amino.Client()


def main_process():
    email = input("-- Email::: ")
    password = input("-- Password::: ")
    client.login(email=email, password=password)
    clients = client.sub_clients(start=0, size=100)
    for x, name in enumerate(clients.name, 1):
        print(f"-- {x}:{name}")
    com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
    sub_client = amino.SubClient(comId=com_id, profile=client.profile)
    message = input("-- Message::: ")
    while True:
        for i in range(0, 2000, 15000):
            try:
                print("-- Sending advertise...")
                online_users = sub_client.get_online_users(start=i, size=100).profile.userId
                sub_client.start_chat(userId=online_users, message=message)
                with ThreadPoolExecutor(max_workers=100) as executor:
                    executor.submit(sub_client.start_chat,
                                    online_users, message)
            except amino.lib.util.exceptions.VerificationRequired as e:
                print(f"-- VerificationRequired::: {e.args[0]['url']}")
                verification = input("-- Press enter after verification!")
            except Exception as e:
                print(e)


main_process()
