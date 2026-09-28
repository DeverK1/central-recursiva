from .excecoes import OperacaoInvalidaError, EntradaInvalidaError


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