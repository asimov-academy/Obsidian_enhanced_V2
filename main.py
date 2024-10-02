from time import sleep

from langchain.agents import (
    AgentExecutor,
    create_tool_calling_agent
)
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

from tools import IsaacTools
from utils.whatsapp_listener import WhatsWeb

# https://asimov.academy/curso-gratuito-python/
# https://asimov.academy/curso-gratuito-ia/

class Isaac:
    def __init__(self):
        self.llm = ChatOpenAI(model= 'gpt-4o-mini') # não esqueça de adicionar sua api_key no .env
        self.tool = IsaacTools()
        self.whats = WhatsWeb()


    def criar_agente(self):
        # https://hub.asimov.academy/curso/agents-de-ia-com-python-e-langchain/
        tools = [
            Tool(name="baixar_video_youtube", func=IsaacTools.baixar_video_youtube, description="Baixa vídeo do YouTube e retorna seu título, autor e descrição."),
            Tool(name="extrair_audio_video", func=IsaacTools.extrair_audio, description="Extrai o áudio de um arquivo MP4."),
            Tool(name="descrever_imagem", func=IsaacTools.descreve_imagem, description="Analisa o image_path e retorna uma descrição detalhada. Caso a imagem contenha texto, ele será transcrito."),
            Tool(name="transcrever_audio", func=IsaacTools.transcrever_audio, description="Transcreve um arquivo de áudio salvo em audio_path para texto utilizando reconhecimento de fala."),
            Tool(name="salvar_nota", func=IsaacTools.salvar_nota, description="Salva o texto em um arquivo de texto no diretório notas."),
        ]
        llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

        prompt = ChatPromptTemplate.from_messages(
            # https://hub.asimov.academy/curso/engenharia-de-prompts/
            [
                (
                    "system",
                    """
                    Você é um assistente especializado em ajudar os usuários a criar notas detalhadas e completas.
                    Você auxilia extraindo as informações principais, 
                    organizando-as em pontos estruturados e garantindo que as notas finais sejam abrangentes.
                    Sempre resuma as informações de maneira clara e concisa.
                    Mantenha o controle dos resultados das ferramentas e incorpore-os às notas conforme necessário.
                    O resultado final deve estar em português brasileiro e formatado em Markdown.
                    """

                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        agent = create_tool_calling_agent(
            llm=llm,
            tools=tools,
            prompt=prompt,
        )
        return agent, tools

    def processar_mensagem(self, msg, agente, tools):
        """Processa a mensagem recebida via WhatsApp e chama a ferramenta correta."""
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=agente,
            tools=tools,
            verbose=True,
        )
        executor_prompt = {"input": 
            f'identifique o tipo de arquivo da mensagem e utilize as tools para criar uma nota.'
            f' - se for um link do youtube: baixe o video, extraia o audio do video baixado, transcreva o audio do audio extraido então salve a nota da transcrição'
            f' - se for um arquivo mp4: extraia o audio do video, transcreva o audio do audio extraido então salve a nota da transcrição'
            f' - se for um arquivo mp3 ou ogg: transcreva o audio então salve a nota da transcrição'
            f' - se for um arquivo de imagem: descreva a imagem e seu conteudo e salve a nota a partir de sua transcrição'
            f'a mensagem é: {msg}'}
        
        resultado = agent_executor.invoke(executor_prompt)
        return resultado

if __name__ == '__main__':
    bot = Isaac()
    bot.whats.buscar_conversa()
    msg = ' '
    agente, tools = bot.criar_agente()
    last_msg = '/quit'
    while msg != '/quit':
        sleep(1)
        msg = bot.whats.ultima_msg()
        if msg != last_msg and msg:
            print(f"Mensagem recebida: {msg}")
            last_msg = msg
            try:
                resultado = bot.processar_mensagem(msg, agente, tools)
                print(f"Resultado: {resultado}")
            except Exception as e:
                print(e)
