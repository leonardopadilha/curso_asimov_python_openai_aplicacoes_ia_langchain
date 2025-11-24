#from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template('''
Responda a seguinte pergunta do usuário em até {n_palavras} palavras:
{pergunta}
''')

#load_dotenv()

#llm = OpenAI()

prompt = prompt_template.format(n_palavras=10, pergunta="O que é um buraco negro?")
print(prompt)

