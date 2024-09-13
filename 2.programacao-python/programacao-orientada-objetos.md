# programação orientada a objetos

A **Programação Orientada a Objetos (POO)** é um paradigma de desenvolvimento de software que organiza o código em torno de **objetos**, em vez de funções e procedimentos. Esses objetos são instâncias de **classes** (representações abstratas de entidades do mundo real ou de conceitos dentro do sistema), que encapsulam tanto os **dados** (atributos) quanto as **funções** (métodos) que operam sobre esses dados.

## principais conceitos da poo

1. **classe** : uma classe é um modelo ou template que define a estrutura e o comportamento de um conjunto de objetos semelhantes. Ela atua como um molde para criar objetos, especificando os atributos (dados) que cada objeto terá e os métodos (funções) que cada objeto poderá executar.

1. **objeto** : um objeto é uma instância de uma classe. É uma entidade concreta criada a partir do modelo definido pela classe, possuindo seus próprios valores para os atributos e a capacidade de executar os métodos definidos na classe.

1. **encapsulamento** : o encapsulamento é o princípio de ocultar os detalhes internos de um objeto e fornecer uma interface pública para interagir com ele. Isso protege os dados do objeto de acessos e modificações indesejadas, permitindo que o objeto gerencie seu próprio estado de forma controlada.

1. **herança** : a herança é um mecanismo que permite criar novas classes (subclasses ou classes derivadas) a partir de classes existentes (superclasses ou classes base). A subclasse herda os atributos e métodos da superclasse, podendo adicionar novos atributos e métodos ou sobrescrever os existentes, promovendo a reutilização de código e a organização hierárquica das classes.

1. **polimorfismo** : o polimorfismo é a capacidade de objetos de diferentes classes responderem à mesma mensagem (chamada de método) de maneiras diferentes. Isso permite que o código seja mais flexível e adaptável, tratando objetos de diferentes classes de forma uniforme através de uma interface comum.

1. **abstração** : a abstração é o processo de focar nos aspectos essenciais de um objeto e ignorar os detalhes irrelevantes. Isso permite criar modelos simplificados e gerenciáveis de entidades complexas, facilitando o entendimento e a manipulação do sistema.

## benefícios da poo

* **modularidade** : a poo promove a organização do código em módulos (classes) coesos e independentes, facilitando a manutenção e a evolução do sistema;
* **reusabilidade** : a herança e o polimorfismo permitem reutilizar código existente em diferentes contextos, aumentando a produtividade e reduzindo a redundância;
* **flexibilidade** : o encapsulamento e o polimorfismo tornam o código mais flexível e adaptável a mudanças, facilitando a manutenção e a extensão do sistema;
* **escalabilidade** : a poo facilita o desenvolvimento de sistemas complexos e de grande porte, permitindo dividir o problema em partes menores e gerenciáveis;
* **manutenibilidade** : a organização modular e a reutilização de código tornam o sistema mais fácil de manter e atualizar ao longo do tempo;

## comando `class`

O comando `class` em Python é usado para definir uma **classe**.

### sintaxe básica

O comando `class` cria uma nova classe em Python. A sintaxe é a seguinte:

```python
class NomeDaClasse:
    pass
```

Aqui, `NomeDaClasse` é o nome da classe que se está criando. O comando `pass` é um placeholder que significa "não faça nada". Ele é temporariamente usado quando você quer definir uma classe sem especificar nenhum detalhe ainda.

Exemplo:

```python
class Carro:
    pass
```

Neste exemplo, foi criada uma classe chamada `Carro`, mas ela ainda não tem nenhuma característica ou comportamento.

### instâncias

Depois de definir uma classe, é possível criar **instâncias** dessa classe. Uma instância é um objeto criado a partir de uma classe, ou seja, um "exemplar" específico dessa classe.

Usando o exemplo da classe `Carro`, é possível criar uma instância da seguinte forma :

```python
meu_carro = Carro()
```

Aqui, `meu_carro` é uma instância da classe `Carro`. Ele é um objeto real, enquanto a classe `Carro` é apenas o molde ou a definição. É possível criar várias instâncias da mesma classe :

```python
carro1 = Carro()
carro2 = Carro()
```

Aqui, `carro1` e `carro2` são duas instâncias diferentes da mesma classe `Carro`. Elas compartilham a mesma estrutura (porque vêm da mesma classe), mas são objetos separados e podem ter suas próprias características.

### classe vs objeto

