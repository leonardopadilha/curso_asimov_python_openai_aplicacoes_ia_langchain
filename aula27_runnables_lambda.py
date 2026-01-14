from langchain_core.runnables import RunnableLambda

# RunnableLambda transforma uma função em um Runnable

def cumprimentar(nome):
    return f"Olá, {nome}!"

runnable_cumprimentar = RunnableLambda(cumprimentar)

resultado = runnable_cumprimentar.invoke("Maria")
print(resultado)