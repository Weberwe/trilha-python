# tipo none

O tipo `None` em Python é um tipo de dado especial que representa a ausência de valor ou um valor nulo. Ele é usado em várias situações para indicar que algo está "vazio", "não definido" ou "não possui valor". Em Python, o valor `None` é único e é uma instância da classe `NoneType`.

## características do `none`:

1. **Singleton** : o `None` é um objeto único no Python. Ou seja, em toda a aplicação, existe apenas uma instância do `None`. Isso significa que se você comparar dois objetos `None` usando `is`, eles sempre serão iguais (`True`), pois ambos apontam para o mesmo objeto na memória;

2. **avaliação booleana** : em uma expressão booleana, `None` é avaliado como `False`. Portanto, se usar `None` em uma estrutura de controle como `if`, ele será considerado como `False`;

3. **Utilização Comum** :
   - **Valores de Retorno de Funções** : uma função que não possui uma declaração explícita de retorno (`return`) retorna `None` por padrão;
   - **Inicialização de Variáveis** : o `None` é frequentemente usado para inicializar variáveis que serão atribuídas posteriormente com valores reais;
   - **Placeholder** : em estruturas de dados, como listas ou dicionários, `None` pode ser usado como um valor temporário até que um valor "real" seja atribuído;

### exemplo de uso:

```python
>>> # função que não retorna nada explicitamente
>>> def minha_funcao():
...     pass
...
>>> resultado = minha_funcao()
>>> print(resultado)
None
>>>
>>> # inicializando uma variável com None
>>> variavel = None
>>> if variavel is None:
...     print("A variável não tem valor atribuído.")
...
>>> # uso de None como placeholder
>>> dados = {"nome": None, "idade": None}
>>> dados["nome"] = "Alice"
>>> dados["idade"] = 30
>>> print(dados)
{'nome': 'Alice', 'idade': 30}
>>> |
```

## comparando `None`:
- **usando `is`** : como `None` é um singleton, a comparação correta para verificar se uma variável é `None` é usando o operador `is`, não `==`. Exemplo:
    ```python
    >>> if variavel is None:
    ...     print("É None")
    ...
    >>> |
    ```

