# Distance

Nesta pasta há um arquivo `main.py` com uma classe `Point` e duas funções:

- `euclidean_distance(a, b)`
- `manhattan_distance(a, b)`

A classe e as funções tem uma docstring com descrição acompanhada de trechos de sessões de console do Python.

Os trechos de console na documentação da classe e das funções exemplificam como é esperado que a classe e funções se comportem. Eles também serão usados no teste automatizado para validar a implementação.

## Atividade

Sua tarefa será implementar a classe `Point`.

- Ela deve receber uma coordenada X e uma coordenada Y para ser instanciada: `Point(0.0, 1.0)`
- As coordenadas devem ser to tipo float, a classe deve proibir a tentativa de instanciâ-la com parâmetros de outros tipos
- Uma instância de `Point` chamada `ponto` deve retornar o valor da coordenada x com o seguinte código: `ponto.x`
- Uma instância de `Point` chamada `ponto` deve permitr redefinir o valor da coordenada x com o seguinte código: `ponto.x = 2.0`
- O mesmo comportamento é esperado para a coordenada y
- Ao instanciar um `Point` no console Python espera-se que a saída seja um texto copiável que cria um `Point` com as mesmas coordenadas

Com a classe `Point` implementada o próximo passo é implementar as funções:

- `euclidean_distance(a, b)`
- `manhattan_distance(a, b)`

Os dois parâmetros devem ser uma instância da classe `Point`, a função deve subir uma exceção se receber algum outro tipo de parâmetro.

A `euclidean_distance` deve retornar a distância euclidiana entre os dois pontos (ver [Distância Euclidiana](https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_euclidiana))

A `manhattan_distance` deve retornar a distância de manhattan entre os dois pontos (ver [Distância de Manhattan](https://pt.wikipedia.org/wiki/Geometria_do_t%C3%A1xi))

## Validação

Você pode validar sua solução conforme desenvolve executando o `main.py`, que irá testar os trechos de console para checar se a implementação se comporta como o esperado.

Exemplo:
```
➜  python3 main.py   
**********************************************************************
File "main.py", line n, in __main__.euclidean_distance
Failed example:
    euclidean_distance(Point(0.0, 0.0), Point(3.0, 4.0))
Expected:
    5.0
Got:
    0.0
**********************************************************************
1 items had failures:
   1 of   3 in __main__.euclidean_distance
***Test Failed*** 1 failures.
```

Aqui a implementação passou em quase todos os testes, falhou em apenas 1.
Era esperado que o resultado da chamada `euclidean_distance(Point(0.0, 0.0), Point(3.0, 4.0))` fosse 5.0 e não 0.0.

Quando sua implementação estiver correta e passar nos 15 testes o script não gera uma saída:
```
➜  python3 main.py
➜  
```

## Regras

Sua solução deve funcionar com Python 3.6 ou Python 3.7, não vamos testar em interpretadores mais antigos.

Uma das filosofias do Python é que ele vem com "baterias inclusas", ou seja, tem uma biblioteca padrão rica o suficiente para resolver diversos problemas sem dependências adicionais. A atividade deste repositório pode e deve ser resolvida sem o uso de bibliotecas externas.

Não altere a documentação da classe ou das funções.
