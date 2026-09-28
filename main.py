from central_recursiva.operacoes import mdc, soma_digitos
from central_recursiva.validacoes import validar_entrada
from central_recursiva.excecoes import (
    OperacaoInvalidaError,
    EntradaInvalidaError,
)


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