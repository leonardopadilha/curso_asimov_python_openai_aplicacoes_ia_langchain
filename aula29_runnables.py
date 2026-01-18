"""
RunnablePassthrough

O RunnablePassthrough é um tipo de Runnable que simplesmente passa a entrada recebida 
como saída, podendo também adicionar chaves adicionais ao resultado. Ele se comporta 
como uma função de identidade, mas é útil em cenários onde você deseja incluir lógica 
adicional ou manipular a entrada de alguma forma antes de passar adiante.
"""

from langchain_core.runnables import RunnablePassthrough

# Criando um RunnablePassthrough
runnable = RunnablePassthrough()

# Invocando o runnable
resultado = runnable.invoke({'mensagem': 'Olá, mundo!'})
print(resultado) # Saída: {'mensagem': 'Olá, mundo!'}

"""
** Neste exemplo, o RunnablePassthrough simplesmente retorna o dicionário 
recebido, permitindo que ele seja usado em um fluxo de trabalho onde a 
entrada precisa ser preservada.

----------------------------------------------------------------

RunnableLambda

O RunnableLambda permite que você crie um Runnable a partir de uma função 
Python arbitrária. Isso é útil para encapsular qualquer lógica que você 
queira aplicar aos dados ou para transformar entradas em saídas de uma 
maneira específica. Um aspecto interessante do RunnableLambda é que ele 
pode ser construído para funcionar de forma síncrona ou assíncrona, 
dependendo de como a função é definida.
"""

from langchain_core.runnables import RunnableLambda

# Definindo uma função simples
def cumprimentar(nome):
    return f'Olá, {nome}'

# Criando um RunnableLambda a partir da função
runnable_cumprimentar = RunnableLambda(cumprimentar)

# Invocando o RunnableLambda
resultado = runnable_cumprimentar.invoke('Maria')
print(resultado) # Saída: 'Olá, Maria!'

"""
** Neste exemplo, o RunnableLambda encapsula a função cumprimentar, permitindo 
que ela seja chamada como um Runnable, facilitando sua integração em cadeias.

----------------------------------------------------------------

RunnableParallel

O RunnableParallel é um componente poderoso que permite executar múltiplos Runnables 
simultaneamente. Ele aceita um dicionário de Runnables e fornece a mesma entrada a todos 
eles, retornando um dicionário com os resultados correspondentes. Isso é especialmente 
útil quando você precisa realizar várias operações independentes ao mesmo tempo, economizando 
tempo em processos que podem ser feitos em paralelo.
"""

from langchain_core.runnables import RunnableLambda, RunnableParallel

# Definindo algumas funções simples
def adicionar_um(x):
    return x + 1

def multiplicar_por_dois(x):
    return x * 2

# Criando Runnables a partir das funções
runnable_adicionar = RunnableLambda(adicionar_um)
runnable_multiplicar = RunnableLambda(multiplicar_por_dois)

# Criando um RunnableParallel
runnable_paralelo = RunnableParallel(
    adicionar=runnable_adicionar,
    multiplicar=runnable_multiplicar
)

# Invocando o RunnableParallel
resultado = runnable_paralelo.invoke({'x': 3})
print(resultado) # Saída: {'adicionar': 4, multiplicar: 6}

"""
** Neste exemplo, RunnableParallel executa as duas operações (adicionar_um e multiplicar_por_dois) 
ao mesmo tempo, retornando os resultados em um dicionário. O uso do RunnableLambda para criar as
funções que serão executadas em paralelo mostra como esses componentes trabalham bem juntos.
"""

