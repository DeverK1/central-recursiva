def mdc(a, b):
    if b == 0:
        return a

    return mdc(b, a % b)

def soma_digitos(numero):
    if numero < 10:
        return numero

    return numero % 10 + soma_digitos(numero // 10)