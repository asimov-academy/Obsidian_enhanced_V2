import os
import re

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

class Notes:
    def cria_tags(texto):
        """Cria tags referentes ao texto."""
        print('Criando tags...')
        tags = llm.invoke(
            f'Crie até 10 tags referentes a este texto: \n{texto}\n'
            f'Voce deve responder apenas as tags, sem nenhum comentario, nem numeração'
            f'as tags devem estar alinhadas em uma unica linha, separadas por um espaço'
            f'Elas devem ser relacionadas apenas ao conteudo do texto'
            f'por exemplo, um texto que fale sobre filosofia pode ter a tag #filosofia'
            f'outro exemplo, um texto que fale sobre treino de academia pode ter as tags #fitness #health'
            f'todas a tags devem ter # na frente, por exemplo: #exemplo'
            )
        return tags.content

    def cria_resumo_curto(texto):
        """Cria um resumo curto de até 20 palavras da Transcrição"""
        print('Criando resumo curto...')
        resumo_curto = llm.invoke(
            f'Crie um resumo do texto em 20 palavras: \n{texto}'
            )
        return resumo_curto.content

    def cria_resumo_detalhado(texto):
        """Cria um resumo detalhado da Transcrição"""
        print('Criando resumo detalhado...')
        resumo_detalhado= llm.invoke(
            f'Resuma detalhadamente o texto:  \n{texto}\n'
            f'mantendo todas as informações importantes de forma estruturada'
            f'o Resumo deve conter todas as informações para que uma pessoa que não leu o texto orignal possa entender por completo'
            )
        return resumo_detalhado.content

    def cria_bullet_point(texto):
        """Cria um bullet point baseado na Transcrição"""
        print('Criando bullet point...')
        bullet_point = llm.invoke(
            f'Liste em bullet points as principais ideias referentes ao texto: \n{texto}'
            )
        return bullet_point.content

    def formata_nota(tags, resumo_curto, resumo_detalhado, bullet_point):
        """Formata os textos em uma unica nota com título, #tags, os resumos."""
        print('Formatando texto...')
        texto_final = (
            f'{tags}\n\n'
            f'# Resumo do Vídeo\n\n#'
            f'## Resumo Curto\n{resumo_curto}\n\n'
            f'## Resumo Detalhado\n{resumo_detalhado}\n\n'
            f'## Bullet Points\n{bullet_point}\n\n'
            # f'Link: {msg}'
        )
        return texto_final

    def salvar_nota(transcricao_path):
        """Salva o texto em um arquivo de texto no diretório _notas."""
        print('Criando texto da Nota')
        
        transcricao_path = transcricao_path.replace("'", "")
        print(f'1transcricao_path {transcricao_path}')

        with open(transcricao_path, "rb") as file:
            transcricao = file.read()
            tags = Notes.cria_tags(transcricao)
            resumo_curto = Notes.cria_resumo_curto(transcricao)
            resumo_detalhado = Notes.cria_resumo_detalhado(transcricao)
            bullet_point = Notes.cria_bullet_point(transcricao)
            nota = Notes.formata_nota(tags, resumo_curto, resumo_detalhado, bullet_point)
            print ('nota criada\n\n')

        output_path = os.path.dirname(transcricao_path)
        output_path = output_path.replace('transcricoes', 'notas')

        base_name = os.path.splitext(os.path.basename(transcricao_path))[0]
        resumo_path = f'{output_path}/{base_name}.md'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Criada pasta '_notas' em: {output_path}")
        
        with open(resumo_path, 'w') as f:
            f.write(nota)
        print(f"Nota salva em: {resumo_path}")

if __name__ == '__main__':
    transcricao_path =  'PARA TESTAR ADICIONE O CAMINHO DE UMA TRANSCRIÇÃO'
    Notes.salvar_nota(transcricao_path)




    

