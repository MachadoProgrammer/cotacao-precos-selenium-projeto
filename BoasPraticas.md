# Boa pratica

- Don't repeat yourself(DRY)
- Verify returned values(str, float...)
- Error treatment

## 4 Direções de como criar funções limpas e elegantes

1. Dê nomes significativos, para que possa ser entendida só de ler o nome da função
2. Funções pequenas que fazem apenas uma coisa -> Uma função grande dividida em pequenas funções para melhor entendimento e manutenção.
"Se você não consegue descrever sua função em uma frase, ela está fazendo coisas demais"
3. Quanto menor a quantidade de argumentos, melhor(max: 3args)
4. Use funções para organizar o código e economizar linhas de código(DRY), códigos se repetindo
5. args. idade e profissao são opcionais = idade == None e profissao == None

# Transformando ideias em Software

1. Ter uma ideia e anotar tudo sobre ela, com maiores detalhes possiveis(ou pegar-la de alguem)
2. Quebrar a grande ideia em menores passos/tarefas e anotar
3. Organizar e comece a trabalhar nas pequenas tarefas, uma a uma(uso de software de organização de projeto é opcional, mas recomendado) -> Notion
    -> Metodologia Kanbann
      -> To DO: Todas as tarefas a realizar
      -> Doing:  
      -> Done:

4. Preencher as lacunas do conhecimento, quando necessário(alguma tarefa que não sabe fazer)
5. Publique seu projeto -> protifolio 

# Log e Logging(Uma forma de manter um histórico de o que acontece na sua aplicação)

-> Exibir para o usuário ou manter um histórico do que está acontecendo na sua aplicação
    1. Relátorios de segurança
    2.  Relátorios de atividade
    3. O que aconteceu na aplicação no decorre dos dias

-> Manter o histórico em um arquivo dos erros que estão acontecendo sem ter que exibir a msg para o usuário 

. Pode ser aberto no bloco de notas

# Coleções

-- Podemos usar o comando dir(list), dir(str), etc... para ver os métodos disponíveis para cada tipo de coleção

-- Processar multiplas listas -> zip, zip_longest -> from itertools
* zip_longest -> para caso uma lista seja maior que a outra

## Dicionários 

-- dict.keys() -> Retorna as chaves do dicionário
-- dict.values() -> Retorna as valores do dicionário
-- dict.items() -> Retorna chave e valor do dicionário

## Tuplas

-- Não é possível adicionar, remover ou alterar elementos de uma tupla.(index)
    1. Dentro de um programa onde os valores não podem ser alterados
    2. Desempacotamento na função -> passar uma tupla 

## Arrays x Listas

````
A escolha entre listas e arrays depende de necessidades específicas de flexibilidade, desempenho e uso de memória. Para operações gerais e pequenas coleções de dados, listas são frequentemente adequadas. Para grandes volumes de dados numéricos e operações matemáticas mais robustas e intensas, arrays são a melhor escolha.

Grande diferença entre um array e uma lista é como elas se comportam na memória RAM. Enquanto a lista usa ponteiros (o que gasta mais processamento) um array ocupa um lugar fixo na memória tornando o processo mais fácil
````

1. Armazena uma coleção de items, mas item do mesmo tipo -> typecode array('i', [lista])
2. Só aceita valores inteiros, números decimais e caracteres

-- Range uma das melhores maneiras de gera valor, tanto para criar laço de repetição como gerar valores inserido em uma lista e outros tipos de coleções

-- Enumerate - Enumerar elementos de uma coleção (lista, tupla, etc),
Facilita a iteração sobre uma coleção e, simultaneamente, obter o índice do elemento

## Ordenar coleções por propriedades

- Se você quiser ordenar um dict ou tipo de coleção que possui uma chave ou propriedade
- Na tupla e matriz para ordenar se passa o index 

-> from operator import itemgetter

## Map() 

1. Processa e retorna todos os valores

-- Função que recebe uma função e uma coleção de dados e aplica a função a cada elemento da coleção
### Logica mais complexa 
    # verificar a pontuação do aluno no banco de dados
    # verificar se o pagamento foi feito em uma planilha

## Filter 

1. Pode ser usado para processar uma coleção de dados e retornar apenas aqueles dados/ items avalados como verdadeiros

## SET 
 -> recebe valores, não aceita repetição e não tem índice
 -> não é ordenado
 -> não é indexado




# Como criar um bot do zero 

- Explicação completa
````
1. Tarefa é feita pelo computador ? -> sim?
2. Você sabe quais são os passos manuais necessários para fazer a tarefa ? -> sim?
3. Você consegue quebrar esses passos manuais em uma sequência de passos ? -> sim?
````

## Podemos criar o bot
````
- Entender o que você quer fazer de forma geral 
- Você consegue explicar para outra pessoa?
- Descrever em grandes detalhes como você faz esse processo de forma manual hoje 
- Quebre cada passo da sua descrição numa tarefa ou modulo, caso seja um projeto maior
- Você consegue quebrar esses passos manuais numa sequência de passos? 
- Transforme cada passo em codigo
- Faça isso a cada um dos passos e ao finaizar terá o ‘bot’ pronto 


    # Metodo 5q's
    
    1. Quais dados necessários de entrada ?
    2. O que fazer com eles ?
    3. Restrições do problema ?
    4. Resultado esperado ?
    5. sequência de passos para o resultado

````
## Exemplo de passo a passo de criar um bot
```
1. Bot de curtidas e comentários no Instagram com PyAutoGUI: -> Ideia
2. Vamos criar um bot que define qual página quer seguir verifica 
   se a postagem mais atual ainda não foi curtida pelo bot. Caso uma nova postagem 
   tenha sido feita, ele deve entrar nessa postagem, curtir e comentar algo nela. -> O que o bot irá fazer
3. Passos -> sequência de passos em passos manuais

abrir o Instagram
buscar pela página
verifica se é seguidor, se não, seguir
abrir postagem mais recente
verifica se postagem já foi curtida, se não, curtir
adicionar um comentário
voltar para home do Instagram
repetir processo a cada 24h

````
