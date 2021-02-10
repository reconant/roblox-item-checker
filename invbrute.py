import ctypes, requests
from threading import Thread

threadc = 250

done = 0
rap = 0
value = 0
limiteds = 0

def thread():
    global done, rap, value, limiteds
    while assetids:
        assetid = assetids.pop(0)
        try:
            r = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/items/asset/{assetid}').json()['data']
            if r:
                amount = len(r)
                print(f'{amount}x {r[0]["name"]}')
                limiteds += amount
                rap += rolimons[assetid][0] * amount
                value += rolimons[assetid][-1] * amount
            done += 1
        except Exception as e:
            print(e)
            assetids.append(assetid)

username = input('Username to search: ')
r = requests.get(f'https://www.roblox.com/user.aspx?username={username}').url
if 'www.roblox.com/users/' in r:
    userid = r.split('/')[-2]
else:
    input('Invalid/Banned user.')
    exit()

import re, json
rolimons = {}
r = requests.get(f'https://www.rolimons.com/itemtable').text
values = json.loads(re.search('var item_details = (.*);', r).group(1))
for assetid in values:
    rolimons[assetid] = (values[assetid][8], values[assetid][22])
assetids = list(rolimons.keys())
total = len(assetids)

for i in range(threadc):
    Thread(target=thread).start()

while 1:
    finished = done
    ctypes.windll.kernel32.SetConsoleTitleW(f'Inventory Bruteforcer | Limiteds checked: {finished}/{total}')
    if finished == total: break

ctypes.windll.kernel32.SetConsoleTitleW(f'Inventory Bruteforcer | Finished.')
print(
    f'RAP: {rap}\n'
    f'Value: {value}\n'
    f'Limiteds: {limiteds}'
)
input()