#!/usr/bin/env python3
import requests
import json
import pandas as pd
from itertools import groupby

def get_data():
    data = requests.get('https://ectf.ctfd.io/api/v1/challenges').json()['data']
    categories = set(x['category'] for x in data)
    structured = {c:[[data[i]['name'], data[i]['solves'], data[i]['value']] for i in range(len(data)) if data[i]['category']==c] for c in categories}
    return structured

def show_scoreboard(structured):
    m = lambda i: max(len(str(chal[i])) for cat in structured.values() for chal in cat)

    for cat, challs in sorted(structured.items())[:-4]:
        print(f'{cat}')
        for chall in challs:
            alert = (' <---- Lots of attacks' if chall[1]>1 else '')
            print(f'  --> | Name: {chall[0].ljust(m(0))} | Value: {str(chall[2]).ljust(m(2))} | Solves: {str(chall[1]).ljust(m(1))} |{alert}')
        print('-'*30)

if __name__ == '__main__':
    show_scoreboard(get_data())