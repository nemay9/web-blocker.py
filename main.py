import time
import os


hosts = r'C:\Windows\System32\drivers\etc\hosts'#win10 hosts path
redirect_url ='127.0.0.1'

blocked_urls = ['www.youtube.com','youtube.com']# list url to block

def block_url():
    try:
        with open(hosts,'r+') as file:
            src = file.read()

            for site in blocked_urls:
                if site in src:
                    pass
                else:
                    file.write(f'{redirect_url} {site}\n')
            print('Access closed!')
    except Exception as e:
        print(e)


def unlock_url():
    try:
        with open(hosts, 'r+') as file:
            src = file.readlines()
            file.seek(0)

            for line in src:
                if not any(site in line for site in blocked_urls):
                    file.write(line)
            file.truncate()
        print('Access done!')
    except Exception as e:
        print(e)


while True:
    com = input(f'block: {blocked_urls}\nY/N: ')
    if com == 'Y' or com == 'y':
        block_url()
    if com == 'N' or com == 'n':
        unlock_url()
