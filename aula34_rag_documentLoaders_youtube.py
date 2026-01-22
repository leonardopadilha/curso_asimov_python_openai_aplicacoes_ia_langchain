from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from dotenv import load_dotenv

load_dotenv()

url = 'https://www.youtube.com/watch?v=rOjusRRO1EI'
save_dir='./docs/youtube/'
loader = GenericLoader(
    YoutubeAudioLoader([url], save_dir),
    OpenAIWhisperParser()
)
docs = loader.load()
print(docs[0].page_content)