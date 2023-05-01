#!/usr/bin/python3
import argparse
import requests
import datetime
from bs4 import BeautifulSoup
from tabulate import tabulate

def excur_web_data_get(city):
    try:
        answer = requests.get('https://excur.ru/' + city)
    except:
        print('excur: request failed')
        raise

    return answer

def excur_parse(what, data):
    try:
        soup = BeautifulSoup(data.text, 'lxml')
    except:
        print('excur: parser init failed')
        raise

    for td in soup.find_all('td'):
        try:
            attr = td.attrs['title']
            if attr == what:
                try:
                    span = td.find('span')
                    return span.text
                except:
                    pass
        except:
            pass

    return '--'

def excur_usd_best_sell_parse(data):
    try:
        value = excur_parse('Выгодная продажа Доллара США', data)
        return value
    except:
        raise

def excur_usd_best_buy_parse(data):
    try:
        value = excur_parse('Выгодная покупка Доллара США', data)
        return value
    except:
        raise

def excur_eur_best_sell_parse(data):
    try:
        value = excur_parse('Выгодная продажа Евро', data)
        return value
    except:
        raise

def excur_eur_best_buy_parse(data):
    try:
        value = excur_parse('Выгодная покупка Евро', data)
        return value
    except:
        raise

def print_rates(args):
    try:
        data = excur_web_data_get(args.city)
    except:
        return

    now = datetime.datetime.now() 
    print(now.strftime("Date: %d.%m.%Y; Time: %H:%M"))
    rates = []
    rates.append(['USD', excur_usd_best_buy_parse(data), excur_usd_best_sell_parse(data)])
    rates.append(['EUR', excur_eur_best_buy_parse(data), excur_eur_best_sell_parse(data)])
    print(tabulate(rates, headers=['Сurrency', 'Buy', 'Sell']))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get exchange rates from https://excur.ru")
    parser.add_argument('-c', '--city', default='Novosibirsk')
    args = parser.parse_args()

    print_rates(args)
