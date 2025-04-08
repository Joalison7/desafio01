h1 = int(input(f"qual sua hora: "))
m1 = int(input(f"qual seus minutos: "))
h2 = int(input(f"qual sua hora: "))
m2 = int(input(f"qual seus minutos: "))

s1 = m1 + m2
s2 = h1 + h2

if s1 >= 60:

    s2 = s2+1
    s1= s1-60

if s2 > 12:

    calculo = s2 - 12

print(f"{calculo}:{s1}")