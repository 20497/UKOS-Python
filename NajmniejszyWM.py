
x = 13
y = 26
wynik = 2
while(True):
    if(x % wynik == 0 and y % wynik == 0):
        break
    else:
        wynik = wynik + 1
print(wynik)