def primo(n):
    i = 2
    while i <= (n ** 1 / 2):
        if n % i == 0:
            return False
        i += 1
    return True


def mayor_factor(n):
    i = 2
    while n > 1:
        if n % i == 0:
            n /= i
        else:
            i += 1
    return i


def capicua(n):
    ni = n
    ni2 = n
    largo = 0
    while ni > 0:
        ni //= 10
        largo += 1
    inv = 0
    while largo > 0:
        a = n % 10
        largo -= 1
        inv += a * (10 ** (largo))
        n //= 10
    if ni2 == inv:
        return True
    else:
        return False


# de 3 digitos para el ejercico de capicua (responde a la pregunta: ¿es
# producto de 2 factores de 3 digitos?)
def factores(n):
    fac = n // 2
    while fac > 1:
        if n % fac == 0 and 100 < fac < 1000:
            fac2 = n // fac
            if 100 < fac2 < 1000:
                return True
        fac -= 1


def mayor_capicua():
    i = 998001  # mayor producto de dos numeros de 3 digitos (999*999=998001)
    while True:
        if capicua(i) and factores(i):
            return i
        i -= 1


def sumacuadrados(n):
    i = 0
    suma = 0
    while i <= n:
        suma += i ** 2
        i += 1
    return suma


def cuadradosuma(n):
    i = 0
    suma = 0
    while i <= n:
        suma += i
        i += 1
    return (suma ** 2)


def triopitagorico(n):  # ejercicio d
    i = 1
    while i < n:
        j = 1
        while j < n:
            k = n - j - i
            if i ** 2 + j ** 2 == k ** 2:
                return i * j * k
            j += 1
        i += 1


def f_alternante(n):
    i = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1
        i += 1
    return i


def operaciones(hasta):
    maxops = 0
    # se parte (hasta/2) porque cualquier numero bajo eso tiene su doble
    # dentro del rango y ese numero da 1 op mas, ejemplo con hasta=50: el
    # numero exluido 18 da x operaciones, pero 36 esta en el rango y al
    # dividirlo por 2 da 18, y entonces las ops de 36 son las de 18 + 1 op.
    n = hasta // 2
    while n < hasta:
        # se excluyen 1) los pares. 2) los numeros de la forma 3n-1. 3) los que
        # al realizarles 3n-1 terminen en 4 u 8 porque se pierden operaciones
        # ya que al tiro son divididos dos veces 8->4->2 en cambio 6->3.
        if (n % 2) != 0 and (((n + 1) / 3) % 1) != 0 and (((3 * n) - 1) % 10) != 8 and (((3 * n) - 1) % 10) != 4:
            ops = f_alternante(n)
            if ops > maxops:
                maxops = ops
                nmax = n
        n += 1
    return nmax


def diasmes(n, año):
    b = False
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        b = True
    if (n < 8 and n % 2 != 0) or (n > 7 and n % 2 == 0):
        dias = 31
    elif n == 2 and b:
        dias = 29
    elif n == 2 and not b:
        dias = 28
    else:
        dias = 30
    return dias


def domingos(hasta):
    i = 0
    y = 1901
    domingos = 1
    dia = 0
    while y <= hasta:
        i = 1
        while i < 13:
            dia += diasmes(i, y)
            if dia % 7 == 0:
                domingos += 1
            i += 1
        y += 1
    return domingos


def sumadigitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma


def factorial(n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i


def sumadigfactorial(n):
    return sumadigitos(factorial(n))


def largo(n):
    ni = n
    largo = 1
    while ni > 9:
        ni //= 10
        largo += 1
    return largo

# ver que esten todos los numeros del 1 al 9


def no1(n):
    while n > 0:
        if n % 10 == 1:
            return False
        n //= 10
    return True


def no2(n):
    while n > 0:
        if n % 10 == 2:
            return False
        n //= 10
    return True


def no3(n):
    while n > 0:
        if n % 10 == 3:
            return False
        n //= 10
    return True


def no4(n):
    while n > 0:
        if n % 10 == 4:
            return False
        n //= 10
    return True


def no5(n):
    while n > 0:
        if n % 10 == 5:
            return False
        n //= 10
    return True


def no6(n):
    while n > 0:
        if n % 10 == 6:
            return False
        n //= 10
    return True


def no6(n):
    while n > 0:
        if n % 10 == 6:
            return False
        n //= 10
    return True


def no7(n):
    while n > 0:
        if n % 10 == 7:
            return False
        n //= 10
    return True


def no8(n):
    while n > 0:
        if n % 10 == 8:
            return False
        n //= 10
    return True


def no9(n):
    while n > 0:
        if n % 10 == 9:
            return False
        n //= 10
    return True

# fin tontera apurado jajaj


def pand_9(n):
    sumaideal = 45
    i = 0
    while i < largo(n):
        if (n // (10 ** i)) % 10 > largo(n) or (n // (10 ** i)) % 10 == 0 or no1(n) or no2(n) or no3(n) or no4(n) or no5(n) or no6(n) or no7(n) or no8(n) or no9(n):
            return False
        i += 1
    if sumaideal == sumadigitos(n):
        return True
    return False


# suma ambos, ej: 186*39 y 39*186, si cambiamos a 50 estamos para la suma 1 vez
def sumapandigital():
    x = 4
    sumadigital = 0
    # x e y menores que 10000 pq si no serian mayores que 9 digitos los
    # productos 1*4
    while x < 10000:
        y = 0
        formado = 0
        while y < 10000 and largo(formado) < 10:
            formado = (
                x * (10 ** (largo(y) + largo(x * y))) + y * (10 ** (largo(x * y))) + (x * y))
            if pand_9(formado):
                sumadigital += formado
                #print (x,'*',y,'=',x*y,'=',formado)
            y += 1
        x += 1
    return sumadigital


def nopar(n):
    while n > 2:
        if n % 2 == 0:
            return False
        n //= 10
    return True


def nocinco(n):
    while n > 5:
        if n % 10 == 5:
            return False
        n //= 10
    return True


def rotar(n):
    n = n % 10 * (10 ** (largo(n) - 1)) + n // 10
    return n


def circulares():
    n = 2
    prod = 1
    # entre 40k y 50k si o si hay numeros pares (el 4) y no pueden ser
    # circulares, ya que al rotar el 4 va a quedar al final alguna vez y será
    # divisible
    while n < 40000:
        # entre 20k y 30k si o si hay numeros pares (no sirven)
        if 0 < n < 20000 or 31000 < n < 40000:
            n1 = rotar(n)
            n2 = rotar(n1)
            n3 = rotar(n2)
            n4 = rotar(n3)
            # dentro de los intervalos señalados, descartamos aquellos numeros
            # que sean pares o cincos a partir del 2 o 5 que si son primos
            if nopar(n) and nocinco(n):
                if primo(n) and primo(n1) and primo(n2) and primo(n3) and primo(n4):
                    prod *= n
        n += 1
    return prod
