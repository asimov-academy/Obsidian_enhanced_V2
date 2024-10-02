import base64

from io import BytesIO
from PIL import Image

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

class ProcessImage:
    def openai_analysis(self, image_path):
        """
        Analisa imagem, e descreve detalhadamente seu conteudo.
        Caso ela possua textos, transcreve em formato markdown.
        """
        pil_image = Image.open(image_path)
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")


        input = [
            [HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": """
                        Analise a imagem, e descreva detalhadamente seu conteudo.
                        Caso ela possua textos, transcreva-os em formato markdown.
                        """
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_str}"
                        }
                    }
                ]
            )],
        ]

        analise_imagem = llm.invoke(input[0])
        return analise_imagem
 
if __name__ == '__main__':
    img = ProcessImage()
    img_path = 'PARA TESTAR ADICIONE O CAMINHO DE UMA IMAGEM JPEG'
    analise_imagem = img.openai_analysis(img_path).content
    print(analise_imagem)