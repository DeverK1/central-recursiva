class OperacaoInvalidaError(Exception):
    pass


class EntradaInvalidaError(Exception):
    pass


def mdc(a, b):
    if b == 0:
        return a

    return mdc(b, a % b)


def soma_digitos(numero):
    if numero < 10:
        return numero

    return numero % 10 + soma_digitos(numero // 10)


def validar_entrada(linha):
    partes = linha.split()

    if not partes:
        raise EntradaInvalidaError()

    operacao = partes[0]

    if operacao not in ("M", "S"):
        raise OperacaoInvalidaError()

    quantidade_esperada = 3 if operacao == "M" else 2

    if len(partes) != quantidade_esperada:
        raise EntradaInvalidaError()

    try:
        numeros = [int(valor) for valor in partes[1:]]
    except ValueError:
        raise EntradaInvalidaError() from None

    if operacao == "M":
        a, b = numeros

        if a <= 0 or b <= 0:
            raise EntradaInvalidaError()

    else:
        numero = numeros[0]

        if numero < 0:
            raise EntradaInvalidaError()

    return operacao, numeros


def main():
    quantidade = int(input())
    processadas = 0

    while processadas < quantidade:
        linha = input()

        try:
            operacao, numeros = validar_entrada(linha)

            if operacao == "M":
                resultado = mdc(numeros[0], numeros[1])
                print(f"MDC = {resultado}")
            else:
                resultado = soma_digitos(numeros[0])
                print(f"SOMA = {resultado}")

        except OperacaoInvalidaError:
            print("ERRO: OperacaoInvalida")

        except EntradaInvalidaError:
            print("ERRO: EntradaInvalida")

        finally:
            processadas += 1


if __name__ == "__main__":
    main()