- **classe** : é uma definição ou molde, como uma receita de bolo ou a planta de um prédio. Ela descreve como os objetos devem ser, mas não é o objeto em si.
- **objeto (ou instância)** : é o resultado concreto criado a partir da classe. Quando se usa a classe para criar algo real, isso é chamado de objeto ou instância.

### exemplo no mundo real

Pense em uma classe como um **plano de uma casa**. O plano define o número de quartos, banheiros, o tamanho da cozinha, etc. Mas ele não é uma casa de verdade.

- a classe é o plano da casa;
- as casas construídas com base nesse plano são os objetos (ou instâncias);

Pode-se construir várias casas usando o mesmo plano, e cada casa será uma instância diferente, embora todas sigam o mesmo formato geral definido no plano.

## método `__init__`

O `__init__` é um **método especial** (também chamado de **método mágico**) em Python. Ele é o **construtor** de uma classe e é responsável por **inicializar** os atributos de uma instância de uma classe assim que essa instância é criada.

Quando se cria uma instância de uma classe, o Python chama automaticamente o método `__init__` para configurar essa nova instância. Embora o `__init__` pareça um método comum, ele tem uma função especial de configurar os atributos iniciais do objeto.

O `__init__` é definido dentro de uma classe da seguinte maneira:

```python
class NomeDaClasse:
    def __init__(self, parametros):
        # inicializa os atributos da instância
```

- o primeiro parâmetro de `__init__` é sempre `self`, que representa a instância da classe; ele é um opcional obrigatório e permite acessar os atributos e métodos dessa instância;
- além de `self`, ainda é poissível passar outros parâmetros ao método `__init__` para inicializar os atributos da instância com valores personalizados;

- Exemplo simples :

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
```

Aqui :

- o método `__init__` recebe `marca` e `modelo` como parâmetros e os usa para definir os atributos `self.marca` e `self.modelo` da instância;
- o `self` refere-se à instância que está sendo criada, e os valores passados ao método `__init__` (como `marca` e `modelo`) são usados para inicializar essa instância;

Quando um objeto da classe `Carro` é criado, o Python executa automaticamente o método `__init__`.

```python
carro1 = Carro('Toyota', 'Corolla')
carro2 = Carro('Honda', 'Civic')
```

- para `carro1`, o `__init__` vai definir `self.marca = 'Toyota'` e `self.modelo = 'Corolla'`;
- para `carro2`, o `__init__` vai definir `self.marca = 'Honda'` e `self.modelo = 'Civic'`;

### o construtor de uma classe

Em Python, o método `__init__` é frequentemente chamado de **construtor** da classe, embora tecnicamente o construtor real seja o método `__new__`. No entanto, o `__init__` é o método que **inicializa** o objeto após a criação.

- o construtor, no sentido prático do termo em Python, é o responsável por **preparar** o objeto recém-criado, atribuindo valores iniciais aos seus atributos;

O fluxo de criação de uma instância de classe pode ser descrito assim :

1. o Python chama o método `__new__` para **criar** uma nova instância da classe;
1. em seguida, chama o método `__init__` para **inicializar** os atributos dessa instância;

Para a maioria dos desenvolvedores, o `__init__` é o que importa, pois é onde se define o estado inicial de um objeto. É nele que os **atributos de instância** são configurados.

## atributos

Os **atributos** são variáveis que armazenam informações sobre um objeto. Eles definem as propriedades e o estado de uma instância de uma classe.

Existem dois tipos principais de atributos em Python :

- **atributos de instância**
- **atributos de classe**

### atributos de instância

Os **atributos de instância** são variáveis que pertencem a uma instância específica de uma classe. Cada instância de uma classe pode ter seus próprios valores para esses atributos, permitindo que objetos diferentes da mesma classe tenham características únicas.

Os atributos de instância são definidos dentro do método `__init__` usando a referência `self`. O `self` permite associar os valores passados como parâmetros ao objeto que está sendo criado.

- Exemplo de Atributos de Instância :

No exemplo abaixo, foi criada uma classe `Carro` com atributos de instância como `marca`, `modelo`, e `ano` :

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo de instância
        self.modelo = modelo  # Atributo de instância
        self.ano = ano  # Atributo de instância
```

Aqui :
- `self.marca`, `self.modelo`, e `self.ano` são os **atributos de instância**;
- Cada instância da classe `Carro` terá seus próprios valores para esses atributos;

Quando se cria diferentes instâncias, cada uma terá seus próprios valores para `marca`, `modelo` e `ano` s:

