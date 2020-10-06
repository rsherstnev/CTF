#!/usr/bin/env python3

''' Generator of most popular Russian passwords with monthly changing password policy '''

from datetime import datetime

months = {
    1: 'zydfhm',
    2: 'atdhfkm',
    3: 'vfhn',
    4: 'fghtkm',
    5: 'vfq',
    6: 'b.ym',
    7: 'b.km',
    8: 'fduecn',
    9: 'ctynz,hm',
    10: 'jrnz,hm',
    11: 'yjz,hm',
    12: 'ltrf,hm'
}

now = datetime.now()
month = now.month
year = now.year

if month == 1:
    base = [months[12], months[1], months[2]]
elif month == 12:
    base = [months[11], months[12], months[1]]
else:
    base = [months[month - 1], months[month], months[month + 1]]

for element in base:
    for char in range(0, len(element)):
        password = element[:char] + element[char].upper() + element[char+1:]
        print(f'{password}{year}\n{year}{password}')
