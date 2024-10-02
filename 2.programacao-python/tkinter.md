# índice

1. [para que serve](#para-que-serve)
1. [instalando](#instalando)
1. [como funciona](#como-funciona)
1. [classe `tk`](#classe-tk)
1. [elementos tkinter](#elementos-tkinter)
1. [`Label`](#label)
    1. [exercícios `Label`](#exercícios-label)
1. [`Button`](#button)
    1. [exercícios `Button`](#exercícios-button)
1. [`Entry`](#entry)
    1. [exercícios `Entry`](#exercícios-entry)
1. [`Text`](#text)
    1. [exercícios `Text`](#exercícios-text)
1. [`Listbox`](#listbox)
    1. [exercícios `Listbox`](#exercícios-listbox)
1. [`Checkbutton`](#checkbutton)
    1. [exercícios `Checkbutton`](#exercícios-checkbutton)
1. [`Radiobutton`](#radiobutton)
    1. [exercícios `Radiobutton`](#exercícios-radiobutton)
1. [gerenciadores de layout](#gerenciadores-de-layout)
    1. [exercícios gerenciadores de layout](#exercícios-gerenciadores-de-layout)
1. [variáveis](#variáveis)
    1. [exercícios variáveis](#exercícios-variáveis)



# tkinter

O **Tkinter** é a biblioteca padrão do Python para a criação de interfaces gráficas (GUIs - Graphical User Interfaces). Ele fornece um conjunto de ferramentas para construir janelas, botões, caixas de texto, menus e outros elementos visuais que permitem a interação do usuário com o programa.

Essa biblioteca é uma interface para o toolkit gráfico **Tk**, que é multiplataforma. Isso significa que os programas criados com Tkinter funcionam em diferentes sistemas operacionais, como Windows, macOS e Linux, sem a necessidade de modificações no código.

## para que serve

O Tkinter é usado para criar aplicações com uma interface visual, permitindo que os usuários interajam com o programa de maneira mais intuitiva. Diferente dos programas baseados em linha de comando, onde o usuário digita comandos, as interfaces gráficas permitem cliques, inserções de texto, seleções de menus, etc.

Exemplos de programas que podem ser feitos com Tkinter incluem:
- calculadoras simples;
- gerenciadores de arquivos;
- ferramentas de anotação de texto;
- jogos simples;
- painéis de controle para automação de processos;

## instalando

O Tkinter já vem instalado na maioria das distribuições do Python, então, em muitos casos, não é necessário fazer uma instalação manual. Contudo, em alguns sistemas, especialmente em distribuições Linux, pode ser necessário instalar o Tkinter separadamente.

Antes de qualquer instalação, é possível verificar se o Tkinter já está disponível no seu Python. Basta rodar o seguinte comando em um terminal :

```bash
python -m tkinter
```

Se o Tkinter estiver instalado, uma janela será aberta. Caso contrário, uma mensagem de erro será exibida, indicando que o Tkinter não está presente.

### como instalar

#### Windows

No Windows, o Tkinter geralmente já vem junto com a instalação do Python, então não há a necessidade de instalar manualmente. No entanto, se estiver usando uma versão customizada do Python que não inclua o Tkinter, pode ser necessário reinstalar o Python a partir do site oficial ([python.org](https://www.python.org/)) e certificar-se de selecionar a opção "Tkinter" durante a instalação.

#### macOS

No macOS, o Tkinter também costuma vir pré-instalado com o Python. Contudo, se o Python que usado foi instalado via um gerenciador de pacotes como o Homebrew, pode ser necessário instalá-lo separadamente.

Para instalar o Python com suporte ao Tkinter pelo Homebrew, use os seguintes comandos :

```bash
brew install python-tk
```

#### Linux

Em muitas distribuições Linux, o Tkinter não vem incluído com o Python e precisa ser instalado separadamente. Os comandos variam dependendo da distribuição:

- **Ubuntu/Debian**

    ```bash
    sudo apt-get install python3-tk
    ```

- **Fedora**

    ```bash
    sudo dnf install python3-tkinter
    ```

- **Arch Linux**

    ```bash
    sudo pacman -S tk
    ```

#### Conda (Anaconda/Miniconda)

Se estiver usando o Anaconda ou Miniconda, o Tkinter pode ser instalado usando o seguinte comando no ambiente conda :

```bash
conda install -c anaconda tk
```

### testando

Após a instalação, para garantir que o Tkinter está funcionando corretamente, basta executar o mesmo comando testado anteriormente:

```bash
python -m tkinter
```

Se uma janela aparecer sem erros, a instalação foi bem-sucedida.

## como funciona

O Tkinter opera em um modelo de programação baseado em eventos. Isso significa que a aplicação "espera" por interações do usuário (como cliques ou entradas de teclado) e responde a essas interações de forma apropriada.

A estrutura básica de um programa com Tkinter envolve:
1. **Criação da janela principal :** o ponto de partida é a criação de uma janela principal (o "root" ou "raiz"), onde os elementos da interface serão colocados;
1. **Adição de widgets :** widgets são os componentes da interface gráfica, como botões, labels, caixas de entrada, etc; esses widgets são inseridos dentro da janela;
1. **Configuração de eventos :** cada widget pode responder a eventos específicos, como um clique de mouse ou uma tecla pressionada; o programador define o que deve acontecer quando um evento ocorre, associando funções a esses eventos;
1. **Loop de execução :** a aplicação Tkinter precisa estar em um loop contínuo, aguardando e processando eventos do usuário; isso é feito com o método `mainloop()`;

Veja um exemplo simples :

```python
# importa o módulo Tkinter
import tkinter as tk

# cria a janela principal (root)
root = tk.Tk()

# adiciona um rótulo (label) à janela
label = tk.Label(root, text="Olá, Turma!")
label.pack()  # posiciona o rótulo na janela

# inicia o loop de eventos da janela
root.mainloop()
```

Neste exemplo:
- é criada uma janela principal (`root`);
- é adicionado um widget de rótulo (`Label`) com o texto "Olá, Mundo!";
- o método `pack()` é usado para posicionar o rótulo na janela;
- por fim, iniciamos o loop de eventos com `root.mainloop()`;

## classe `tk`

A classe `Tk()` representa a **janela principal** de uma aplicação Tkinter. Ela é responsável por iniciar o loop de eventos e controlar todos os widgets que serão adicionados à interface. Ao criar uma instância de `Tk()`, se está essencialmente criando a janela principal de um aplicativo.

Veja um exemplo básico :

```python
# importa o módulo Tkinter
import tkinter as tk

# cria uma nova instância da classe Tk (a janela principal)
root = tk.Tk()

# configura o título da janela
root.title("Minha segunda janela com Tkinter")

# define o tamanho inicial da janela (largura x altura)
root.geometry("400x300")

# inicia o loop de eventos da janela
root.mainloop()
```

O que está acontecendo acima :

1. **Importação do módulo Tkinter** :
    - o Tkinter precisa ser importado antes de ser utilizado; aqui, `import tkinter as tk` é usado para tornar o código mais conciso, mas também poderia ser usado `import tkinter` diretamente;

2. **Criação da instância `Tk()`** :
    - o objeto `root` é uma instância da classe `Tk()`, que representa a janela principal do programa; toda aplicação Tkinter precisa dessa instância como ponto de partida;
    - isso cria uma janela vazia que, por enquanto, não faz nada até que widgets sejam adicionados;

3. **Configuração do título da janela** :
    - usa-se `root.title("Minha segunda janela com Tkinter")` para dar um título à janela, que aparecerá na barra superior;

4. **Configuração do tamanho da janela** :
    - a função `root.geometry("400x300")` define as dimensões iniciais da janela, onde `"400x300"` indica que a janela terá 400 pixels de largura e 300 pixels de altura;

5. **Loop de eventos (`mainloop()`)** :
    - a chamada `root.mainloop()` é essencial e serve para iniciar o loop de eventos do Tkinter; este loop aguarda interações do usuário (como cliques ou inserção de dados) e mantém a janela aberta até que o usuário a feche; sem esse loop, a janela desapareceria imediatamente após sua criação;

### métodos da instância `tk()`

Uma instância da classe `Tk()` possui diversos métodos que são usados para configurar a aplicação.

Veja a tabela abaixo :

| Nome do Método | Parâmetros | Descrição |
|----|----|----|
| `title()` | `title (str)` | define o título da janela |
| `geometry()` | `geometry_string (str)` | define o tamanho e a posição da janela no formato `"largura"x"altura"+"posição_x"+"posição_y"`. Exemplo: `"400x300+100+200"` |
| `resizable()` | `width (bool), height (bool)` | controla se a janela pode ser redimensionada horizontalmente (largura) e verticalmente (altura) |
| `minsize()` | `min_width (int), min_height (int)` | define o tamanho mínimo permitido da janela |
| `maxsize()` | `max_width (int), max_height (int)` | define o tamanho máximo permitido da janela |
| `iconbitmap()` | `bitmap_path (str)` | define o ícone da janela (somente no Windows) a partir de um arquivo `.ico` |
| `attributes()` | `-alpha (float)` | define a transparência da janela. O valor varia de `0` (completamente transparente) a `1` (completamente opaco) |
| `destroy()` | nenhum | Fecha a janela e encerra o loop de eventos |
| `mainloop()` | nenhum | Inicia o loop de eventos da aplicação, mantendo a janela aberta até que seja fechada |
| `configure()` | `**options` | modifica diversas opções de configuração da janela, como a cor de fundo (`bg`), borda, entre outras |
| `update()` | nenhum | Atualiza a janela, processando eventos pendentes.|
| `update_idletasks()` | nenhum | Processa apenas as tarefas pendentes que não exigem interação do usuário, como a renderização de widgets |
| `after()` | `time (int), func, *args` | executa a função `func` após o tempo especificado em milissegundos. Pode ser usado para agendar eventos futuros |
| `bind()` | `event (str), handler (func)` | associa um evento (como cliques ou pressionamento de teclas) a uma função. Exemplo: associar `<Button-1>` para detectar cliques com o mouse |
| `deiconify()` | nenhum | Restaura uma janela que foi minimizada |
| `withdraw()` | nenhum | Oculta a janela sem fechá-la |
| `lift()` | nenhum | Traz a janela para a frente de todas as outras janelas no sistema |
| `lower()` | nenhum | Envia a janela para trás de todas as outras janelas no sistema |
| `protocol()` | `name (str), func` | associa uma função ao fechamento da janela, por exemplo, capturando o evento de fechar a janela com `"WM_DELETE_WINDOW"` |

## elementos tkinter

### widgets

| Nome do Widget | Parâmetros Comuns | Explicação |
|---|---|---|
| [`Label`](#label) | `text`, `font`, `bg`, `fg`, `width`, `height` | exibe texto ou imagens |
| [`Button`](#button) | `text`, `command`, `width`, `height`, `bg`, `fg` | cria um botão clicável |
| [`Entry`](#entry) | `width`, `bg`, `fg`, `show` | permite a entrada de texto de uma única linha |
| [`Text`](#text) | `width`, `height`, `bg`, `fg`, `wrap` | permite a entrada e exibição de texto multilinha |
| [`Listbox`](#listbox) | `width`, `height`, `bg`, `fg`, `selectmode` | exibe uma lista de itens que podem ser selecionados |
| [`Checkbutton`](#checkbutton) | `text`, `variable`, `onvalue`, `offvalue`, `command` | cria uma caixa de seleção (checkbox) |
| [`Radiobutton`](#radiobutton) | `text`, `variable`, `value`, `command` | cria um botão de opção (radio button) dentro de um grupo |
| `Scale` | `from_`, `to`, `orient`, `length`, `tickinterval`, `resolution`, `command` | cria um controle deslizante (slider) para selecionar um valor numérico |
| `Scrollbar` | `orient`, `command` | cria uma barra de rolagem para navegar em conteúdo maior que a área visível |
| `Frame` | `bg`, `relief`, `bd` | cria um contêiner para organizar outros widgets |
| `Toplevel` | `bg`, `title` | cria uma nova janela de nível superior (semelhante à janela principal) |
| `Menu` || Cria uma barra de menus |
| `Menubutton` | `text`, `menu` | cria um botão que abre um menu suspenso |
| `Canvas` | `width`, `height`, `bg` | cria uma área para desenhar gráficos e formas |
| `Spinbox` | `from_`, `to`, `increment`, `values`, `wrap`, `command` | cria uma caixa de entrada com setas para cima e para baixo para selecionar um valor de uma lista ou intervalo |
| `PanedWindow` | `orient`, `showhandle`, `sashrelief`, `sashwidth` | cria uma janela com painéis redimensionáveis |
| `LabelFrame` | `text`, `bg`, `relief`, `bd` | cria um frame com um rótulo |
| `Message` | `text`, `bg`, `fg`, `width`, `aspect`, `justify`, `relief`, `bd` | exibe texto multilinha que se ajusta automaticamente à área disponível |
| `OptionMenu` | `variable`, `*values` | cria um menu suspenso para selecionar uma opção de uma lista |

### variáveis

| Nome da Variável | Parâmetros | Explicação |
|----|----|----|
| [`StringVar`](#stringvar)  | `value=None`  | armazena e gerencia valores do tipo `str`. Usada para associar widgets de texto, como `Entry` e `Label` |
| [`IntVar`](#intvar) | `value=None` | armazena e gerencia valores inteiros (`int`). Usada com widgets como `Radiobutton` e `Checkbutton` |
| [`DoubleVar`](#doublevar) | `value=None` | armazena e gerencia valores de ponto flutuante (`float`). Usada para valores numéricos, como em entradas ou cálculos |
| [`BooleanVar`](#booleanvar) | `value=None` | armazena e gerencia valores booleanos (`True` ou `False`). Usada para associar widgets como `Checkbutton` |

- `value`: O valor inicial que a variável irá armazenar. Por padrão, é `None` para `StringVar`, `IntVar`, `DoubleVar` e `BooleanVar`.

## `Label`

O **Label** é um widget simples usado para exibir textos ou imagens estáticas em uma janela. Ele é normalmente utilizado para rótulos, mensagens ou títulos em uma interface gráfica.

```python
label = tk.Label(parent, options...)
```

### parâmetros mais comuns

- **`parent`** : a janela ou frame onde o rótulo será colocado (geralmente a instância `Tk()` ou um `Frame()`);
- **`text`** : define o texto a ser exibido no rótulo;
- **`bg`** : define a cor de fundo;
- **`fg`** : define a cor do texto;
- **`font`** : define a fonte, estilo e tamanho do texto;
- **`image`** : exibe uma imagem em vez de texto;
- **`padx`, `pady`** : define o espaçamento horizontal e vertical ao redor do rótulo;

### exemplo

```python
import tkinter as tk

# criação da janela principal
root = tk.Tk()
root.title("Exemplo de Label")
root.geometry("300x200")

# criando um rótulo (Label)
label = tk.Label(
    root,
    text="Olá, Mundo!",
    font=("Arial", 20),
    bg="lightblue",
    fg="black")
# adicionando com padding
label.pack(padx=20, pady=20)

# iniciando o loop de eventos
root.mainloop()
```

- **`text="Olá, Mundo!"`** : define o texto exibido;
- **`font=("Arial", 20)`** : define a fonte como Arial e o tamanho 20;
- **`bg="lightblue"` e `fg="black"`** : define a cor de fundo e a cor do texto;
- **`pack()`** : adiciona o rótulo à janela com espaçamento ao redor;

## exercícios `Label`

<details>
<summary>Lista de Exercícios</summary>

1. **Exibindo Texto Simples** : Crie uma janela com um `Label` que exiba o texto "Olá, Mundo!". Personalize o tamanho da janela e o tamanho da fonte do texto.
1. **Modificando Texto de um Label** : Crie um programa que contenha um botão e um `Label`. Ao clicar no botão, o texto do `Label` deve ser alterado para "Texto modificado!".
1. **Labels com Várias Fontes** : Crie três `Labels`, cada um exibindo o texto "Fonte A", "Fonte B" e "Fonte C", com diferentes estilos de fonte, tamanhos e cores.
1. **Exibindo Imagens em um Label** : Use o widget `Label` para exibir uma imagem (formato PNG ou JPG). Certifique-se de redimensionar a janela de acordo com a imagem.
1. **Label Dinâmico com Variável** : Crie um programa com uma `StringVar` e um `Label`. Modifique o valor da `StringVar` dinamicamente a cada 2 segundos para exibir diferentes mensagens no `Label`.
1. **Criando Labels com Fundo e Borda** : Crie dois `Labels` com textos diferentes. Um deve ter uma cor de fundo (background) personalizada e o outro deve ter uma borda (borderwidth) configurada.
1. **Label com Texto Longo e Quebra de Linha** : Crie um `Label` que exiba um texto longo e configure o widget para que o texto seja quebrado automaticamente em múltiplas linhas, ajustando a largura do widget.
1. **Centralizando um Label** : Crie um `Label` que seja centralizado horizontalmente e verticalmente dentro da janela. Use o método de layout `pack()` ou `grid()` para centralizar o widget.
1. **Interação entre Entry e Label** : Crie um programa com um `Entry` e um `Label`. O texto digitado no `Entry` deve aparecer em tempo real no `Label`, conforme o usuário digita.
1. **Alterando o Texto do Label com Radiobuttons** : Crie três `Radiobuttons`, cada um com uma cor como opção (vermelho, verde e azul). Quando o usuário selecionar uma das cores, o texto do `Label` deve mudar para "Você escolheu: [cor]".

</details>

---

## `Button`

O **Button** cria um botão interativo que pode realizar uma ação quando clicado. Ele pode exibir texto, uma imagem ou executar uma determinada ação.

```python
button = tk.Button(parent, options...)
```

### parâmetros mais comuns

- **`parent`** : a janela ou frame onde o botão será colocado;
- **`text`** : define o texto exibido no botão;
- **`command`** : define a função a ser chamada quando o botão for clicado;
- **`bg`** e **`fg`** : define a cor de fundo e a cor do texto do botão;
- **`font`** : define a fonte do texto no botão;
- **`state`** : define o estado do botão (ativo ou desativado);

### exemplo

```python
import tkinter as tk

def on_click():
    label.config(text="Botão clicado!")

# criação da janela principal
root = tk.Tk()
root.title("Exemplo de Button")
root.geometry("300x200")

# criando um rótulo (Label)
label = tk.Label(
    root,
    text="Clique no botão",
    font=("Arial", 16))
label.pack(padx=10, pady=10)

# criando um botão (Button)
button = tk.Button(
    root,
    text="Clique aqui",
    command=on_click,
    font=("Arial", 16),
    bg="lightgreen")
button.pack(padx=10, pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`command=on_click`** : especifica que, ao clicar no botão, a função `on_click()` será chamada;
- **`label.config()`** : atualiza o texto do rótulo dinamicamente quando o botão é clicado;
- **`bg="lightgreen"`** : define a cor de fundo do botão;

## exercícios `Button`

<details>
<summary>Lista de Exercícios</summary>

1. **Botão Simples** : Crie uma janela com um único botão que, quando clicado, exibe a mensagem "Botão Clicado!" no terminal (usando a função `print()`).
1. **Desabilitando e Habilitando o Botão** : Crie um programa com um botão que começa habilitado. Quando clicado, ele deve ser desativado (desabilitado). Adicione outro botão que reative o botão anterior.
1. **Botão que Muda o Texto de um Label** : Crie uma interface com um botão e um `Label`. Ao clicar no botão, o texto do `Label` deve mudar para "Botão Pressionado!".
1. **Botão com Cores Personalizadas** : Crie três botões, cada um com uma cor de fundo (background) e uma cor de texto (foreground) personalizada. Ao clicar em qualquer botão, exiba uma mensagem no terminal indicando qual botão foi clicado.
1. **Botão que Fecha a Janela** : Crie um programa com um botão que, ao ser clicado, fecha a janela do Tkinter (usando o método `destroy()`).
1. **Botão com Tamanho Ajustado** : Crie um botão com largura e altura definidas manualmente (usando os parâmetros `width` e `height`). Quando clicado, exiba uma mensagem no terminal indicando o tamanho do botão.
1. **Botão com Imagem** : Use o widget `Button` para criar um botão com uma imagem (formato PNG ou JPG) ao invés de texto. Quando o botão for clicado, exiba uma mensagem no terminal.
1. **Botão que Inicia e Para um Temporizador** : Crie um programa com dois botões: um para iniciar um temporizador que incrementa um contador a cada segundo e exibe o valor em um `Label`, e outro botão para parar o temporizador.
1. **Botão de Alternância (Toggle Button)** : Crie um botão que alterne entre dois estados: "ON" e "OFF". Quando estiver "ON", o botão deve exibir "Desligar" e, quando estiver "OFF", deve exibir "Ligar". Ao clicar, ele deve alternar entre os estados.
1. **Botão com Funções Diferentes para Clique Simples e Duplo** : Crie um programa com um botão que execute uma função ao ser clicado uma vez e outra função ao ser clicado duas vezes (usando os eventos `<Button-1>` para clique simples e `<Double-1>` para clique duplo).

</details>

---

## `Entry`

O **Entry** é um widget de entrada de texto de linha única, usado para coletar informações como nomes, senhas ou qualquer tipo de dado que caiba em uma única linha.

```python
entry = tk.Entry(parent, options...)
```

### parâmetros mais comuns

- **`parent`** : a janela ou frame onde o widget será colocado;
- **`textvariable`** : associado a uma variável do tipo `StringVar()`, permite obter ou alterar o texto do campo dinamicamente;
- **`show`** : usado para ocultar o texto digitado, ideal para campos de senha. Por exemplo, `show="*"` exibe apenas asteriscos no campo;
- **`bg`**, **`fg`** : define as cores de fundo e do texto, respectivamente;
- **`font`** : define a fonte usada no campo;
- **`state`** : define o estado do campo (`normal` ou `disabled`);

### métodos úteis

- **`get()`** : obtém o texto atual do campo;
- **`delete(start, end)`** : apaga o texto entre as posições `start` e `end`;
- **`insert(index, string)`** : insere texto em uma posição específica;

### exemplo

```python
import tkinter as tk

def mostra_digitado():
    digitado = entry.get()  # obtém o texto do campo
    label.config(text=f"Você digitou: {digitado}")

# criação da janela principal
root = tk.Tk()
root.title("Exemplo de Entry")
root.geometry("300x150")

# criando um rótulo (Label)
label = tk.Label(root, text="Digite algo:", font=("Arial", 12))
label.pack(padx=10, pady=10)

# criando um campo de entrada (Entry)
entry = tk.Entry(root, font=("Arial", 12), bg="lightyellow")
entry.pack(padx=10, pady=10)

# botão para exibir o texto digitado
button = tk.Button(
    root,
    text="Mostrar Texto",
    command=mostra_digitado,
    font=("Arial", 12))
button.pack(padx=10, pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`get()`** : obtém o valor atual do campo `Entry`;
- **`label.config()`** : atualiza o texto do rótulo com o valor obtido do campo;

## exercícios `Entry`

<details>
<summary>Lista de Exercícios</summary>

1. **Entrada Simples** : Crie uma janela com um widget `Entry` e um botão. Quando o botão for clicado, o texto inserido no `Entry` deve ser exibido no terminal (usando `print()`).
1. **Limpar Entrada** : Crie uma interface com um widget `Entry` e dois botões: um para exibir o conteúdo da entrada no terminal e outro para limpar o texto digitado no `Entry`.
1. **Entrada de Texto com Placeholder** : Crie um `Entry` que exiba um texto padrão (placeholder) quando vazio, como "Digite seu nome". O texto deve desaparecer quando o usuário começar a digitar.
1. **Verificar o Tamanho do Texto** : Crie um programa com um `Entry` e um botão. Quando o botão for clicado, o programa deve verificar se o texto inserido tem mais de 5 caracteres e, se for o caso, exibir "Texto válido" em um `Label`, ou "Texto muito curto" caso contrário.
1. **Entrada de Senha (Password Entry)** : Crie um `Entry` que oculte os caracteres digitados, como em um campo de senha. Exiba o valor inserido em um `Label` ao clicar em um botão.
1. **Entrada Numérica** : Crie um `Entry` que só permita a entrada de números inteiros (use validação ou o método `validatecommand`). Quando o valor for inserido, exiba-o em um `Label`.
1. **Entrada com Texto Capitalizado Automaticamente** : Crie um `Entry` onde o texto digitado seja automaticamente convertido para letras maiúsculas enquanto o usuário digita. Exiba o valor em um `Label`.
1. **Verificar se o Campo de Entrada Está Vazio** : Crie uma interface com um `Entry` e um botão. Quando o botão for clicado, o programa deve verificar se o campo de entrada está vazio e, se estiver, exibir uma mensagem de erro em um `Label`.
1. **Entrada com Limite de Caracteres** : Crie um `Entry` com um limite máximo de 10 caracteres. Se o usuário tentar digitar mais, impeça que os caracteres adicionais sejam adicionados. Exiba a contagem de caracteres restantes em tempo real em um `Label`.
1. **Exibir Texto Digitado em Tempo Real** : Crie um `Entry` e um `Label`. À medida que o usuário digita no `Entry`, o texto deve ser exibido em tempo real no `Label`, sem a necessidade de pressionar um botão.

</details>

---

## `Text`

O **Text** é um widget que permite a entrada e exibição de múltiplas linhas de texto, sendo bastante utilizado em caixas de texto onde o usuário pode escrever ou visualizar blocos de texto.

```python
text = tk.Text(parent, options...)
```

### parâmetros mais comuns

- **`parent`** : a janela ou frame onde o campo de texto será colocado;
- **`width`** : define a largura do widget (em caracteres);
- **`height`** : define a altura do widget (em linhas);
- **`bg`** e **`fg`** : define a cor de fundo e a cor do texto;
- **`font`** : define a fonte usada no campo de texto;
- **`state`** : define o estado do campo de texto (`normal`, `disabled`, etc.);

### métodos úteis

- **`get(start, end)`** : obtém o texto do widget entre as posições `start` e `end`;
- **`insert(position, text)`** : insere texto no widget na posição especificada;
- **`delete(start, end)`** : remove texto entre as posições `start` e `end`;

### exemplo

```python
import tkinter as tk

def mostra_texto():
    # obtém o texto do campo de texto
    texto_usuario = text_box.get("1.0", tk.END)
    # exibe o texto no rótulo
    label.config(text=texto_usuario)

# criação da janela principal
root = tk.Tk()
root.title("Exemplo de Text")
root.geometry("400x300")

# criando um rótulo (Label)
label = tk.Label(
    root,
    text="Digite algo abaixo:",
    font=("Arial", 14))
label.pack(padx=10, pady=10)

# criando um campo de texto (Text)
text_box = tk.Text(
    root,
    width=40,
    height=5,
    font=("Arial", 12))
text_box.pack(padx=10, pady=10)

# criando um botão (Button) para exibir o texto digitado
button = tk.Button(
    root,
    text="Exibir texto",
    command=mostra_texto,
    font=("Arial", 14),
    bg="lightblue")
button.pack(padx=10, pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`text_box.get("1.0", tk.END)`** : obtém todo o texto do campo, começando da linha 1, caractere 0 (`1.0`), até o fim (`tk.END`);
- **`text_box.insert()`** : pode ser usado para adicionar texto programaticamente ao widget;
- **`text_box.delete()`** : pode ser usado para apagar partes ou todo o conteúdo do widget;
- **`label.config()`** : atualiza o texto do rótulo para mostrar o conteúdo do campo de texto;

## exercícios `Text`

<details>
<summary>Lista de Exercícios</summary>

1. **Text Widget Básico** : Crie uma janela com um widget `Text` e um botão. Quando o botão for clicado, o conteúdo digitado no `Text` deve ser exibido no terminal (usando `print()`).
1. **Limpar Conteúdo do Text Widget** : Crie um widget `Text` com dois botões: um para exibir o conteúdo digitado e outro para limpar o conteúdo do widget.
1. **Contagem de Caracteres no Text Widget** : Crie um `Text` e um botão. Quando o botão for clicado, exiba a quantidade de caracteres inseridos no widget `Text` em um `Label`.
1. **Text Widget com Barra de Rolagem** : Crie um `Text` que possa exibir grandes blocos de texto e adicione uma barra de rolagem para permitir a navegação vertical do conteúdo.
1. **Busca de Texto no Widget** : Crie um programa com um `Text` e um `Entry`. Quando o usuário digitar uma palavra no `Entry` e pressionar um botão, destaque todas as ocorrências da palavra dentro do widget `Text`.
1. **Inserir Texto Programaticamente** : Crie um programa onde um botão insere um texto predefinido no `Text` sempre que clicado. O texto deve ser inserido no final do conteúdo já existente.
1. **Formatação de Texto (Negrito, Itálico)** : Crie um `Text` e dois botões: um para aplicar negrito e outro para aplicar itálico ao texto selecionado. Use tags do `Text` para alterar o estilo.
1. **Desabilitar Edição no Text Widget** : Crie um `Text` com um botão. O botão deve alternar entre habilitar e desabilitar a edição no `Text`, permitindo ou bloqueando o usuário de alterar o texto.
1. **Salvar Conteúdo do Text em um Arquivo** : Crie um programa com um `Text` e um botão "Salvar". Quando o botão for clicado, o conteúdo digitado no `Text` deve ser salvo em um arquivo de texto no disco.
1. **Contagem de Palavras no Text Widget** : Crie um programa que exiba a contagem de palavras inseridas no widget `Text` em tempo real, conforme o usuário digita. Exiba o número de palavras em um `Label`.

</details>

---

## `Listbox`

O **Listbox** exibe uma lista de itens, e o usuário pode selecionar um ou mais deles. Ele é útil para mostrar listas de opções, como listas de arquivos, opções de escolha múltipla, etc.

```python
listbox = tk.Listbox(parent, options...)
```

### parâmetros mais comuns

- **`parent`** : a janela ou frame onde o widget será colocado;
- **`selectmode`** : define o modo de seleção; valores comuns são `SINGLE` (seleção única) e `MULTIPLE` (seleção múltipla);
- **`height`** : define o número de linhas visíveis no Listbox;
- **`bg`**, **`fg`** : define as cores de fundo e do texto;
- **`font`** : define a fonte usada no Listbox;

### métodos úteis

- **`insert(index, *elements)`** : insere itens no Listbox em uma posição específica;
- **`delete(start, end)`** : remove itens entre as posições `start` e `end`;
- **`get(start, end)`** : obtém os itens entre as posições `start` e `end`;
- **`curselection()`** : retorna o índice dos itens selecionados;

### exemplo

```python
import tkinter as tk

def mostra_selecionados():
    indices_selecionados = listbox.curselection()  # Obtém os índices dos itens selecionados
    itens_selecionados = [listbox.get(i) for i in indices_selecionados]  # Converte índices em itens
    label.config(text=f"Selecionado: {', '.join(itens_selecionados)}")

# criação da janela principal
root = tk.Tk()
root.title("Exemplo de Listbox")
root.geometry("300x200")

# criando uma lista de itens
listbox = tk.Listbox(
    root,
    selectmode="SINGLE",
    font=("Arial", 12),
    height=5)
listbox.pack(padx=10, pady=10)
for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
    listbox.insert(tk.END, item)

# criando um rótulo (Label)
label = tk.Label(
    root,
    text="Selecione um item",
    font=("Arial", 12))
label.pack(padx=10, pady=10)

# botão para exibir a seleção
button = tk.Button(
    root,
    text="Mostrar Seleção",
    command=mostra_selecionados,
    font=("Arial", 12))
button.pack(padx=10, pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`curselection()`** : obtém os índices dos itens selecionados;
- **`get()`** : converte os índices em valores para exibir os itens selecionados no rótulo;

## exercícios `Listbox`

<details>
<summary>Lista de Exercícios</summary>

1. **Listbox Simples** : Crie uma janela com um `Listbox` contendo uma lista de frutas (como maçã, banana e laranja). Exiba a fruta selecionada em um `Label` quando o usuário clicar em um botão.
1. **Adicionar Itens ao Listbox** : Crie um `Listbox` vazio e um `Entry`. Quando o usuário digitar um texto no `Entry` e clicar em um botão "Adicionar", o texto deve ser adicionado como um novo item no `Listbox`.
1. **Remover Itens do Listbox** : Crie um `Listbox` com cinco itens e um botão "Remover". Quando o botão for clicado, o item selecionado deve ser removido da lista.
1. **Selecionar Múltiplos Itens** : Crie um `Listbox` que permita a seleção de múltiplos itens (usando a opção `selectmode=MULTIPLE`). Quando um botão for clicado, exiba os itens selecionados em um `Label`.
1. **Mover Itens Entre Dois Listboxes** : Crie dois `Listboxes` lado a lado e dois botões ">>" e "<<". O botão ">>" deve mover o item selecionado do primeiro `Listbox` para o segundo, e o botão "<<" deve fazer o inverso.
1. **Contar Itens no Listbox** : Crie um `Listbox` e um botão "Contar". Quando o botão for clicado, exiba o número total de itens no `Listbox` em um `Label`.
1. **Listbox com Barra de Rolagem** : Crie um `Listbox` com 20 itens e adicione uma barra de rolagem para navegar pelos itens.
1. **Modificar o Texto de um Item Selecionado** : Crie um `Listbox` e um botão "Modificar". Quando um item for selecionado e o botão for clicado, o texto do item selecionado deve ser modificado para "Item Modificado".
1. **Limpar Todo o Conteúdo do Listbox** : Crie um `Listbox` com 5 itens e um botão "Limpar". Quando o botão for clicado, todos os itens devem ser removidos do `Listbox`.
1. **Mover Item Selecionado para Cima ou para Baixo** : Crie um `Listbox` com cinco itens e dois botões: "Mover Para Cima" e "Mover Para Baixo". O botão "Mover Para Cima" deve mover o item selecionado para uma posição acima na lista, e o botão "Mover Para Baixo" deve movê-lo para uma posição abaixo.

</details>

---

## `Checkbutton`

O **Checkbutton** cria uma caixa de seleção que permite ao usuário marcar ou desmarcar uma opção. Ele é frequentemente utilizado em formulários onde múltiplas escolhas podem ser feitas.

```python
checkbutton = tk.Checkbutton(parent, options...)
```

### parâmetros mais comuns

- **`parent`** : a janela ou frame onde o widget será colocado;
- **`text`** : define o texto associado ao Checkbutton;
- **`variable`** : uma variável do tipo `IntVar()` ou `BooleanVar()` que rastreia o estado (marcado ou desmarcado);
- **`onvalue`** e **`offvalue`** : define os valores para a variável quando o Checkbutton estiver marcado ou desmarcado;

### exemplo

```python
import tkinter as tk

def mostra_selecionados():
    label.config(text=f"Opção marcada: {opcao.get()}")

# criação da janela principal
root = tk.Tk()
root.title("Exemplo de Checkbutton")
root.geometry("300x150")

# variável associada ao Checkbutton
opcao = tk.IntVar()

# criando um Checkbutton
checkbutton = tk.Checkbutton(
    root,
    text="Aceitar Termos",
    variable=opcao,
    onvalue=1,
    offvalue=0)
checkbutton.pack(padx=10, pady=10)

# criando um rótulo (Label)
label = tk.Label(root, text="Opção marcada: 0", font=("Arial", 12))
label.pack(padx=10, pady=10)

# botão para exibir o estado
button = tk.Button(
    root,
    text="Mostrar Seleção",
    command=mostra_selecionados,
    font=("Arial", 12))
button.pack(padx=10, pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`variable=opcao`** : a variável `opcao` armazena o estado do Checkbutton (marcado ou desmarcado);
- **`onvalue=1` e `offvalue=0`** : define os valores quando o Checkbutton está marcado ou desmarcado;

## exercícios `Checkbutton`

<details>
<summary>Lista de Exercícios</summary>

1. **Checkbutton Simples** : Crie um programa com um `Checkbutton` que, ao ser marcado ou desmarcado, exibe o estado atual ("Marcado" ou "Desmarcado") em um `Label`.
1. **Checkbutton com Variável de Controle** : Crie um `Checkbutton` associado a uma variável `IntVar`. Quando o `Checkbutton` for alterado, exiba o valor da variável (`1` para marcado, `0` para desmarcado) em um `Label`.
1. **Vários Checkbuttons Independentes** : Crie três `Checkbuttons` independentes para selecionar "Pizza", "Hambúrguer" e "Sushi". Ao clicar em um botão "Exibir Seleção", mostre quais opções estão marcadas em um `Label`.
1. **Checkbuttons com Estado Inicial** : Crie dois `Checkbuttons` com estado inicial, um marcado e outro desmarcado. Permita que o usuário altere os estados e exiba os novos estados em um `Label`.
1. **Checkbutton que Habilita e Desabilita Outros Widgets** : Crie um `Checkbutton` que, quando marcado, habilita um `Entry` para que o usuário possa digitar. Quando desmarcado, o `Entry` deve ser desabilitado (usando o método `config(state=DISABLED)`).
1. **Alternando Texto de um Checkbutton** : Crie um `Checkbutton` com o texto "Ativar". Quando ele for marcado, o texto deve mudar para "Desativar". Quando desmarcado, o texto deve voltar para "Ativar".
1. **Selecionar e Desmarcar Todos os Checkbuttons** : Crie cinco `Checkbuttons` com opções variadas (por exemplo, "Opção 1", "Opção 2", etc.) e dois botões: "Selecionar Todos" e "Desmarcar Todos". Ao clicar nesses botões, todos os `Checkbuttons` devem ser marcados ou desmarcados, respectivamente.
1. **Checkbuttons com Contagem de Seleção** : Crie três `Checkbuttons`. Quando o usuário marcar ou desmarcar qualquer um deles, exiba em um `Label` quantos `Checkbuttons` estão atualmente marcados.
1. **Checkbutton que Controla a Cor de Fundo** : Crie três `Checkbuttons`, cada um associado a uma cor (vermelho, verde e azul). Quando o `Checkbutton` for marcado, a cor correspondente deve ser aplicada como cor de fundo da janela.
1. **Checkbutton para Ativar/Desativar Funcionalidade** : Crie um `Checkbutton` que, quando marcado, ative uma função de temporizador que exibe a hora atual em um `Label` a cada segundo. Quando desmarcado, o temporizador deve ser desativado.

</details>

---

## `Radiobutton`

O **Radiobutton** permite a seleção de apenas uma opção entre várias. É usado quando o usuário deve escolher uma única opção em um grupo.

```python
radiobutton = tk.Radiobutton(parent, options...)
```

### parâmetros mais comuns

- **`parent`** : a janela ou frame onde o widget será colocado;
- **`text`** : define o texto associado ao Radiobutton;
- **`variable`** : uma variável do tipo `IntVar()` que armazena o valor da opção selecionada;
- **`value`** : o valor atribuído à variável quando o Radiobutton está selecionado;

### exemplo

```python
import tkinter as tk

def mostra_selecionados():
    label.config(text=f"Opção selecionada: {radio_var.get()}")

# criação da janela principal
root = tk.Tk()
root.title("Exemplo de Radiobutton")
root.geometry("300x200")

# variável associada aos Radiobuttons
radio_var = tk.IntVar()

# criando Radiobuttons
radiobutton1 = tk.Radiobutton(root, text="Opção 1", variable=radio_var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Opção 2", variable=radio_var, value=2)
radiobutton3 = tk.Radiobutton(root, text="Opção 3", variable=radio_var, value=3)

radiobutton1.pack(padx=10, pady=5)
radiobutton2.pack(padx=10, pady=5)
radiobutton3.pack(padx=10, pady=5)

# criando um rótulo (Label)
label = tk.Label(root, text="Nenhuma opção selecionada", font=("Arial", 12))
label.pack(padx=10, pady=10)

# botão para exibir a seleção
button = tk.Button(
    root,
    text="Mostrar Seleção",
    command=mostra_selecionados,
    font=("Arial", 12))
button.pack(padx=10, pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`variable=radio_var`** : a variável `radio_var` armazena o valor da opção selecionada;
- **`value=1`, `value=2`, `value=3`** : define os valores associados a cada Radiobutton;

## exercícios `Radiobutton`

<details>
<summary>Lista de Exercícios</summary>

1. **Radiobutton Simples** : Crie três `Radiobuttons` com opções de cores ("Vermelho", "Verde", "Azul"). Exiba a cor selecionada em um `Label` quando qualquer um dos `Radiobuttons` for clicado.
1. **Radiobutton com Variável de Controle** : Crie quatro `Radiobuttons` (por exemplo, "Opção A", "Opção B", "Opção C" e "Opção D") vinculados a uma variável `IntVar`. Quando o usuário selecionar uma opção, exiba o valor correspondente em um `Label`.
1. **Radiobutton que Controla o Texto de um Label** : Crie três `Radiobuttons` com diferentes opções de saudação ("Bom dia", "Boa tarde", "Boa noite"). Quando o usuário selecionar uma saudação, o texto de um `Label` deve ser atualizado com a saudação escolhida.
1. **Formulário de Seleção de Gênero** : Crie um formulário com dois `Radiobuttons` para selecionar o gênero (por exemplo, "Masculino" e "Feminino"). Quando um botão "Enviar" for clicado, exiba a escolha em um `Label`.
1. **Radiobuttons Desativados e Habilitados Dinamicamente** : Crie três `Radiobuttons`, mas deixe-os inicialmente desativados (usando `state=DISABLED`). Adicione um `Checkbutton` que, quando marcado, habilite os `Radiobuttons`.
1. **Seleção de Opções de Tamanho** : Crie um conjunto de três `Radiobuttons` que permita selecionar tamanhos de camisetas ("Pequeno", "Médio", "Grande"). Exiba o tamanho selecionado em um `Label` e mostre uma mensagem de "Seleção inválida" caso nenhum tamanho tenha sido escolhido.
1. **Mudar a Cor de Fundo com Radiobutton** : Crie quatro `Radiobuttons` com opções de cores. Quando o usuário selecionar uma cor, altere a cor de fundo da janela para a cor correspondente.
1. **Radiobutton com Imagens** : Crie três `Radiobuttons`, cada um associado a uma imagem (como ícones de frutas: maçã, banana, uva). Ao selecionar um `Radiobutton`, exiba a imagem correspondente em um `Label`.
1. **Radiobutton que Controla Outras Funções** : Crie dois `Radiobuttons`, "Ativar" e "Desativar". Quando "Ativar" for selecionado, um `Entry` deve ser habilitado. Quando "Desativar" for selecionado, o `Entry` deve ser desabilitado.
1. **Radiobuttons com Função de Enquete** : Crie uma interface com cinco `Radiobuttons` representando diferentes faixas etárias (ex: "Menos de 18", "18-25", "26-35", "36-50", "Mais de 50"). Quando o usuário clicar em "Submeter", exiba a faixa etária selecionada em um `Label`.

</details>

---

## variáveis

No Tkinter, além de usar variáveis Python normais, há um conjunto especial de **variáveis de controle** que são projetadas para armazenar e rastrear valores que são associados a widgets interativos. Essas variáveis são necessárias quando se quer vincular o estado de um widget com um valor dinâmico (como entradas de texto, seleção de botões de rádio, checkbuttons, etc.). Essas variáveis são subclasses do tipo especial `Variable`, projetado para facilitar a interação entre o código e os widgets.

O Tkinter fornece quatro principais tipos de variáveis de controle, cada uma projetada para lidar com diferentes tipos de dados:

1. **`StringVar`** : variável para armazenar strings (texto);
1. **`IntVar`** : variável para armazenar inteiros;
1. **`DoubleVar`** : variável para armazenar números de ponto flutuante (float);
1. **`BooleanVar`** : variável para armazenar valores booleanos (`True` ou `False`);

Cada uma dessas variáveis possui métodos que permitem obter e definir o valor associado, e elas são comumente usadas com widgets que precisam manter um valor dinâmico, como `Entry`, `Checkbutton`, `Radiobutton`, e outros.

### `StringVar`

A variável `StringVar` (String Variable) é usada para armazenar e gerenciar valores de texto. É útil para widgets como `Entry`, `Label`, e `OptionMenu`.

- **`get()`** : retorna o valor armazenado;
- **`set(value)`** : define um novo valor para a variável;

#### exemplo

```python
import tkinter as tk

# criando a janela principal
root = tk.Tk()
root.title("Exemplo com StringVar")
root.geometry("300x200")

# criando um StringVar
nome_var = tk.StringVar()

# função que será chamada ao pressionar o botão
def exibir_nome():
    print("Nome:", nome_var.get())  # Obtém o valor da StringVar

# criando um Entry ligado ao StringVar
entry_nome = tk.Entry(root, textvariable=nome_var)
entry_nome.pack(pady=10)

# botão que exibe o valor inserido
btn_mostrar = tk.Button(root, text="Exibir Nome", command=exibir_nome)
btn_mostrar.pack(pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`textvariable=nome_var`** : liga o valor digitado no widget `Entry` à variável `nome_var`; qualquer alteração no `Entry` também modifica o valor da `StringVar`, e vice-versa;
- **`nome_var.get()`** : obtém o valor atual da variável, que neste caso, é o texto inserido no campo de entrada;

### `IntVar`

A variável `IntVar` (Integer Variable) é usada para armazenar valores inteiros. É comumente utilizada em widgets como `Radiobutton` e `Checkbutton`.

- **`get()`** : retorna o valor armazenado;
- **`set(value)`** : define um novo valor para a variável;

#### exemplo

```python
import tkinter as tk

# criando a janela principal
root = tk.Tk()
root.title("Exemplo com IntVar")
root.geometry("300x200")

# criando uma IntVar
opcao_var = tk.IntVar()

# função que exibe a opção selecionada
def exibir_opcao():
    print("Opção selecionada:", opcao_var.get())

# criando Radiobuttons associados ao IntVar
radio1 = tk.Radiobutton(root, text="Opção 1", variable=opcao_var, value=1)
radio1.pack(pady=5)
radio2 = tk.Radiobutton(root, text="Opção 2", variable=opcao_var, value=2)
radio2.pack(pady=5)

# botão que exibe a opção selecionada
btn_exibir = tk.Button(root, text="Exibir Opção", command=exibir_opcao)
btn_exibir.pack(pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`variable=opcao_var`** : liga a variável `IntVar` ao grupo de `Radiobuttons`; o valor da variável é alterado quando um botão de rádio é selecionado;
- **`value=1`, `value=2`** : cada `Radiobutton` tem um valor associado, que será atribuído a `opcao_var` quando o botão for selecionado;

### `DoubleVar`

A variável `DoubleVar` (Double Variable) é usada para armazenar números de ponto flutuante (números decimais).

- **`get()`** : retorna o valor armazenado;
- **`set(value)`** : define um novo valor para a variável;

#### exemplo

```python
import tkinter as tk

# criando a janela principal
root = tk.Tk()
root.title("Exemplo com DoubleVar")
root.geometry("300x200")

# criando uma DoubleVar
valor_var = tk.DoubleVar(value=1.0)

# função para exibir o valor
def exibir_valor():
    print("Valor atual:", valor_var.get())

# etiqueta exibindo o valor inicial
label = tk.Label(root, textvariable=valor_var)
label.pack(pady=10)

# botão para exibir o valor no terminal
btn_exibir = tk.Button(root, text="Exibir Valor", command=exibir_valor)
btn_exibir.pack(pady=10)

# Iniciando o loop de eventos
root.mainloop()
```

- **`DoubleVar()`** : armazena valores flutuantes; é possível inicializar a variável passando um valor como argumento (por exemplo, `1.0`);
- **`textvariable=valor_var`** : o `Label` exibe o valor armazenado na variável, que pode ser atualizado em tempo real;

### `BooleanVar`

A variável `BooleanVar` (Boolean Variable) armazena valores booleanos (`True` ou `False`). É útil para widgets como `Checkbutton`.

- **`get()`** : retorna `True` ou `False`;
- **`set(value)`** : define o valor para `True` ou `False`;

#### exemplo

```python
import tkinter as tk

# criando a janela principal
root = tk.Tk()
root.title("Exemplo com BooleanVar")
root.geometry("300x200")

# criando uma BooleanVar
opcao = tk.BooleanVar()

# função para exibir o estado do checkbox
def exibir_estado():
    print("Checkbox está selecionado?", opcao.get())

# criando o Checkbutton ligado à BooleanVar
check_button = tk.Checkbutton(root, text="Aceitar Termos", variable=opcao)
check_button.pack(pady=10)

# botão que exibe o estado do checkbox
btn_verificar = tk.Button(root, text="Verificar", command=exibir_estado)
btn_verificar.pack(pady=10)

# iniciando o loop de eventos
root.mainloop()
```

- **`variable=opcao`** : liga o estado do `Checkbutton` à variável `BooleanVar`. Quando o botão é marcado, o valor de `opcao` é `True`; caso contrário, é `False`;
- **`opcao.get()`** : retorna o estado atual do `Checkbutton`;

## exercícios variáveis

<details>
<summary>Lista de Exercícios</summary>

1. Exercícios com `StringVar`
    1. **Exibição Simples de Texto** : Crie um programa onde o texto de um `Label` seja controlado por uma `StringVar`. O `Label` deve atualizar automaticamente ao modificar o valor da variável.
    1. **Entrada de Texto Dinâmica** : Crie um programa com um `Entry` e um `Label`. Use uma `StringVar` para conectar o texto do `Entry` ao `Label`, de forma que o `Label` atualize conforme o texto é digitado.
    1. **Combinação de Texto** : Crie dois `Entry` widgets para o primeiro e o último nome. Use duas variáveis `StringVar` para capturar o conteúdo, combiná-los e exibir o nome completo em um `Label`.
    1. **Validação de Entrada** : Crie um `Entry` conectado a uma `StringVar`. Sempre que o texto for modificado, verifique se o valor inserido é um nome válido (sem números) e exiba uma mensagem de erro em um `Label`.
    1. **Alteração de Texto ao Clicar em um Botão** : Crie um `Button` que, quando clicado, altere o valor de uma `StringVar` e atualize um `Label` com o novo valor.
    1. **Atualização Condicional** : Crie dois `Entry` widgets e uma `StringVar` para cada um. Quando ambos os campos forem preenchidos, mostre um `Label` com uma mensagem de boas-vindas usando os dois nomes combinados.
    1. **Concatenação de Valores** : Crie três `Entry` widgets (nome, sobrenome e cidade) com três variáveis `StringVar`. Exiba um `Label` que mostre uma frase concatenando esses valores.
    1. **Troca de Valores entre Widgets** : Crie dois `Entry` widgets com uma `StringVar` para cada. Adicione um botão que troque os valores entre os dois `Entry`.
    1. **Manipulação com Expressões Regulares** : Crie um `Entry` com uma `StringVar` para capturar um número de telefone. Valide o número inserido em tempo real, exibindo uma mensagem de erro se o formato estiver incorreto (por exemplo, "(XX) XXXX-XXXX").
    1. **Interagir com Menu** : Crie um menu suspenso (`OptionMenu`) que exibe uma lista de opções. Use uma `StringVar` para armazenar a opção selecionada e mostre a escolha em um `Label`.
1. Exercícios com `IntVar`
    1. **Exibição Simples de Número** : Crie um `Label` que exibe o valor de uma `IntVar`. Quando o valor da variável mudar, o `Label` deve ser atualizado automaticamente.
    1. **Contador com Botões** : Crie dois `Buttons` para incrementar e decrementar o valor de uma `IntVar`. Mostre o valor atual em um `Label`.
    1. **Controle de Volume Simples** : Crie uma interface que simule um controle de volume com um `Scale` horizontal. Use uma `IntVar` para capturar o valor e exiba o nível de volume em um `Label`.
    1. **Controle de Números Impares e Pares** : Crie dois `Radiobuttons` com valores de uma `IntVar`. Um deve selecionar números ímpares e o outro números pares. Ao clicar, exiba uma lista de números ímpares ou pares em um `Label`.
    1. **Somador de Valores** : Crie três `Entry` widgets, cada um conectado a uma `IntVar`. Mostre a soma dos três valores em um `Label` e atualize o resultado em tempo real.
    1. **Verificador de Par ou Ímpar** : Crie um `Entry` onde o usuário insere um número inteiro. Utilize uma `IntVar` para capturar o valor e exiba em um `Label` se o número é par ou ímpar.
    1. **Seleção de Opções Numéricas** : Crie um conjunto de cinco `Radiobuttons`, cada um representando um número de 1 a 5. Utilize uma `IntVar` para armazenar a seleção e exiba o valor escolhido em um `Label`.
    1. **Atualização Automática de Números** : Crie uma interface com um `Scale` e um `Label`. Use uma `IntVar` para conectar o `Scale` ao `Label` e exiba o valor do `Scale` conforme ele é movido.
    1. **Calculadora de Fatorial** : Crie um `Entry` para inserir um número inteiro e um `Button` que, ao ser clicado, calcule e exiba o fatorial do número usando uma `IntVar`.
    1. **Controle de Alternância com Checkbuttons** : Crie quatro `Checkbuttons` cada um ligado a uma `IntVar`. Adicione um botão que exiba o valor numérico resultante da combinação dos `Checkbuttons` marcados.
1. Exercícios com `DoubleVar`
    1. **Exibição Simples de Valor Decimal** : Crie um `Label` que exibe o valor de uma `DoubleVar`. O `Label` deve ser atualizado automaticamente ao alterar a variável.
    1. **Conversão de Moeda** : Crie um `Entry` onde o usuário insere um valor em dólares. Use uma `DoubleVar` para capturar o valor e exiba a conversão em reais usando uma taxa de câmbio fictícia.
    1. **Calculadora de Desconto** : Crie um `Entry` para inserir o preço original de um produto e um `Scale` para ajustar o percentual de desconto. Use uma `DoubleVar` para capturar esses valores e exibir o preço final com desconto.
    1. **Cálculo de IMC (Índice de Massa Corporal)** : Crie dois `Entry` widgets para o usuário inserir peso (em kg) e altura (em metros). Use `DoubleVar` para capturar esses valores e calcular o IMC, exibindo o resultado em um `Label`.
    1. **Controle de Precisão Decimal** : Crie um `Scale` que permite selecionar valores decimais entre 0.0 e 10.0. Use uma `DoubleVar` para armazenar o valor e exiba-o com 2 casas decimais em um `Label`.
    1. **Conversor de Temperatura** : Crie uma interface com um `Entry` para o usuário inserir uma temperatura em Celsius. Use uma `DoubleVar` para converter o valor para Fahrenheit e exibi-lo em um `Label`.
    1. **Calculadora de Juros Simples** : Crie três `Entry` widgets para inserir o valor principal, taxa de juros anual e número de anos. Use `DoubleVar` para capturar esses valores e calcular o valor total após os juros.
    1. **Medidor de Distância** : Crie uma interface com um `Entry` onde o usuário insere uma distância em quilômetros. Converta esse valor para milhas utilizando uma `DoubleVar` e exiba o resultado em um `Label`.
    1. **Multiplicação Automática** : Crie dois `Entry` widgets para o usuário inserir dois números decimais. Use `DoubleVar` para multiplicá-los e exiba o resultado em um `Label`.
    1. **Simulador de Investimento** : Crie uma interface onde o usuário insere o valor inicial e a taxa de crescimento anual. Use uma `DoubleVar` para calcular o valor acumulado após 5 anos e exibi-lo em um `Label`.
1. Exercícios com `BooleanVar`
    1. **Checkbutton Simples** : Crie um `Checkbutton` que altera uma `BooleanVar`. Exiba o estado atual (True ou False) em um `Label`.
    1. **Botão de Ativação/Desativação** : Crie um `Button` que alterna o valor de uma `BooleanVar` entre True e False a cada clique e atualiza um `Label` com o valor atual.
    1. **Simulação de Lâmpada** : Crie uma interface com um `Checkbutton` que simula uma lâmpada. Quando marcado, exiba "Ligada", e quando desmarcado, exiba "Desligada", usando uma `BooleanVar`.
    1. **Habilitar/Desabilitar Widgets** : Crie um `Checkbutton` que habilita e desabilita um `Entry` widget ao marcar e desmarcar, controlado por uma `BooleanVar`.
    1. **Radiobutton com BooleanVar** : Crie dois `Radiobuttons` com opções "Ativado" e "Desativado". Use uma `BooleanVar` para controlar a seleção e exiba o valor atual em um `Label`.
    1. **Alternância entre Estados** : Crie dois `Buttons`, um para definir uma `BooleanVar` como `True` e outro para definir como `False`. Mostre o valor da variável em um `Label`.
    1. **Botão de Validação** : Crie um `Button` que só possa ser clicado se uma `BooleanVar` for `True`. Controle o estado do botão com um `Checkbutton` ligado a essa variável.
    1. **Simulação de Login** : Crie um sistema de login onde um `Checkbutton` deve ser marcado para lembrar a senha. Use uma `BooleanVar` para controlar a opção.
    1. **Seleção de Opções** : Crie três `Checkbuttons` para representar opções de um questionário. Use `BooleanVar` para cada uma e exiba uma mensagem com as opções selecionadas ao clicar em um botão.
    1. **Aplicação de Estilo** : Crie um `Checkbutton` que ativa ou desativa uma cor de fundo para a janela. Use uma `BooleanVar` para controlar a mudança de cor.

</details>
