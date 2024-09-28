# atividade aula

Abaixo há a atividade que deverá ser realizada e entregue no começo de aula do dia 30/10, na próxima segunda-feira.
Ela servirá como aula não presencial do dia 26/10/2024. A não entrega da atividade implicará em falta no dia.

O código deverá ser desenvolvido em apenas um módulo.

Sua complexidade foi pensada para ser desenvolvida em uma aula de 4h.

## agenda eletrônica

Agendas eletrônicas eram dispositivos portáteis que armazenavam digitalmente informações como contatos, compromissos, tarefas e anotações, substituindo as agendas de papel tradicionais. Elas ofereciam recursos como calendário, calculadora, jogos e, em alguns casos, até mesmo conexão com outros dispositivos. Eram populares antes da era dos smartphones, que acabaram incorporando suas funções e tornando-as obsoletas.

## tarefa

Desenvolva uma agenda eletrônica pagar guardar apenas os contatos.
Use apenas os conhecimentos adquiridos em aula.

## estrutura

A Agenda Eletrônica deverá ser criada segundo os critérios abaixo :
- uma classe `Agenda` que vai ter as seguintes funcionalidades :
    - adicionar contato;
    - editar contato;
    - apagar contato;
    - listar todos os contatos;
    - listar contatos semelhantes ao nome que for buscado :
        - exemplo : buscar por *carlos* irá retornar *Carlos Alberto*, *Carlos Silva* e *José Carlos da Silva*;
    - ao inicializar, ela deve mostrar o nome de todos os aniversariantes do dia;
- uma classe `Contato`, que vai ser composta por :
    - nome completo;
    - telefone;
    - endereço;
    - data de aniversário (exibida sempre como dd/mm/yyyy);
    - correio eletrônico;
    - também deve mostrar :
        - a idade a partir da data de nascimento;
        - a quantidade de dias até o próximo aniversário;
- uma classe `Arquivo`, que :
    - vai salvar os dados em disco;
    - carregar os dados do disco sempre que for inicializada;
    - salvar os dados em disco sempre que algo for alterado;
    - escolha o formato de arquivo que achar melhor de trabalhar:
        - texto, json ou binário (única exceção de uso de material ainda não visto, MUITO DESAFIADOR!!!);

Considerações :
- opções incorretas devem ser mostradas na tela;
- use o módulo `os` para limpar a tela sempre que a agenda for inicalizada ou alguma opção escolhida;
- use menus numéricos para navegar pelas opções;
- use exceções específicas;
