def calcular_mcd(n, m):
    if m == 0:
        return n
    return calcular_mcd(m, n % m)


def repetir_palabra(texto, n):
    if n == 0:
        return ""
    return texto + " " + repetir_palabra(texto, n - 1)


def contar_letras(texto, letra):
    if not texto:
        return 0
    return (texto[0] == letra) + contar_letras(texto[1:], letra)


def decimal_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_binario(n%2)+decimal_binario(n//2)
def invertir (texto):
    if texto=="":
        return ""
    else:
        return invertir(texto[1:])+texto[0]

def contar_digitos(n):
    if 0 <= n <= 9:
        return 1
    return 1 + contar_digitos(n // 10)


def menu():
    while True:
        print("\n__Menu__")
        print("1. Calcular MCD")
        print("2. Repetir una palabra")
        print("3. Cuantas veces aparece la letra?")
        print("4. Convertir numero decimal a binario")
        print("5. Cuantos digitos tiene un numero?")
        print("6. Salir")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            n = int(input("Ingrese un numero: "))
            m = int(input("Ingrese otro numero: "))
            print(f"El MCD es: {calcular_mcd(n, m)}")
        elif opcion == 2:
            texto = input("Ingresa una palabra: ")
            n = int(input("Cuantas veces desea repetir la palabra?: "))
            print(repetir_palabra(texto, n))
        elif opcion == 3:
            palabra = input("Ingresa una palabra: ")
            letra = input("Ingresa una letra: ")
            print(f"La letra aparece: {contar_letras(palabra, letra)} veces en la palabra")
        elif opcion == 4:
            n = int(input("Ingresa un numero: "))
            binario=str(decimal_binario(n))
            invertido=invertir(binario)
            print(f"Binario: {invertido)}")
        elif opcion == 5:
            n = int(input("Ingresa un numero: "))
            print(f"El numero tiene {contar_digitos(n)} digitos")
        elif opcion == 6:
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion invalida")


menu()



