from calc import math_oper as calc


while True:
    print("Dodawanie - 1")
    print("Odejmowanie - 2")
    print("Mnozenie - 3")
    print("Dzielenie - 4")
    print("wyjście - q")
    oper = input("wybierz dzialanie ")

    if oper in ('1', '2', '3', '4'):
        try:
            x = float(input("x="))
        except:
            print("To nie jest liczba, sprobuj ponownie")
            continue
        try:
            y = float(input("y="))
        except:
            print("To nie jest liczba, sprobuj ponownie")
            continue
        if oper == '1':
            print("wynik x+y=", calc.add(x, y))
        elif oper == '2':
            print("wynik x-y=", calc.sub(x, y))
        elif oper == '3':
            print("wynik x*y=", calc.mul(x, y))
        elif oper == '4' and y!=0:
            print("wynik x/y=", calc.div(x, y))
        elif oper == '4' and y==0:
            print("Niedozwolone dzielenie przez 0")
    if oper == 'q':
        break