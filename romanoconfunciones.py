def romanos(N):

    Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    
    u= N % 10
    d=int(math.floor(N/10))%10
    c=int(math.floor(N/100))
    if (N == 1000):
        return("M")
    else:
        if(N>=100):
            return(Centena[c]+Decena[d]+Unidad[u])
        else:
            if(N>=10):
                return (Decena[d]+Unidad[u])
            else:
                return(Unidad[N])   
import math
N=int(input("Introduzca un numero entero del 1 al 1000:"))
while N<1 or N>1000:
    N=int(input("Introduzca un numero entero del 1 al 1000:"))
print("El número es:",romanos(N)) 