```python
carro1 = Carro('Toyota', 'Corolla', 2020)
carro2 = Carro('Honda', 'Civic', 2019)

print(carro1.marca)  # Toyota
print(carro2.modelo)  # Civic
print(carro1.ano)  # 2020
```

- o objeto `carro1` terá os atributos `marca='Toyota'`, `modelo='Corolla'`, e `ano=2020`;
- o objeto `carro2` terá os atributos `marca='Honda'`, `modelo='Civic'`, e `ano=2019`;

Esses valores são **específicos** para cada instância de `Carro`, e podem ser diferentes para cada objeto criado.

### atributos de classe

Os **atributos de classe** são compartilhados por **todas** as instâncias de uma classe. Eles são definidos diretamente dentro da classe e fora de qualquer método. Todos os objetos dessa classe acessam e compartilham o mesmo valor para esses atributos, a menos que sejam sobrescritos.

```python
class Carro:
    rodas = 4  # Atributo de classe, compartilhado por todas as instâncias

    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo de instância
        self.modelo = modelo  # Atributo de instância
        self.ano = ano  # Atributo de instância
```

Aqui, `rodas` é um **atributo de classe**. Ele é o mesmo para todas as instâncias da classe `Carro` :

```python
carro1 = Carro('Toyota', 'Corolla', 2020)
carro2 = Carro('Honda', 'Civic', 2019)

print(carro1.rodas)  # 4
print(carro2.rodas)  # 4
```

Se um dos objetos mudar o valor de `rodas`, ele só afetará esse objeto se for sobrescrito em nível de instância:

```python
carro1.rodas = 6  # Muda o número de rodas apenas para carro1
print(carro1.rodas)  # 6
print(carro2.rodas)  # 4 (não foi alterado)
```

## atributos de instância vs atributos de classe

Como mencionado antes, os **atributos de instância** pertencem a cada objeto separadamente, enquanto os **atributos de classe** pertencem à classe em si e são compartilhados por todas as instâncias.

```python
class Carro:
    rodas = 4  # Atributo de classe (compartilhado por todas as instâncias)

    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo de instância (específico para cada instância)
        self.modelo = modelo  # Atributo de instância
        self.ano = ano  # Atributo de instância
```

Aqui:
- `rodas` é um **atributo de classe**. Todos os carros (instâncias) terão 4 rodas, a menos que seja explicitamente alterado.
- `marca`, `modelo` e `ano` são **atributos de instância**. Eles podem variar de um carro para outro.

## métodos de instância

Os **métodos de instância** são funções definidas dentro de uma classe que operam sobre uma instância específica dessa classe. Ou seja, eles têm acesso e podem modificar os **atributos de instância** — valores únicos para cada objeto criado a partir da classe.

Cada método de instância, por convenção, tem o parâmetro `self` como seu primeiro argumento. O `self` se refere à instância específica da classe sobre a qual o método está sendo chamado e permite que você acesse ou modifique seus atributos.

### estrutura

```python
class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor  # Atributo de instância

    def metodo_instancia(self):
        print(f"O valor atual é: {self.valor}")
```

Aqui, `metodo_instancia` é um método de instância. Quando chamamos esse método em uma instância de `MinhaClasse`, ele acessa o atributo `valor` daquela instância em particular.

#### explicando

- **`self`**: É a referência à instância atual da classe. Sempre deve ser o primeiro parâmetro em qualquer método de instância, mas não é necessário passá-lo explicitamente ao chamar o método; o Python o gerencia automaticamente. Ele permite que o método acesse e modifique os atributos e outros métodos de instância.

- **Método de instância**: Qualquer função dentro de uma classe que tem `self` como o primeiro parâmetro.

### exemplos

#### exemplo 1: criando e chamando um método de instância

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

    def saudacao(self):  # Método de instância
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

Aqui, o método de instância `saudacao` usa `self` para acessar os atributos `nome` e `idade`.

```python
# Criando uma instância de Pessoa
pessoa1 = Pessoa("Ana", 30)
pessoa1.saudacao()  # Chama o método saudacao
```

**Saída:**

```
Olá, meu nome é Ana e tenho 30 anos.
```

- o método `saudacao` foi chamado na instância `pessoa1`. Ele acessa os atributos `nome` e `idade` através do `self`;

#### exemplo 2: modificando atributos com métodos de instância

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instância
        self.modelo = modelo  # Atributo de instância

    def mudar_modelo(self, novo_modelo):  # Método de instância
        self.modelo = novo_modelo  # Modificando o atributo de instância
        print(f"O modelo do carro foi atualizado para {self.modelo}.")

