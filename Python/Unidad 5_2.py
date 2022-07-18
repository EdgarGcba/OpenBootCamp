def esPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            print("El numero ", str(num),"No es primo", n, "es divisor")
            return False
    print("El numero ", str(num), " Es primo")
    return True

esPrimo(15)
esPrimo(17)