from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate

template_word_count = PromptTemplate.from_template('''
Responda a pergunta em até {n_palavras} palavras.''')

template_language = PromptTemplate.from_template('''
Retorne a resposta na {lingua}.''')

template_final = (
    template_word_count + 
    template_language +
    '\nResponda a pergunta seguinte seguindo as instruções: {pergunta}'
)

load_dotenv()

llm = OpenAI(model="gpt-4o-mini")

print(template_final.template)
print("-" * 100)

template_user = template_final.format(n_palavras=10, lingua='inglês', pergunta='O que é uma estrela?')
print(template_user)
print("-" * 100)

prompt = template_final.format(n_palavras=10, lingua='inglês', pergunta='O que é uma estrela?')
print(llm.invoke(prompt))
