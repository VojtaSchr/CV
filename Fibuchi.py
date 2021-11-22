def fib(n):
    if (n>1): #Podminka ukonceni rekurze
        return fib(n-1)+fib(n-2)
    else:
        return 1; #Nerekurzivni doreseni

f=fib(35)
print(f)