# Criando uma instância de Carro
meu_carro = Carro("Toyota", "Corolla")
meu_carro.mudar_modelo("Camry")  # Modifica o modelo
```

**Saída:**

```
O modelo do carro foi atualizado para Camry.
```

- o método `mudar_modelo` foi usado para modificar o valor do atributo `modelo` da instância `meu_carro`;

#### exemplo 3: métodos de instância que executam cálculos

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura  # Atributo de instância
        self.altura = altura  # Atributo de instância

    def calcular_area(self):  # Método de instância
        return self.largura * self.altura

# Criando uma instância de Retangulo
meu_retangulo = Retangulo(5, 3)
area = meu_retangulo.calcular_area()  # Chamando o método calcular_area
print(f"A área do retângulo é: {area}")
```

**Saída:**

```
A área do retângulo é: 15
```

- aqui, o método `calcular_area` retorna a área do retângulo multiplicando os atributos `largura` e `altura`;

### Importância dos Métodos de Instância

1. **Encapsulamento** : eles permitem encapsular o comportamento específico de uma instância dentro da classe; isso mantém a lógica organizada e evita que o código seja espalhado em várias partes do programa;

1. **Acesso e Modificação de Atributos** : métodos de instância podem acessar, modificar e retornar os valores dos atributos de uma instância específica, facilitando o gerenciamento do estado interno do objeto;

1. **Reutilização** : os métodos de instância permitem reutilizar o comportamento, pois pode criar várias instâncias de uma classe e usar os mesmos métodos em diferentes objetos;

#### exemplo 4: métodos que combinam atributos

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo  # Atributo de instância

    def depositar(self, valor):  # Método de instância
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.saldo}")

    def sacar(self, valor):  # Método de instância
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}")

