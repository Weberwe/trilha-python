# pyinstaller

O [**PyInstaller**](https://pyinstaller.org/en/stable/) é uma ferramenta poderosa que converte programas Python em executáveis, permitindo a distribuição de suas aplicações sem que os usuários precisem instalar o Python.

---

## instalação

Antes de começar a usar o PyInstaller, é preciso instalá-lo. O PyInstaller é compatível com Windows, macOS e Linux.

- Python 3.5 ou superior (incluindo o Python 3.11);
- `pip` instalado (gerenciador de pacotes do Python);

**Passos para instalação**

1. **Verificando a instalação do Python :** antes de tudo, certifique-se de que o Python está corretamente instalado e configurado no seu sistema. Execute no terminal ou prompt de comando:

    ```bash
    python --version
    ```

    Isso deve retornar a versão do Python instalada.

1. **Instalando o PyInstaller com `pip` :** No terminal (Linux/macOS) ou no prompt de comando (Windows), execute o comando:

    ```bash
    pip install pyinstaller
    ```

    Esse comando irá baixar e instalar o PyInstaller, juntamente com suas dependências.

1. **Verificando a instalação :** Após a instalação, verifique se o PyInstaller foi instalado corretamente executando o seguinte comando:

    ```bash
    pyinstaller --version
    ```

    Isso deve exibir a versão do PyInstaller instalada, confirmando que tudo está correto.

---

### como usar

1. Gerando um executável simples

    Para gerar um executável a partir de um script Python, basta usar o comando básico do PyInstaller:

    - No terminal ou prompt de comando, navegue até o diretório onde seu script Python está localizado. Por exemplo, se o arquivo `meu_programa.py` estiver na pasta `projetos`, pode usar o comando :

    ```bash
    cd /caminho/para/pasta/projetos
    ```

    - Agora, execute o seguinte comando para gerar o executável :

    ```bash
    pyinstaller meu_programa.py
    ```

    O PyInstaller irá gerar várias pastas e arquivos, incluindo o executável dentro da pasta `dist`. O comando acima cria uma pasta chamada `dist/meu_programa` contendo o executável, juntamente com as dependências necessárias.

1. Executável sem console (somente GUI)

    Se o programa tem uma interface gráfica (GUI), e não quer que o console do terminal apareça ao executá-lo, use o parâmetro `--noconsole` ou `--windowed` :

    ```bash
    pyinstaller --noconsole meu_programa.py
    ```

    Isso cria um executável que não abre o terminal ao ser executado, ideal para aplicações que usam bibliotecas como `tkinter`, `PyQt` ou `Kivy`.

1. Gerar um único arquivo executável

    Por padrão, o PyInstaller cria uma pasta com o executável e outros arquivos de dependência. Se quiser que tudo seja compactado em um único arquivo, use a opção `--onefile`:

    ```bash
    pyinstaller --onefile meu_programa.py
    ```

    Isso cria um único executável na pasta `dist`, o que facilita a distribuição do seu programa.

1. Incluir arquivos adicionais

    Se o programa precisa de arquivos adicionais, como imagens, bases de dados ou configurações, pode-se incluir esses arquivos no executável utilizando a opção `--add-data`.

    No Windows, o comando seria :

    ```bash
    pyinstaller --onefile --add-data "imagem.png;." meu_programa.py
    ```

    No Linux/macOS, use :

    ```bash
    pyinstaller --onefile --add-data "imagem.png:." meu_programa.py
    ```

    Isso garante que o arquivo `imagem.png` será incluído na pasta onde o executável será executado.

1. Especificar o ícone do executável

    Se deseja personalizar o ícone do seu executável, use a opção `--icon` para especificar um arquivo `.ico` (Windows) ou `.icns` (macOS) :

    ```bash
    pyinstaller --onefile --icon=meu_icone.ico meu_programa.py
    ```

1. Arquivo de especificação (spec)

    O PyInstaller gera um arquivo `.spec` quando cria um executável. Esse arquivo pode ser editado manualmente para customizar ainda mais o processo de criação do executável. Pode-se reutilizar o arquivo `.spec` para gerar o executável sem precisar escrever novamente todos os parâmetros:

    ```bash
    pyinstaller meu_programa.spec
    ```

1. Excluindo bibliotecas

    Se o seu executável estiver muito grande, pode-se excluir algumas bibliotecas desnecessárias usando a opção `--exclude-module` :

    ```bash
    pyinstaller --onefile --exclude-module tkinter meu_programa.py
    ```

---

### estrutura dos arquivos gerados

Após a execução do PyInstaller, os seguintes diretórios e arquivos serão criados :

- **`build/`** : diretório temporário usado durante o processo de compilação;
- **`dist/`** : contém o executável gerado. Se usou a opção `--onefile`, o arquivo único estará aqui;
- **`meu_programa.spec`** : arquivo de especificação que descreve como o executável será gerado;

Pode-se limpar os diretórios temporários (como o `build/`) após a compilação, se desejar.

---

### exemplos práticos

1. **Exemplo 1 :** criar um executável de um script simples

    Suponha que tenha o seguinte script Python chamado `hello.py` :

    ```python
    # hello.py
    print("Olá, mundo!")
    ```

    Para gerar o executável desse script, basta executar:

    ```bash
    pyinstaller hello.py
    ```

    Isso vai gerar a estrutura de diretórios e o executável em `dist/hello`.

1. **Exemplo 2 :** gerar um executável GUI sem console

    Se tiver uma aplicação com interface gráfica, como este exemplo usando `tkinter`:

    ```python
    # gui_app.py
    import tkinter as tk

    root = tk.Tk()
    root.title("Aplicação GUI")

    label = tk.Label(root, text="Bem-vindo à aplicação!")
    label.pack()

    root.mainloop()
    ```

    Use o seguinte comando para gerar um executável sem console:

    ```bash
    pyinstaller --noconsole gui_app.py
    ```

1. **Exemplo 3 :** gerar um único arquivo com um ícone

    Se quiser gerar um único executável com um ícone personalizado, execute:

    ```bash
    pyinstaller --onefile --icon=meu_icone.ico meu_programa.py
    ```

## exercícios

Como exercício, crie executáveis de scripts criados anteriormente em outras atividades.
