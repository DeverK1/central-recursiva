# Central Recursiva

Aplicação em Python desenvolvida para a TED 02 de Algoritmos e Programação Avançada, com o professor Jackson, na UniBalsas. O projeto aplica modularização, recursividade e tratamento de exceções personalizadas ao problema CentralRecursivaRobusta.

## Integrantes

- Luiz Fernando Carvalho da Costa
- Kawê Victor Lima De Oliveira
- Joacy Arruda de Assis Junior

## Funcionalidades

- `M A B`: calcula o máximo divisor comum (MDC) de dois inteiros positivos.
- `S N`: calcula a soma dos dígitos de um inteiro não negativo.
- Identifica operações desconhecidas e entradas inválidas.

## Organização dos arquivos

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Lê a quantidade de operações, coordena validações e cálculos e imprime os resultados. |
| `central_recursiva/__init__.py` | Identifica o pacote Python; pode permanecer vazio. |
| `central_recursiva/operacoes.py` | Implementa as funções recursivas `mdc` e `soma_digitos`. |
| `central_recursiva/validacoes.py` | Verifica a operação, a quantidade de argumentos, a conversão para inteiros e os sinais dos valores. |
| `central_recursiva/excecoes.py` | Define as duas exceções personalizadas. |
| `beecrowd/central_recursiva_robusta.py` | Reúne a mesma lógica em um único arquivo para submissão. |
| `README.md` | Documenta o projeto e sua execução. |

## Como executar

É necessário ter Python 3 instalado. Não são necessárias bibliotecas externas.

Abra o terminal na pasta principal `central-recursiva` e execute:

```bash
python main.py
```

Em ambientes que utilizam o comando `python3`, substitua `python` por `python3`.

Digite primeiro a quantidade de operações (`Q`, de 1 a 100). Depois, informe uma operação por linha. Pressione Enter após a última linha.

### Exemplo de entrada

```text
7
S 12345
M 72 30
M 17 19
S 0
M 0 25
S -50
X 10 20
```

### Saída esperada

```text
SOMA = 15
MDC = 6
MDC = 1
SOMA = 0
ERRO: EntradaInvalida
ERRO: EntradaInvalida
ERRO: OperacaoInvalida
```

No uso interativo, o terminal pode exibir as entradas digitadas intercaladas com os resultados.

Para executar a versão de submissão:

```bash
python beecrowd/central_recursiva_robusta.py
```

## Algoritmos recursivos

### MDC — algoritmo de Euclides

A função `mdc(a, b)` utiliza a propriedade `MDC(a, b) = MDC(b, a % b)`. A cada chamada, o segundo argumento é substituído pelo resto da divisão.

O caso-base ocorre quando `b == 0`: a função retorna `a`. Por exemplo, `mdc(48, 18)` chama `mdc(18, 12)`, depois `mdc(12, 6)` e finalmente `mdc(6, 0)`, retornando `6`.

O zero que surge durante a recursão é parte do algoritmo. Na entrada de uma operação `M`, os dois números devem ser positivos.

### Soma dos dígitos

A função `soma_digitos(numero)` obtém o último dígito com `numero % 10` e os dígitos restantes com `numero // 10`. Ela soma o último dígito ao resultado de uma chamada recursiva com os demais.

O caso-base ocorre quando `numero < 10`, retornando o próprio número. Isso também atende à entrada `0`. Por exemplo, para `2026`, a soma é `6 + 2 + 0 + 2 = 10`.

## Validações e exceções personalizadas

As duas classes herdam de `Exception` e são lançadas com `raise`:

- `OperacaoInvalidaError`: lançada quando a operação não é `M` nem `S`. Produz `ERRO: OperacaoInvalida`.
- `EntradaInvalidaError`: lançada para linha vazia, quantidade incorreta de argumentos, falha na conversão para inteiro ou valores com sinais não permitidos. Produz `ERRO: EntradaInvalida`.

A operação `M` rejeita zero e números negativos. A operação `S` rejeita números negativos e aceita zero. A versão aceita não rejeita inteiros por ultrapassarem os limites máximos numéricos listados no enunciado.

Uma falha de conversão com `int()` gera `ValueError`, que é capturada e convertida em `EntradaInvalidaError`. A primeira linha é lida considerando a garantia do enunciado de que `Q` é válido.

No fluxo principal, `try` envolve a validação e o cálculo; os blocos `except` imprimem a mensagem correspondente. O bloco `finally` incrementa o contador de operações processadas, tanto em caso de sucesso quanto em caso de erro. Assim, uma operação inválida também é contabilizada entre as `Q` linhas.

## Beecrowd

- Problema: [7923 — CentralRecursivaRobusta](https://judge.beecrowd.com/en/custom-problems/view/7923)
- Submissão aceita: **1618258**
- Resultado: **Accepted**
- Linguagem da submissão: **Python 3.11**

A versão modular é destinada à avaliação da organização do projeto. O arquivo em `beecrowd/` contém a versão independente enviada ao juiz.
