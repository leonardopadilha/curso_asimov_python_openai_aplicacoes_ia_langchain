from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core import output_parsers
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from typing import Optional
from pydantic import BaseModel, Field

class Piada(BaseModel):
    """Piada para contar ao usuário"""
    introducao: str = Field(description='A introdução da piada')
    punchline: str = Field(description='A conclusão da piada')
    avaliacao: Optional[int] = Field(description='O quão engraçada é a piada de 1 a 10')

load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini")

llm_estruturada = chat.with_structured_output(Piada)
resposta = llm_estruturada.invoke('Conte uma piada sobre gatinhos')
print(resposta)
#print(resposta.punchline)