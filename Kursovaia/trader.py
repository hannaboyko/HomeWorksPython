'''
Валютний трейдер USD-UAH
Складність 4/4

Реалізувати функціонал обміну USD та UAH валют за допомогою CLI Python.

User Story:
Початкові умови (можна винести у config.json):
     курс: 36.00
     на гривневому рахунку: 10000.00 UAH
     на доларовому рахунку: 0.00 USD
     дельта: 0.5

Правила зміни курсу долара:
     випадковим чином у діапазоні:
     price - delta <new_price <price + delta (у прикладі від 35.50 до 36.50)

Всі розрахунки ведемо з точністю 2 знаки після коми!

Аргументи запуску файлу:
     RATE – отримання поточного курсу (USD/UAH)
     AVAILABLE - отримання залишків за рахунками
     BUY XXX - покупка xxx доларів. За відсутності гирвень для покупки виводить повідомлення типу UNAVAILABLE, REQUIRED BALANCE UAH 2593.00, AVAILABLE 1000.00
     SELL XXX - продаж доларів. У разі відсутності доларів для продажу виводить повідомлення типу UNAVAILABLE, REQUIRED BALANCE USD 200.00, AVAILABLE 135.00
     BUY ALL – купівля доларів на всі можливі гривні.
     SELL ALL - продаж всіх доларів.
     NEXT – отримати наступний курс
     RESTART - розпочати гру з початку (з початковими умовами)

Tech Requirements:
Мінімум три файли: 1) trader.py, 2) config.json 3) Стан системи (можна з історією дій) – свою назву
Стан системи (курс і доступний баланс кожної валюти) зчитується і зберігається у окремому файлі (формат файлу не розсуд розробника).
config.json
     Поля:
         "delta": 0.5
>>>python trader.py NEXT
>>>python trader.py RATE
26.27
>>>python trader.py NEXT
>>>python trader.py NEXT
>>>python trader.py NEXT
>>>python trader.py RATE
25.93
>>>python trader.py BUY 100
>>>python trader.py AVAILABLE
USD 100.0 UAH 7407.0
'''
import argparse
import json
import random


class Trader:
    def __init__(self, config):
        self.config = config
        with open("state.json", "r") as state_file:
            state = json.load(state_file)

        self.rate = state["initial_rate"]
        self.uah_balance = state["initial_uah_balance"]
        self.usd_balance = state["initial_usd_balance"]
        self.delta = state["delta"]
        self.history = state.get("history", [])

    def add_history(self, command, details=None):
        self.history.append({"command": command, "details": details})
        self.save_state()

    def save_state(self):
        state = {
            "initial_rate": self.rate,
            "initial_uah_balance": self.uah_balance,
            "initial_usd_balance": self.usd_balance,
            "delta": self.delta,
            "history": self.history
        }
        with open("state.json", "w") as state_file:
            json.dump(state, state_file)

    def next(self):
        self.rate = round(random.uniform(self.rate - self.delta, self.rate + self.delta), 2)
        self.add_history("NEXT", {"rate": self.rate})
        self.save_state()

    def get_rate(self):
        return self.rate

    def buy(self, amount):
        required_uah = round(amount * self.rate, 2)
        if required_uah > self.uah_balance:
            error = f"UNAVAILABLE, REQUIRED BALANCE UAH {required_uah:.2f}, AVAILABLE {self.uah_balance:.2f}"
            print(error)
            self.add_history("BUY", {"ERROR": error, "amount": amount, "rate": self.rate})
        else:
            self.uah_balance -= required_uah
            self.usd_balance += amount
            self.add_history("BUY", {"amount": amount, "rate": self.rate})
        self.save_state()

    def sell(self, amount):
        if amount > self.usd_balance:
            error = f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {self.usd_balance:.2f}"
            print(error)
            self.add_history("SELL", {"ERROR": error, "amount": amount, "rate": self.rate})
        else:
            self.uah_balance += round(amount * self.rate, 2)
            self.usd_balance -= amount
            self.add_history("SELL", {"amount": amount, "rate": self.rate})
        self.save_state()

    def buy_all(self):
        amount_usd = round(self.uah_balance / self.rate, 2)
        self.uah_balance = 0
        self.usd_balance += amount_usd
        self.add_history("BUY_ALL", {"amount": amount_usd, "rate": self.rate})
        self.save_state()

    def sell_all(self):
        self.uah_balance += round(self.usd_balance * self.rate, 2)
        self.usd_balance = 0
        self.add_history("SELL_ALL", {"amount": self.usd_balance, "rate": self.rate})
        self.save_state()

    def available(self):
        return f"USD {self.usd_balance:.2f} UAH {self.uah_balance:.2f}"

    def restart(self):
        self.rate = self.config["initial_rate"]
        self.uah_balance = self.config["initial_uah_balance"]
        self.usd_balance = self.config["initial_usd_balance"]
        self.history = []
        self.save_state()


def main():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    trader = Trader(config)

    parser = argparse.ArgumentParser(description="Currency trader CLI for USD-UAH")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("RATE")
    subparsers.add_parser("AVAILABLE")
    buy_parser = subparsers.add_parser("BUY")
    buy_parser.add_argument("amount", type=float, help="Amount of USD to buy")

    sell_parser = subparsers.add_parser("SELL")
    sell_parser.add_argument("amount", type=float, help="Amount of USD to sell")

    subparsers.add_parser("BUY_ALL")
    subparsers.add_parser("SELL_ALL")
    subparsers.add_parser("NEXT")
    subparsers.add_parser("RESTART")

    args = parser.parse_args()
    if args.command == "RATE":
        print(trader.get_rate())
    elif args.command == "AVAILABLE":
        print(trader.available())
    elif args.command == "BUY":
        trader.buy(args.amount)
    elif args.command == "SELL":
        trader.sell(args.amount)
    elif args.command == "BUY_ALL":
        trader.buy_all()
    elif args.command == "SELL_ALL":
        trader.sell_all()
    elif args.command == "NEXT":
        trader.next()
    elif args.command == "RESTART":
        trader.restart()


if __name__ == "__main__":
    main()