# Criando uma instância de ContaBancaria
minha_conta = ContaBancaria("João", 1000)
minha_conta.depositar(500)  # Adiciona dinheiro na conta
minha_conta.sacar(200)  # Remove dinheiro da conta
```

**Saída:**

```
Depósito de 500 realizado com sucesso. Saldo atual: 1500
Saque de 200 realizado com sucesso. Saldo atual: 1300
```

- o método `depositar` modifica o saldo da instância `minha_conta`, e o método `sacar` verifica se há saldo suficiente antes de realizar o saque;

### Diferenciando Métodos de Instância de Outros Tipos de Métodos

Em Python, existem três tipos principais de métodos em classes:

1. **métodos de instância** : já discutidos, são os mais comuns e operam em instâncias individuais de uma classe;

1. **métodos de classe** : usam o decorador `@classmethod` e recebem a própria classe como primeiro argumento, em vez de uma instância;

1. **métodos estáticos** : usam o decorador `@staticmethod` e não recebem nem a instância nem a classe como parâmetro. são usados quando o comportamento do método não depende da instância ou da classe;

Os métodos de **classe** e **estátivco** serão vistos posteriormente.

## exercícios

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios sobre o Método `__init__`
    1. **Classe simples com `__init__`** : Crie uma classe `Animal` com o método `__init__` que inicialize o atributo `especie`.
    1. **Múltiplos parâmetros no `__init__`** : Crie uma classe `Livro` com o método `__init__` que receba os parâmetros `titulo` e `autor`.
    1. **Parâmetros padrão no `__init__`** : Crie uma classe `Produto` com o método `__init__`, onde o atributo `preco` tenha um valor padrão de 100.
    1. **Inicializando listas no `__init__`** : Crie uma classe `Estudante` com o método `__init__` que inicialize o atributo `notas` como uma lista vazia.
    1. **Modificando o `__init__`** : Modifique a classe `Estudante` do exercício anterior para permitir passar uma lista de notas como parâmetro no método `__init__`.
    1. **Verificação no `__init__`** : Crie uma classe `Pessoa` com o método `__init__` que receba a `idade` e garanta que a idade seja sempre maior que 0.
    1. **Atributo opcional no `__init__`** : Crie uma classe `Computador` que tenha um atributo opcional `marca`, cujo valor padrão seja `"Genérica"` no `__init__`.
    1. **Exibindo valores no `__init__`** : Crie uma classe `Filme` e, no método `__init__`, exiba o título do filme assim que a instância for criada.
    1. **Usando variáveis locais dentro do `__init__`** : Crie uma classe `Carro` com os atributos `marca` e `modelo`, onde o método `__init__` use variáveis locais para armazenar os parâmetros antes de inicializar os atributos de instância.
    1. **Criando instâncias dentro do `__init__`** :  Crie uma classe `Equipe` que, no método `__init__`, crie uma lista de membros (strings) fornecida como parâmetro.
1. Exercícios sobre Atributos de Instância
    1. **Acessando atributos de instância** :  Crie uma classe `Aluno` com os atributos de instância `nome` e `idade`. Crie um objeto e imprima o valor de seus atributos.
    1. **Modificando atributos de instância** :  Crie uma classe `Funcionario` com o atributo `salario`. Crie um objeto e imprima o valor de seus atributos.
    1. **Atributos dependentes de outros** :  Crie uma classe `Circulo` com os atributos `raio` e `area`, onde o `area` seja calculado no método `__init__` a partir do `raio`.
    1. **Atributos com valores fornecidos pelo usuário** :  Crie uma classe `Carro` com os atributos `marca` e `ano`. Permita que o usuário forneça os valores desses atributos ao criar a instância.
    1. **Lista de atributos de instância** :  Crie uma classe `Biblioteca` com um atributo `livros`, que seja uma lista de livros (strings) fornecida no método `__init__`.
    1. **Adicionando elementos a um atributo de instância** :  Crie uma classe `CestaDeCompras` com um atributo `produtos` (uma lista vazia). Peça ao usuário diversos itens que são adicionados em `produtos`.
    1. **Atributos de instância como contadores** :  Crie uma classe `Contador` com um atributo `valor`, que seja inicializado como 0 no método `__init__`. Peça para o usuário um número e incremente `valor` até o número escolhido pelo usuário.
    1. **Atributos de instância dependentes de condições** :  Crie uma classe `Candidato` com os atributos `nome` e `aprovado`. Se a nota for maior ou igual a 60, o atributo `aprovado` deve ser `True`, caso contrário, `False`.
    1. **Atributos de instância com valores calculados** :  Crie uma classe `Viagem` com os atributos `distancia` e `tempo`. Adicione um atributo `velocidade_media` que seja calculado dividindo a distância pelo tempo.
    1. **Atributos de instância inicializados como objetos** :  Crie uma classe `Casa` com um atributo de instância `proprietario`, que seja inicializado como uma instância de uma classe `Pessoa`.
1. Exercícios sobre Atributos de Classe
    1. **Atributo de classe simples** :  Crie uma classe `Pessoa` com um atributo de classe `especie` cujo valor seja `"Humano"`.
    1. **Acessando um atributo de classe** :  Crie uma classe `Carro` com o atributo de classe `rodas` igual a 4. Crie uma instância da classe e acesse o valor do atributo `rodas`.
    1. **Modificando um atributo de classe** :  Crie uma classe `Empresa` com um atributo de classe `empregados`. Modifique o valor desse atributo para 50 fora da classe.
    1. **Atributos de classe com valores dinâmicos** :  Crie uma classe `Banco` com o atributo de classe `taxa_juros`. Crie duas instâncias da classe e veja como o atributo de classe pode ser acessado e modificado globalmente.
    1. **Atributos de classe e instância com o mesmo nome** :  Crie uma classe `Animal` com um atributo de classe `especie` e um atributo de instância `especie`. Crie uma instância e veja qual valor prevalece ao acessá-los.
    1. **Contando o número de instâncias de uma classe** :  Crie uma classe `Aluno` com um atributo de classe `numero_de_alunos` que é incrementado sempre que uma nova instância for criada.
    1. **Atributo de classe com valor compartilhado** :  Crie uma classe `Universidade` com o atributo de classe `pais` igual a `"Brasil"`. Verifique que todas as instâncias dessa classe compartilham esse atributo.
    1. **Atributo de classe e `__init__`** :  Crie uma classe `Livro` com um atributo de classe `numero_de_livros` e incremente esse valor sempre que um novo livro for criado.
    1. **Verificando se o atributo é de instância ou de classe** :  Crie uma classe `Fruta` com um atributo de classe `tipo` e um atributo de instância `cor`. Verifique todos os valores dos atributos.
    1. **Atributos de classe versus instância** :  Crie uma classe `Celular` com um atributo de classe `tecnologia` e um atributo de instância `modelo`. Crie uma instância e veja como os atributos de classe e instância coexistem e podem ser acessados separadamente.
1. Exercícios sobre Atributos e Métodos de Instância
    1. **Criação e Exibição de Atributos** : Crie uma classe `Pessoa` com os atributos de instância `nome` e `idade`. Adicione um método `exibir_informacoes` que exiba esses atributos.
    1. **Atualização de Atributo via Método** : Crie uma classe `Carro` com os atributos `marca` e `modelo`. Adicione um método `mudar_modelo` que permita alterar o modelo do carro.
    1. **Cálculo com Atributos de Instância** : Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione um método `calcular_area` que retorne a área do retângulo.
    1. **Verificação de Atributos** : Crie uma classe `ContaBancaria` com os atributos `saldo` e `titular`. Adicione um método `verificar_saldo` que verifique se o saldo é suficiente para realizar uma operação.
    1. **Método que Retorna Atributos** : Crie uma classe `Livro` com os atributos `titulo` e `autor`. Adicione um método `informacoes_livro` que retorne uma string contendo o título e o autor do livro.
    1. **Modificação Condicional de Atributos** : Crie uma classe `Elevador` com o atributo `andar_atual`. Adicione métodos para `subir` e `descer` de andar, verificando se o andar atual está dentro dos limites de um prédio de 10 andares.
    1. **Método que Usa Vários Atributos** : Crie uma classe `Produto` com os atributos `preco` e `quantidade`. Adicione um método `calcular_total` que retorne o valor total do estoque com base no preço e quantidade.
    1. **Modificação e Exibição de Atributos** : Crie uma classe `Jogador` com os atributos `nome`, `pontos`. Adicione um método `ganhar_pontos` que aumente os pontos do jogador e exiba a nova pontuação.
    1. **Método que Modifica Atributos de Várias Instâncias** : Crie uma classe `Amigo` com o atributo `humor`. Adicione um método `animar_amigo` que mude o humor de todos os amigos de uma lista fornecida.
    1. **Método que Define Atributo com Base em Outros** : Crie uma classe `Circulo` com o atributo `raio`. Adicione um método `definir_diametro` que defina o diâmetro com base no raio.
    1. **Método que Modifica Mais de um Atributo** : Crie uma classe `ContaCorrente` com os atributos `saldo` e `limite`. Adicione um método `ajustar_limite` que ajuste o limite com base no saldo atual.
    1. **Método que Zera Atributos** : Crie uma classe `Jogador` com os atributos `nome` e `vidas`. Adicione um método `perder_vidas` que diminua o número de vidas e um método `resetar_vidas` que zere as vidas.
    1. **Método com Operações Matemáticas em Atributos** : Crie uma classe `Vendedor` com os atributos `vendas` e `comissao`. Adicione um método `calcular_comissao` que retorne o valor da comissão baseada nas vendas e uma porcentagem de comissão.
    1. **Método que Atualiza Listas como Atributos** : Crie uma classe `Turma` com um atributo `alunos` (uma lista). Adicione um método `adicionar_aluno` que permita adicionar novos alunos à turma.
    1. **Método que Lida com Atributos Complexos** : Crie uma classe `Funcionario` com o atributo `horas_trabalhadas`. Adicione um método `registrar_horas` que atualize o total de horas trabalhadas e calcule o pagamento com base em uma taxa por hora.
    1. **Método que Verifica e Modifica Atributos Condicionalmente** : Crie uma classe `CarroEletrico` com os atributos `bateria` (em %) e `autonomia`. Adicione um método `carregar_bateria` que aumenta a porcentagem da bateria e ajuste a autonomia com base na carga.
    1. **Método que Faz Comparações entre Atributos** : Crie uma classe `Produto` com os atributos `preco` e `desconto`. Adicione um método `aplicar_desconto` que subtraia o desconto do preço e retorne o preço final.
    1. **Método com Condicionais e Modificações** : Crie uma classe `Aluno` com os atributos `nome`, `notas` (uma lista de notas) e `media`. Adicione um método `calcular_media` que calcule a média das notas e defina se o aluno está aprovado ou não (média >= 7).
    1. **Método que Reconfigura um Atributo** : Crie uma classe `Veiculo` com o atributo `velocidade`. Adicione um método `ajustar_velocidade` que defina um novo valor para a velocidade e exiba a nova velocidade.
    1. **Método que Lida com Atributos Dinâmicos** : Crie uma classe `Cachorro` com os atributos `nome` e `energia`. Adicione métodos `brincar` (que reduz a energia) e `descansar` (que aumenta a energia), com o valor de energia nunca podendo ser menor que 0 ou maior que 100.

</details>
