# git

O [Git](https://git-scm.com) é um **sistema de controle de versão distribuído**, amplamente utilizado no desenvolvimento de software para rastrear mudanças em arquivos e coordenar o trabalho em equipe. Ele permite que desenvolvedores colaborem no mesmo projeto de forma eficiente, mantendo um histórico completo de todas as alterações realizadas no código ao longo do tempo.

Criado por [**Linus Torvalds**](https://pt.wikipedia.org/wiki/Linus_Torvalds) em 2005 para ajudar no desenvolvimento do kernel do Linux, o Git se tornou um dos sistemas mais populares devido à sua eficiência, flexibilidade e robustez. Hoje, ele é essencial para o desenvolvimento de software, seja em projetos individuais ou em grandes equipes.

## o que é controle de versão?

O **controle de versão** é uma prática essencial no desenvolvimento de software que ajuda a gerenciar as alterações feitas no código ao longo do tempo. Ele permite que você acompanhe quem fez mudanças, quando essas mudanças foram feitas e por quê. Também possibilita o retorno a versões anteriores do código caso algo dê errado ou seja necessário comparar diferentes estados do projeto.

Existem dois tipos principais de controle de versão:

1. **controle de versão local** : o desenvolvedor mantém versões diferentes do código em pastas locais no seu computador, o que não é eficiente para projetos grandes ou colaborativos;
1. **controle de versão centralizado** : um único servidor central armazena todas as versões dos arquivos e os desenvolvedores fazem "check-out" para trabalhar localmente; o problema é que esse modelo cria dependência do servidor central;
1. **controle de versão distribuído** : nesse modelo, usado pelo git, cada colaborador tem uma cópia completa do repositório, incluindo o histórico de todas as alterações; isso permite maior segurança e flexibilidade, pois o trabalho continua mesmo se o servidor central estiver inacessível;

---

## como o git funciona

O Git usa três principais áreas para gerenciar o código:

1. **diretório de trabalho (working directory)** : é onde você faz as alterações nos arquivos de forma local;
1. **área de preparação (staging area)** : aqui, você prepara as alterações que deseja confirmar no histórico do projeto; é como uma "zona de rascunho" antes de salvar as mudanças;
1. **repositório local (local repository)** : é onde o git armazena o histórico das suas alterações confirmadas (commits); cada colaborador tem seu próprio repositório local;

O Git também permite trabalhar com **repositórios remotos**, hospedados em servidores como o GitHub, GitLab ou Bitbucket, para facilitar a colaboração em equipe. A comunicação com esses servidores permite **sincronizar** as mudanças feitas por diferentes desenvolvedores.

---

## principais vantagens do git

1. **distribuído** : cada desenvolvedor possui uma cópia completa do repositório, permitindo que se trabalhe off-line e com maior segurança;
1. **rápido e eficiente** : git é otimizado para gerenciar grandes quantidades de código com muitas ramificações (branches) e mesclagens (merges) de forma rápida;
1. **controle de branches** : branches no git são muito leves, o que facilita o desenvolvimento de novos recursos isoladamente antes de integrá-los ao código principal;
1. **histórico completo** : o git mantém o histórico detalhado de todas as mudanças, permitindo voltar no tempo e entender o motivo de uma alteração;
1. **colaboração facilitada** : com o git, várias pessoas podem trabalhar no mesmo projeto simultaneamente, sem que o código de uma interfira no trabalho de outra;

---

## github

O GitHub é uma plataforma de desenvolvimento colaborativo que aloja projetos na nuvem utilizando o sistema de controle de versões chamado Git. A plataforma ajuda os desenvolvedores a armazenar e administrar o código e faz o registro de mudanças. Geralmente o código é aberto, o que permite realizar projetos compartilhados e manter o acompanhamento detalhado de seu progresso. A plataforma GitHub também funciona como rede social, conectando os desenvolvedores com os usuários. Como usuário, você pode descarregar programas ou aplicativos, e da mesma maneira, pode colaborar com seu desenvolvimento oferecendo melhorias e discutindo as questões que interessam nos fóruns temáticos.

### criando uma conta no github

Criar uma conta no GitHub é um processo simples e rápido.

1. **acesse o site do github** : abra seu navegador e vá para o site oficial do github: [github.com](https://github.com);
1. **iniciar o processo de criação da conta** : na página inicial do github, clique no botão **"sign up"** ou **"sign up for github"** (inscrever-se) no canto superior direito da tela;
1. **preencher as informações de cadastro** : você será direcionado para a página de cadastro, onde deverá preencher algumas informações como **username**, **e-mail** e **senha**; uma vez preenchido, clique no botão **"continue"**;
1. **verificar a conta** : github solicitará que você complete um teste simples de captcha para verificar que você não é um robô; complete o captcha e clique em **"create account"** (criar conta);
1. **confirmar o e-mail** : após criar a conta, o github enviará um e-mail de confirmação para o endereço fornecido;
1. **escolher um plano** : o github oferece dois planos: um **gratuito** e um **pago**; para começar, escolha o plano **gratuito** clicando na opção correspondente;
1. **configurar sua conta** : depois de confirmar sua conta, você será direcionado ao painel principal do github, onde poderá configurar algumas preferências iniciais, como adicionar uma foto de perfil e personalizar suas configurações;

Agora que sua conta foi criada, você pode começar a usar o GitHub para **criar repositórios**, **colaborar com outros desenvolvedores**, **clonar e fazer fork de repositórios**.

### criando um repositório

Uma vez que a conta está criada, é a hora de criar um repositório.

Para isso :

1. **acessar o github**

   - entre no [site do github](https://github.com/) e faça login na sua conta (caso ainda não esteja logado);

2. **criar um novo repositório**

   - no canto superior direito, clique no ícone “+” e selecione **New repository** (Novo repositório);

3. **definir as informações do repositório**

   - **add .gitignore** : você pode escolher um template de `.gitignore`, que especifica arquivos que o git deve ignorar (por exemplo, arquivos temporários ou gerados automaticamente);
   - **choose a license** : escolha uma licença para seu projeto, caso necessário; ela define os termos sob os quais outros podem usar seu código;
   - **description (opcional)** : adicione uma breve descrição sobre o projeto;
   - **initialize this repository with a readme** : se você marcar esta opção, o github criará um arquivo `README.md` automaticamente. ele é útil para descrever o projeto e será exibido na página principal do repositório;
   - **owner** : escolha se o repositório será criado na sua conta pessoal ou em uma organização (caso faça parte de alguma);
   - **public ou private** : escolha se o repositório será público (qualquer pessoa pode ver) ou privado (somente você e os colaboradores autorizados podem acessá-lo);
   - **repository name** : defina um nome único e descritivo para o repositório (ex: `silver-enigma`);

4. **criar o repositório**:

    - clique no botão **Create repository** (Criar repositório). Agora, o seu repositório está criado e pronto para uso no GitHub;

---

## instalando o git

O Git pode ser instalado facilmente em computadores Windows, macOS e Linux. Cada sistema possui métodos específicos para instalação.

### instalar git no windows

1. **baixar o instalador**

   - Acesse o site oficial do Git: [git-scm.com](https://git-scm.com/) e clique no botão **Download for Windows**. Isso fará o download do instalador mais recente para Windows.

1. **executar o instalador**

   - Após o download, execute o arquivo instalador.

1. **configurar a instalação**

   - Durante o processo de instalação, você verá várias opções. Para a maioria dos usuários, as opções padrão são suficientes. Algumas opções que podem aparecer:
      - **select destination location** : escolha onde deseja instalar o git. o padrão geralmente é `c:\program files\git`;
      - **select components** : algumas opções incluem instalar atalhos, associar arquivos `.git` ao git e outras configurações avançadas. recomenda-se manter as opções padrão;
      - **editor para commits** : você pode escolher qual editor de texto será usado por padrão ao editar mensagens de commit (o padrão é o vim, mas você pode selecionar outro como o vscode ou notepad++);
      - **adjusting path environment** : escolha a opção **git from the command line and also from 3rd-party software**, que permite usar o git em qualquer terminal no windows;
      - **configurações de https** : recomenda-se manter a opção padrão de usar a biblioteca `openssl` para lidar com https;

1. **concluir a instalação**

   - continue seguindo as instruções do instalador até a finalização. Selecione a opção de iniciar o **Git Bash** ao final, se desejar;

1. **verificar a instalação**
   - após a instalação, abra o **Git Bash** ou o **Prompt de Comando** e execute o comando abaixo para verificar a versão instalada:
      ```bash
      git --version
      ```

### instalar git no macos

Existem algumas maneiras de instalar o Git no macOS, incluindo a instalação via Homebrew ou diretamente pelo site oficial.

#### método 1: usando homebrew (recomendado)

1. **instalar o homebrew** (se você ainda não o tiver)

   - Homebrew é um gerenciador de pacotes para macOS que facilita a instalação de software. Para instalar, abra o **Terminal** e execute o comando:
      ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```

1. **instalar o git**

   - Com o Homebrew instalado, você pode instalar o Git com o seguinte comando:
      ```bash
      brew install git
      ```

1. **verificar a instalação**

   - Após a instalação, verifique a versão do Git com:
      ```bash
      git --version
      ```

#### método 2: usando xcode command line tools

Se você não quiser instalar o Homebrew, outra opção é instalar o Git usando as ferramentas de linha de comando do Xcode (que já incluem o Git).

1. **instalar as ferramentas do xcode**

   - No **Terminal**, execute:
      ```bash
      xcode-select --install
      ```

1. **verificar a instalação**

   - Quando a instalação estiver concluída, verifique se o Git foi instalado:
      ```bash
      git --version
      ```

#### método 3: baixar do site oficial

1. **baixar o instalador**

   - Acesse [git-scm.com](https://git-scm.com/) e baixe o instalador do Git para macOS.

1. **executar o instalador**

   - Siga as instruções do instalador e finalize o processo.

### instalar git no linux

Em sistemas Linux, o Git pode ser instalado diretamente usando o gerenciador de pacotes da sua distribuição. Abaixo estão os comandos para as distribuições mais populares.

#### instalar git no ubuntu e debian

Todos os comandos abaixo deverão ser realizados no emulador shell que estiver sendo usado.

1. **atualizar o gerenciador de pacotes**
   ```bash
   sudo apt update
   ```

1. **instalar o git**
   ```bash
   sudo apt install git
   ```

1. **verificar a instalação**
   ```bash
   git --version
   ```

#### instalar git no fedora

1. **instalar o git**
   ```bash
   sudo dnf install git
   ```

1. **verificar a instalação**
   ```bash
   git --version
   ```

#### instalar git no arch linux

1. **instalar o git**
   ```bash
   sudo pacman -S git
   ```

1. **verificar a instalação**
   ```bash
   git --version
   ```

---

## `git config`

O comando `git config` permite que você configure várias opções para o Git. Entre as mais comuns estão as configurações de nome de usuário, email e editor de texto. Essas configurações podem ser definidas em três níveis diferentes:

1. **nível de sistema** (`--system`) : afeta todos os usuários no sistema;
1. **nível global** (`--global`) : afeta apenas o usuário atual, aplicando-se a todos os repositórios que esse usuário acessar;
1. **nível local** (`--local`) : afeta apenas o repositório atual;

### estrutura dos arquivos de configuração

- **nível de sistema** : geralmente, está localizado em `/etc/gitconfig` (linux/macos) ou no diretório de instalação do git (windows);
- **nível global** : o arquivo de configuração é armazenado no diretório home do usuário, geralmente em `~/.gitconfig` ou `~/.config/git/config` (linux/macos) ou `c:\users\seunome\.gitconfig` (windows);
- **nível local** : cada repositório git possui um arquivo `.git/config` que armazena as configurações locais;

### `user.name` e `user.email`

Você pode configurar o nome de usuário e o email em qualquer um dos três níveis.

#### nível de sistema

Essa configuração aplica-se a todos os usuários e repositórios no sistema. Para fazer isso, você precisa ter permissões de administrador.

- **nome de usuário**
   ```bash
   git config --system user.name "Seu Nome"
   ```
- **email**
   ```bash
   git config --system user.email "seu-email@exemplo.com"
   ```

#### nível global

Essa configuração se aplica ao usuário atual e a todos os repositórios que ele acessar.

- **nome de usuário**
   ```bash
   git config --global user.name "Seu Nome"
   ```
- **email**
   ```bash
   git config --global user.email "seu-email@exemplo.com"
   ```

#### **nível local (para um repositório específico)**

Essa configuração se aplica apenas ao repositório em que você está trabalhando.

- **nome de usuário**
   ```bash
   git config --local user.name "Seu Nome"
   ```
- **email**
   ```bash
   git config --local user.email "seu-email@exemplo.com"
   ```

### configurando o editor de texto

Você pode configurar o editor de texto que o Git abrirá para você editar mensagens de commit, entre outras coisas. Por padrão, o Git usa o `vim`, mas você pode configurar editores como o `nano`, `VSCode`, ou qualquer outro de sua preferência.

> [!NOTE]
> Para as próximas configurações será usado apenas o nível `--global`, mas o mesmo processo pode aplicado para os demais `--system` e `--local `;

- **para definir o editor no nível global**
   ```bash
   git config --global core.editor "nano"
   ```

   Ou, para VSCode:

   ```bash
   git config --global core.editor "code --wait"
   ```

### visualizar as configurações

Você pode visualizar as configurações em cada nível com os seguintes comandos:

```bash
git config --system --list
git config --global --list
git config --local --list
```

## `git clone`

O comando `git clone` é utilizado para fazer uma cópia local de um repositório remoto, como os hospedados no GitHub. Esse comando copia o histórico de commits e arquivos do repositório remoto para o seu computador, permitindo que você comece a trabalhar no código localmente.

```bash
git clone <URL do repositório>
```

- **URL do repositório** : é o link do repositório no GitHub (ou outro servidor Git). Ele pode ser fornecido usando diferentes protocolos, como HTTPS ou SSH;

### clonando um repositório do github

1. **Obter a URL do repositório no GitHub**

   - acesse o GitHub e vá até o repositório que deseja clonar;
   - clique no botão verde **Code** (Código) e, em seguida, copie a URL. Você verá três opções:
     - **HTTPS** : `https://github.com/usuario/repo.git`
     - **SSH** : `git@github.com:usuario/repo.git` (necessário configurar chaves SSH)
     - **GitHub CLI** : `gh repo clone usuario/repo`

   para usuários que não configuraram o SSH, é mais simples usar a URL HTTPS.

2. **Abrir o terminal ou prompt de comando**

   - no seu computador, abra o **Terminal** (Linux/macOS) ou **Prompt de Comando** / **Git Bash** (Windows);

3. **Navegar até o diretório onde deseja clonar o repositório**

   - Use o comando `cd` para navegar até o diretório desejado:

     ```bash
     cd /caminho/para/o/diretorio
     ```

4. **Executar o comando `git clone`**

   - Com a URL copiada do GitHub, use o comando `git clone` para baixar o repositório. Exemplo para clonar via HTTPS:

     ```bash
     git clone https://github.com/usuario/repo.git
     ```

   Isso criará uma cópia local do repositório dentro de um diretório chamado `repo`.

5. **Navegar até o repositório clonado**

   - Após a clonagem, vá para o diretório criado com o comando:

     ```bash
     cd repo
     ```

Agora você tem uma cópia local do repositório e pode começar a trabalhar no projeto.

### opções comuns do comando `git clone`

- **Clonar em um diretório diferente** : Você pode especificar um nome diferente para o diretório local onde o repositório será clonado:

   ```bash
   git clone https://github.com/usuario/repo.git novo-diretorio
   ```

  Isso criará um diretório chamado `novo-diretorio` em vez de `repo`.

- **Clonar um branch específico** : Para clonar apenas um branch específico (em vez do branch `main` por padrão):

   ```bash
   git clone --branch nome-do-branch https://github.com/usuario/repo.git
   ```

- **Clonar sem o histórico completo** (shallow clone): Se você não precisar do histórico completo de commits (por exemplo, para otimizar o espaço), pode fazer um **clone raso** (shallow):

   ```bash
   git clone --depth 1 https://github.com/usuario/repo.git
   ```

   Isso clona apenas a versão mais recente do repositório, sem os commits anteriores.

### clonando via ssh

Se você configurou o SSH para autenticação com o GitHub, você pode usar a URL SSH para clonar repositórios. Isso evita que você precise digitar seu nome de usuário e senha em cada operação.

Exemplo de clonagem via SSH:

```bash
git clone git@github.com:usuario/repo.git
```

Para configurar o SSH com o GitHub, você pode seguir o guia oficial de configuração: [GitHub SSH keys guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## `git status`

O comando `git status` exibe o status do repositório em termos de arquivos. Ele mostra informações sobre quais arquivos foram modificados, quais estão prontos para serem commitados e quais ainda precisam ser versionados.

```bash
git status
```

- Exibe se há **arquivos modificados** que ainda não foram adicionados ao staging (área de preparação para commit).
- Informa se há **arquivos no stage** (prontos para commit).
- Mostra se há **arquivos novos não rastreados** (não adicionados ao controle de versão ainda).
- Informa o **branch atual** no qual você está trabalhando.

**Exemplo:**

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   arquivo1.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	novo_arquivo.txt
```

**Interpretação:**
- **Modified**: O arquivo `arquivo1.txt` foi modificado, mas ainda não está no stage.
- **Untracked files**: O arquivo `novo_arquivo.txt` é novo e ainda não está sob controle de versão.

---

## `git log`

O comando `git log` exibe o histórico de commits do repositório, mostrando informações detalhadas sobre cada commit.

```bash
git log
```

- Exibe a **lista de commits**, incluindo o hash (identificador único) do commit, o autor, a data e a mensagem de commit.
- Você pode ver todo o histórico do projeto desde o início, inclusive quem fez as alterações e quando.

**Exemplo:**

```bash
$ git log
commit d74b4c63f12848a4ab68495b87bcb517c87ae562 (HEAD -> main)
Author: João Silva <joao@exemplo.com>
Date:   Mon Oct 23 10:15:10 2024 -0300

    Corrige erro no arquivo principal

commit 837ea1b6f2f45c7e91e147bbcb1a3bc0e9b7c2ba
Author: Maria Oliveira <maria@exemplo.com>
Date:   Sun Oct 22 15:30:25 2024 -0300

    Adiciona nova funcionalidade ao projeto
```

**Opções úteis:**

- **`git log --oneline`**: Exibe o histórico de commits em uma única linha por commit, mostrando o hash e a mensagem resumida.

   ```bash
   git log --oneline
   ```

   Exemplo:

   ```bash
   d74b4c6 Corrige erro no arquivo principal
   837ea1b Adiciona nova funcionalidade ao projeto
   ```

- **`git log -p`**: Mostra os detalhes de cada commit, incluindo as alterações de código feitas.

   ```bash
   git log -p
   ```

- **`git log --author="Nome"`**: Filtra os commits por um autor específico.

   ```bash
   git log --author="Maria Oliveira"
   ```

- **`git log --since="2024-10-01"`**: Exibe os commits feitos desde uma data específica.

   ```bash
   git log --since="2024-10-01"
   ```

---

## `git diff`

O comando `git diff` exibe as diferenças entre os arquivos no repositório. Ele compara o conteúdo entre diferentes estados, mostrando exatamente o que foi alterado linha por linha.

```bash
git diff
```

- **Exibe diferenças entre o working directory (diretório de trabalho) e o stage**: Mostra as mudanças que foram feitas no diretório de trabalho, mas que ainda não foram adicionadas ao stage.

- **Comparar o stage com o último commit**: Se você já adicionou arquivos ao stage, mas ainda não fez commit, você pode usar `git diff --staged` para ver as diferenças entre o stage e o último commit.

**Exemplos:**

- **Ver diferenças entre o working directory e o stage**:

   ```bash
   git diff
   ```

   Exemplo de saída:

   ```diff
   diff --git a/arquivo1.txt b/arquivo1.txt
   index 9daeafb..47b3c43 100644
   --- a/arquivo1.txt
   +++ b/arquivo1.txt
   @@ -1,2 +1,2 @@
   -linha antiga
   +linha nova
   ```

   Isso mostra que a linha `linha antiga` foi modificada para `linha nova`.

- **Ver diferenças entre o stage e o último commit**:

   ```bash
   git diff --staged
   ```

- **Comparar dois commits**:

   ```bash
   git diff commit1 commit2
   ```

   Isso mostrará as diferenças entre dois commits específicos.

---

## `git add`

O comando `git add` adiciona mudanças no diretório de trabalho (arquivos modificados, novos ou removidos) à **área de staging** (também chamada de área de preparação). A área de staging é como uma "prévia" das mudanças que serão incluídas no próximo commit.

```bash
git add <arquivo>
```

Ou, para adicionar todos os arquivos:

```bash
git add .
```

- Adiciona um ou mais arquivos à área de staging, preparando-os para o commit.
- Você pode adicionar arquivos específicos, ou todos os arquivos modificados de uma vez.

**Exemplos:**

- **Adicionar um arquivo específico**:

   ```bash
   git add arquivo.txt
   ```

   Isso prepara o arquivo `arquivo.txt` para o commit.

- **Adicionar todos os arquivos modificados ou novos**:

   ```bash
   git add .
   ```

   O ponto (`.`) significa "todos os arquivos no diretório atual". Isso adiciona todas as mudanças (novos arquivos, arquivos modificados e até mesmo arquivos excluídos) ao staging.

- **Adicionar arquivos com um padrão específico** (por exemplo, todos os arquivos `.txt`):

   ```bash
   git add *.txt
   ```

---

## `git commit`

O comando `git commit` salva as mudanças na área de staging no histórico do repositório. Um commit é um "instantâneo" do estado dos arquivos naquele momento, com uma mensagem de log descrevendo o que foi feito.

```bash
git commit -m "Mensagem do commit"
```

Ou, se você quiser que o Git abra um editor de texto para escrever uma mensagem de commit mais detalhada:

```bash
git commit
```

- Salva todas as mudanças que estão na área de staging como um novo commit.
- Inclui uma mensagem descritiva sobre o que foi alterado, o que ajuda a rastrear o histórico de alterações no projeto.

**Exemplos:**

- **Fazer commit com uma mensagem**:

   ```bash
   git commit -m "Corrige bug no arquivo principal"
   ```

   Isso cria um commit com a mensagem `"Corrige bug no arquivo principal"`.

- **Fazer commit de todos os arquivos modificados e adicionar uma mensagem** (combinando `git add` e `git commit` em um único comando):

   ```bash
   git commit -a -m "Atualiza os arquivos de configuração"
   ```

   A opção `-a` adiciona automaticamente todos os arquivos modificados (mas não os novos arquivos) ao commit. Ainda assim, arquivos novos precisam ser adicionados manualmente com `git add`.

**Mensagens de Commit:**

- A mensagem de commit deve ser descritiva e clara. Ela ajuda a entender o que foi feito no projeto sem a necessidade de inspecionar diretamente o código.
- Exemplo de boas mensagens de commit:
   - `"Adiciona funcionalidade de login"`
   - `"Corrige bug na função de cálculo de impostos"`
   - `"Remove código desnecessário da classe de autenticação"`

---

## `git push`**

O comando `git push` é usado para **enviar os commits do seu repositório local** para um repositório remoto. Ele transfere o histórico de commits e as alterações feitas nos arquivos para o repositório remoto, como o GitHub.

```bash
git push <nome-remoto> <nome-branch>
```

- **`<nome-remoto>`**: Geralmente, o nome do repositório remoto é `origin`, que é o nome padrão quando você clona um repositório. Mas pode ser qualquer nome que você tenha dado ao repositório remoto.
- **`<nome-branch>`**: É o nome do branch que você deseja enviar (geralmente, `main` ou `master`).

- Envia os commits que estão no seu repositório local, mas que ainda não estão no repositório remoto.
- Atualiza o branch correspondente no repositório remoto para refletir o estado atual do seu repositório local.

**Exemplo:**

1. Você fez alterações no branch `main` local e as comitou:

   ```bash
   git commit -m "Corrige bug no arquivo principal"
   ```

2. Agora, você deseja enviar essas alterações para o GitHub (repositório remoto):

   ```bash
   git push origin main
   ```

   - Isso enviará as alterações para o repositório remoto nomeado `origin`, no branch `main`.

**Dicas úteis:**

- Se você já configurou o repositório remoto e está trabalhando no branch principal (por exemplo, `main` ou `master`), você pode simplesmente usar:

   ```bash
   git push
   ```

- Se este for o primeiro push para um novo branch no repositório remoto, você precisará usar:

   ```bash
   git push -u origin <nome-branch>
   ```

   A opção `-u` define o branch local para acompanhar automaticamente o branch remoto, de modo que em futuros `git push` ou `git pull`, o branch correto seja atualizado sem precisar especificá-lo manualmente.

---

## `git pull`

O comando `git pull` é usado para **trazer as alterações de um repositório remoto** para o seu repositório local. Ele faz o download das mudanças (commits, arquivos novos, modificados ou deletados) do repositório remoto e as incorpora ao seu branch local.

```bash
git pull <nome-remoto> <nome-branch>
```

- **`<nome-remoto>`**: Assim como no `git push`, geralmente é `origin`.
- **`<nome-branch>`**: O branch do qual você deseja puxar as alterações (por exemplo, `main` ou `develop`).

- O `git pull` é, na verdade, uma combinação de dois comandos:
   1. **`git fetch`**: Baixa as alterações do repositório remoto.
   2. **`git merge`**: Incorpora essas alterações no seu branch local.

   Em resumo, o `git pull` baixa as alterações mais recentes do repositório remoto e faz a fusão dessas alterações com o seu branch atual.

**Exemplo:**

1. Você deseja atualizar seu branch local `main` com as últimas alterações que foram feitas no GitHub por outros colaboradores. Use:

   ```bash
   git pull origin main
   ```

   Isso trará as últimas mudanças do branch `main` no repositório remoto `origin` e as incorporará ao seu branch `main` local.

**Dicas úteis:**

- Se o seu branch local já está rastreando um branch remoto (o que é o caso normal para o branch `main`), você pode simplesmente rodar:

   ```bash
   git pull
   ```

- **Conflitos de merge**: Às vezes, ao fazer um `git pull`, você pode enfrentar **conflitos de merge**. Isso ocorre quando você e outra pessoa modificaram a mesma parte do código. O Git não consegue mesclar automaticamente as alterações e pede que você resolva os conflitos manualmente. Após resolver os conflitos, você faz o commit das alterações resultantes da fusão.

---

## `git branch`

O comando `git branch` é usado para **listar, criar, renomear ou deletar branches** (ramificações) no Git. Branches permitem que você trabalhe em diferentes funcionalidades ou correções de forma independente, sem interferir no código principal.

- Para **listar** branches:

   ```bash
   git branch
   ```

- Para **criar** um novo branch:

   ```bash
   git branch <nome-branch>
   ```

- Para **deletar** um branch:

   ```bash
   git branch -d <nome-branch>
   ```

- Para **renomear** um branch:

   ```bash
   git branch -m <novo-nome-branch>
   ```

**Exemplos:**

- **Listar branches**: Para ver os branches disponíveis no repositório e o branch atual (indicado por um asterisco):

   ```bash
   git branch
   ```

   Saída possível:

   ```
   * main
      feature-nova
      bugfix
   ```

   Isso mostra que você está atualmente no branch `main`, e há outros branches chamados `feature-nova` e `bugfix`.

- **Criar um novo branch** chamado `feature-nova`:

   ```bash
   git branch feature-nova
   ```

   Isso cria o branch, mas você ainda não está trabalhando nele (não fez o "checkout").

- **Deletar um branch** chamado `bugfix`:

   ```bash
   git branch -d bugfix
   ```

   Deleta o branch `bugfix` se ele já foi integrado e não tem mais commits não mesclados.

---

## `git checkout`

O comando `git checkout` é usado para **mudar de branch** ou até mesmo **criar um novo branch e mudar para ele**. Ele também pode ser usado para restaurar arquivos ou commits anteriores, mas aqui focaremos no uso para manipulação de branches.

- Para **mudar para um branch existente**:

   ```bash
   git checkout <nome-branch>
   ```

- Para **criar um novo branch** e automaticamente mudar para ele:

   ```bash
   git checkout -b <nome-branch>
   ```

**Exemplos:**

- **Mudar para o branch `feature-nova`**:

   ```bash
   git checkout feature-nova
   ```

   Isso faz com que você passe a trabalhar no branch `feature-nova`. Agora, qualquer alteração ou commit será feito nesse branch.

- **Criar e mudar para um novo branch** chamado `hotfix`:

   ```bash
   git checkout -b hotfix
   ```

   Isso cria o branch `hotfix` e automaticamente troca para ele, economizando um passo.

---

## `git merge`

O comando `git merge` é usado para **combinar mudanças de um branch em outro**. Geralmente, você faz merge de um branch de desenvolvimento (como `feature-nova`) no branch principal (como `main`) após concluir uma nova funcionalidade ou correção de bug.

```bash
git merge <nome-branch>
```

- Combina as alterações do `<nome-branch>` no branch **atual**.
- O branch do qual você está fazendo o merge permanece inalterado, mas o branch atual recebe todas as alterações.

**Exemplos:**

1. **Situação típica de merge**:
   - Você está no branch `main` e quer integrar as mudanças feitas no branch `feature-nova`.

2. Primeiro, mude para o branch `main`:

   ```bash
   git checkout main
   ```

3. Agora, faça o merge do branch `feature-nova` no `main`:

   ```bash
   git merge feature-nova
   ```

   Isso integra as mudanças do branch `feature-nova` ao branch `main`.

#### Tipos de Merge:

- **Fast-forward**: Se o branch principal (`main`) não teve alterações desde a criação do branch `feature-nova`, o Git simplesmente move o ponteiro do branch `main` para incluir as mudanças. É um merge linear.

- **Merge com commit de merge**: Se o branch principal (`main`) e o branch `feature-nova` têm diferentes commits desde o último ponto em comum, o Git faz um **merge de três vias**, e cria um commit especial chamado **commit de merge**.

#### Conflitos de Merge:

- Se o Git encontrar alterações conflitantes (por exemplo, se você e outro colaborador modificaram a mesma parte de um arquivo), ele não poderá completar o merge automaticamente.
- Nesse caso, você terá que **resolver os conflitos manualmente** e então fazer um commit das mudanças resultantes. O Git marcará os arquivos que precisam de resolução, e você verá algo assim dentro dos arquivos conflitantes:

   ```
   <<<<<<< HEAD
   código no branch atual
   =======
   código no branch feature-nova
   >>>>>>> feature-nova
   ```

   Você precisa escolher qual código manter, resolver o conflito, salvar o arquivo, adicionar (`git add`) e fazer o commit.
