import time
import re

class CustList(list["Customer"]):

    def cred_verify(self, cid, pin):
        for cus in self:
            if cid == cus.cid:
                if pin == cus.get_pin():
                    return True
                else:
                    return False

    def check_balance(self,cid):
        for cus in self:
            if cid == cus.cid:
                return cus.get_balance()

    def incr_balance(self,cid,amount):
        for cus in self:
            if cid in cus.cid:
                cus.set_balance(amount)
                return cus.get_balance()

    def decr_balance(self,cid,amount):
        for cus in self:
            if cid in cus.cid:
                cus.set_balance(-amount)
                return cus.get_balance()

class Customer:
    bank_customers = CustList()

    def __init__(self, data):
        self.cid = data[0]
        self.__pin = data[1]
        self.__balance = int(data[2])
        Customer.bank_customers.append(self)

    def get_pin(self):
        return self.__pin

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance += amount

with open("cust_data.txt", "r") as f:
    customers = f.readlines()
    for row in customers:
        cust_data = re.split(',', row.strip(), 3)
        c = Customer(cust_data)

def enter_cred():
    card_id = input("podaj id karty: ")
    pin = input("podaj pin: ")
    return card_id, pin

while True:
    print("wyplata gotowki - 1")
    print("wplata gotowki - 2")
    print("stan konta - 3")
    print("wyjście - q")
    oper = input("wybierz operacje ")
    if oper == '1':
        cred = enter_cred()
        if Customer.bank_customers.cred_verify(cred[0], cred[1]):
            print("autoryzacja OK")
            amount = input("wpisz kwote do wyplaty ")
            if Customer.bank_customers.check_balance(cred[0]) > int(amount):
                print("aktualny stan konta: ", Customer.bank_customers.decr_balance(cred[0], int(amount)))
            else:
                print("za malo srodkow na koncie")
        else:
            print("autoryzacja NOK")
            continue
    if oper == '2':
        cred = enter_cred()
        if Customer.bank_customers.cred_verify(cred[0], cred[1]):
            print("autoryzacja OK")
            amount = input("wpisz kwote wplaty ")
            print("wloz gotowke do bankomatu")
            time.sleep(5)
            print("aktualny stan konta: ", Customer.bank_customers.incr_balance(cred[0], int(amount)))
        else:
            print("autoryzacja NOK")
            continue
    if oper == '3':
        cred = enter_cred()
        if Customer.bank_customers.cred_verify(cred[0], cred[1]):
            print("autoryzacja OK")
            print("aktualny stan konta: ", Customer.bank_customers.check_balance(cred[0]))
        else:
            print("autoryzacja NOK")
            continue
    if oper == 'q':
        break
