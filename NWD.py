x = 126
y = 15
wynik = 1
if( x >= y):
    wynik = y
else:
    wynik = x
while(True):
    if( x % wynik == 0 and y % wynik ==0):
        break
    else:
        wynik = wynik -1
print(wynik)