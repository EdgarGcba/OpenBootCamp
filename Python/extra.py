num = int(input('Ingrese un numero: '))
 
for divisor in [2, 3, 5, 7]:
    if num % divisor == 0:
        print(f'Elnumero {num} es divisible por {divisor}')
        