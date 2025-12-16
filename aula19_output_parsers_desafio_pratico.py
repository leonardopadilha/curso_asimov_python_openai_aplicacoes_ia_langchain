from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from pydantic import BaseModel, Field

"""
Este soprador de folhas é bastante incrível. Ele tem quatro configurações: sopro de vela, brisa suave, 
cidade ventosa e tornado. Chegou em dois dias, bem a tempo para o presente de aniversário 
da minha esposa. Acho que minha esposa gostou tanto que ficou sem palavras. Até agora, fui o único 
a usá-lo, e tenho usado em todas as manhãs alternadas para limpar as folhas do nosso gramado. É um pouco 
mais caro do que os outros sopradores de folhas disponíveis no mercado, mas acho que vale a pena pelas 
características extras.

E eu quero que o modelo de linguagem processe esta review para estruturá-la no seguinte formato:

```json
{
  "presente": true,
  "dias_entrega": 2,
  "percepcao_de_valor": ["um pouco mais caro do que os outros sopradores de folhas disponíveis no mercado"]
}

```
"""

load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini")

review_cliente = """Este soprador de folhas é bastante incrível. Ele tem 
quatro configurações: sopro de vela, brisa suave, cidade ventosa 
e tornado. Chegou em dois dias, bem a tempo para o presente de 
aniversário da minha esposa. Acho que minha esposa gostou tanto 
que ficou sem palavras. Até agora, fui o único a usá-lo, e tenho 
usado em todas as manhãs alternadas para limpar as folhas do 
nosso gramado. É um pouco mais caro do que os outros sopradores 
de folhas disponíveis no mercado, mas acho que vale a pena pelas 
características extras."""

class AvaliacaoReview(BaseModel):
    """ Avalia review do cliente """
    descricao_produto: list[str] = Field(description="breve descrição do produto")
    entrega_produto: bool = Field(description="Verdadeiro se o cliente ficou satisfeito com a entrega e False se não ficou")
    sentimento_produto: bool = Field(description="Verdadeiro se o cliente ficou satisfeito com o produto e False se não ficou")
    atendimento: list[str] = Field(description="breve descrição do atendimento do cliente")
    satisfacao: list[str] = Field(description="Satisfação geral do cliente com a compra")


llm_estruturada = chat.with_structured_output(AvaliacaoReview)
resposta = llm_estruturada.invoke(review_cliente)
print(resposta.descricao_produto)
#print(resposta)

