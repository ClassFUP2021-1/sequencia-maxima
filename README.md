# sequencia-maxima
### Objetivo do algoritmo: Identificar sequência crescente de maior soma. 
Escreva um programa que leia um inteiro n >= 2 e uma sequência de n números inteiros e imprima um segmento crescente de dois elementos desta sequência, cuja a soma seja a máxima.

O algoritmo deverá receber um ou mais números inteiros, o primeiro será a quantidade de números na sequência e os seguintes serão o valor de cada número.

### Objetivos do exercicio:
- A partir do código base dentro de **exercicio.py**, você deverá validar o que já está escrito, realizando as modificações necessárias para a execução correta do algoritmo.
- Desenvolver a capacidade de detectar os casos de teste de um algoritmo

### Entrada
- Número inteiro X igual ou maior que 2.
- Números inteiros Yn (quantidade de números definida pelo valor da variável X). 

### Saída
- String contendo sequência crescente de maior soma, string "sem sequencia crescente" ou string "entrada invalida".

### Observações
**Obs1.:** Caso o algoritmo não encontre o segmento crescente de dois elementos consecutivos da sequência, cuja soma seja máxima, o algoritmo deve informar “sem sequencia crescente” e caso identifique alguma entrada inválida deve informar “entrada invalida”.

**Obs2.:** Não usar as funções mínimo e máximo.

### Exemplos
| Entrada | Saida |
| ------ | ------ |
| 12-1-15-2-4-7-20-19-26-3-14-40-25 | "14, 40" |
| 3-1-5-6 | "5, 6" |
| 0 | "entrada invalida" |
| 3-6-5-1 | "sem sequencia crescente" |

### Instruções gerais
- Escreva seu código dentro do arquivo **exercicio.py**
- Escreva os casos de teste do algoritmo dentro do arquivo **casosDeTeste.py**
- Dentro do arquivo **exercicio.py** existe um código que resolve parcialmente o problema. Vocé deverá validar o que está escrito, realizando as modificações necessárias para a execução correta do algoritmo.
- Dentro do arquivo **casosDeTeste.py** existe uma estrutura no formato: { "X-Y1-Y2": "saida" }, onde X, Y1 e Y2 são as entradas já descritas e devem ser separadas por hífen. Você deverá inserir seus casos de teste nele. Por exemplo, {"3-1-5-6" : "5, 6"} significa que as entradas serão **X = 3**, **Y1 = 1**, **Y2 = 5** e **Y3 = 6** e a saida será **"5, 6"**. Para inserir um novo caso de teste como, por exemplo,{"0" : "entrada invalida"}, basta inserir uma virgula e adicionar os novos dados, como no exemplo abaixo:
```sh
{"3-1-5-6" : "5, 6",
"0" : "entrada invalida"}
```
- Após a codificação do algoritmo não esqueça de **commitar as mudanças** clicando no botão commit **changes**.
- Dentro do arquivo **exercicio.py** existem duas variáveis: **n** e **sequencia** que representam **X** e **Yn** respectivamente. Ou seja, você deverá usa-las como entradas do seu algoritmo. Note, que esse algoritmo não recebe as entradas através do ``` input()``` e sim através de ``` sys.argv[1]``` e ``` sys.argv[i+2]```. Para a codificação do algoritmo na sua máquina, você poderá ``` input()``` normalmente, mas não se esqueça de altera-lo para ``` sys.argv[1]``` e ``` sys.argv[i+2]``` no momento de submeter seu código.
- Em hipótese alguma você deverá alterar o código do arquivo exercicio_test.py, caso seja detectada alguma alteração, sua resolução será desconsiderada.

