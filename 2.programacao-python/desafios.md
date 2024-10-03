# desafios

Abaixo há uma lista de exercícios que são um pouco mais complexos que os exercícios propostos com o material. Sinta-se livre para realizá-los da melhor forma que achar (sempre usando **APENAS** o material de aula).


## árvore feliz

Faça um programa que peça um número ao usuário e monte um pinheiro como o mostrado abaixo. Se altura for menor que 3, o tronco terá apenas um de altura, senão será dois.
```
     #
    ###
   #####
  #######
 #########
###########
     #
     #
```
Exemplo de um pinheiro com altura 6.

## lanchonete

O cardápio de uma lanchonete é o seguinte :

```
Especificação......Código....Preço
Cachorro Quente.....100.....R$ 1,20
Bauru Simples.......101.....R$ 1,30
Bauru com ovo.......102.....R$ 1,50
Hambúrguer..........103.....R$ 1,20
Cheeseburguer.......104.....R$ 1,30
Refrigerante........105.....R$ 1,00
```

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

## votação

Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação da sua escolha. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir :
- O total de votos computados;
- Os númeos e respectivos votos de todos os jogadores que receberam votos;
- O percentual de votos de cada um destes jogadores;
- O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de listas. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

```
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador....Votos........%
...09........4......50,0%
...10........3......37,5%
...11........1......12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
```

## tamanho strings

Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

```
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
```

## gerador leetspeak

Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

## sequência de fibonacci

A sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores. A sequência começa com os números 0 e 1, e então cada número subsequente é gerado somando-se os dois números anteriores. Os primeiros termos da sequência de Fibonacci são :

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Observe que :
- O terceiro número (1) é a soma dos dois primeiros (0 + 1).
- O quarto número (2) é a soma do segundo e do terceiro (1 + 1).
- O quinto número (3) é a soma do terceiro e do quarto (1 + 2).

Para calcular a sequência de Fibonacci, é preciso seguir estas etapas :

1. **definir os dois primeiros números** da sequência como 0 e 1;
1. **calcular o próximo número** como a soma dos dois números anteriores;
1. **repetir o processo** até que a quantidade desejada de números na sequência seja gerada;

Seu objetivo é criar um algoritmo que gera os `n` primeiros números da sequência de Fibonacci, onde `n` é um valor fornecido pelo usuário.

## calculadora romanos

Crie uma calculadora de números romanos.

- crie uma calculadora romana das operações `+`, `-`, `*`, `/`, `**`;
    - o intervalo de entrada e resultado deve ser (-4000,4000);
    - isto é, o valor mínimo recebido e calculado será -3999;
    - e o valor máximo recebido e calculado será 3999;
- o resultado da divisão deve ser representado como quociente e resto;
- a entrada dos dois números deve ser em números romanos;
- o resultado deve ser mostrado em números romanos;
- todos os cálculos devem ser salvos em um dicionário, que deve ser armazenado em uma lista;
- encerre o programa quando o usuário digitar `sair`;
- ao final, mostre todos as operações realizadas;
- exemplos :
    - operação tradicional :
        - calculo = {'valor_1': 'X', 'valor_2': 'IV', 'operacao': '+', 'resposta': 'XIV'}
    - operação onde foi entrado um valor maior que 3999 ou menor que -3999 :
        - calculo = {'valor_1': 'erro', 'valor_2': 'MM', 'operacao': '/', 'resposta': 'erro'}
    - modelo usando subtração com algum valor negativo :
        - calculo = {'valor_1': '-C', 'valor_2': 'X', 'operacao': '-', 'resposta': '-CX'}
    - modelo de divisão :
        - calculo = {'valor_1': 'XI', 'valor_2': 'III', 'operacao': '/', 'resposta': 'III', 'resto': 'II'}

## funções do Python

O Python possui diversas funções built-in que facilitam o trabalho. Embora ajudem, é interessante tentar replicar o comportamento delas para entender como funciona e, também, para praticar.
Então, recrie as seguintes funções :
- `sum()`, `len()`, `pow()`, `max()`, `min()`, `abs()`, `round()`, `range()`, `divmod()`

## Jogo da Velha

Crie uma interface gráfica para o jogo da velha usando botões em uma matriz 3x3. Os jogadores podem clicar nos botões para fazer suas jogadas e exiba mensagens de vitória, empate ou próximo jogador em um Label.

## Jogo da Forca

Crie uma interface gráfica para o jogo da forca. Exiba uma palavra oculta com underscore (_) para cada letra não revelada. Os jogadores podem digitar letras em um Entry e clicar em um botão para verificar se a letra está correta. Exiba a palavra atualizada e a imagem da forca à medida que o jogador erra.

## Adivinhar o Número

Crie uma interface gráfica para um jogo de adivinhação de números. Gere um número aleatório e deixe os jogadores digitarem sua suposição em um Entry. Forneça um botão para verificar se a suposição está correta e exiba mensagens informando se é muito alta ou muito baixa.

## Calculadora

Crie uma calculadora, como a do Windows, usando o Tkinter.

## Bloco de Notas

Crie um aplicativo que simule o Bloco de Notas. Implemente a possibilidade de trocar as fontes do campo `Text` durante a execução do programa.

Todas as fontes instaldas podem ser encontradas em :
- Windows : `C:\Windows\Fonts`;
- Linux : `/usr/share/fonts` ou `~/.fonts`;
- macOS : `/Library/Fonts` ou `~/Library/Fonts`
