import requests
from babel import numbers
from api_conf import API_KEY

currencies = ['RUB', 'USD', 'EUR', 'GBP', 'JPY']
try:
    url = f'https://prime.exchangerate-api.com/v5/{API_KEY}/latest/{currencies[0]}'
    data = requests.get(url).json()
    courses = {curr: data['conversion_rates'][curr] for curr in currencies}
except KeyError:
    print('Нет такой валюты')
except requests.ConnectionError:
    print('Нет подключения к интернету')


class Currency:
    def __init__(self, number, currency=None):
        self.number = number if type(number) in [float, int] else 0
        if currency is not None and currency not in currencies:
            raise Exception('Нет такой валюты')
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, (float, int)):
            return Currency(self.number + other, self.currency)
        elif isinstance(other, Currency):
            if other.currency is not None and self.currency is not None:
                return Currency(self.number+other.number*courses[self.currency]/courses[other.currency], self.currency)
            elif other.currency is None:
                return Currency(self.number+other.number, self.currency)
            elif self.currency is None:
                return Currency(self.number + other.number, other.currency)
        else:
            print('Сложение невозможно')

    def convert(self, new_currency):
        try:
            if self.currency is not None:
                self.number *= courses[new_currency]/courses[self.currency]
            self.currency = new_currency
            return self
        except KeyError:
            print('Нет такой валюты')

    def __str__(self):
        return numbers.format_currency(self.number, self.currency, locale='ru') if self.currency else str(self.number)

    def __repr__(self):
        return f'Currency({self.number}, {self.currency})'


# a = Currency(500)
# print(a)
# a.convert('RUB')
# print(a)
# a.convert('USD')
# print(a)
# a.convert('EUR')
# print(a)
# a.convert('EURee')
# print(a)
#
# print('-------------')
#
# b = Currency(1, 'USD')
# c = Currency(1, 'EUR')
# print(b+c)
# print(b)
#
# print('-------------')
# d = 5
# e = Currency(3, 'USD')
#
# print(e+d)
#
# print('-------------')
#
# f = Currency(4)
# e = Currency(3, 'USD')
# print(f+e)
# print(e+f)
