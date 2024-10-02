
# Obsidian_Enhanced_V2

Este projeto automatiza a criação de notas no Obsidian utilizando Inteligência Artificial para resumir vídeos.
A automação é feita utilizando agentes com Langchain, PyTube, Whisper, e a API da OpenAI para salvar as notas geradas na pasta do Obsidian.

## Funcionalidades
* *Download de vídeos do Youtube*
* *Extrair audios de videos*
* *Transcrever audios*
* *Descrever imagens*
* *Integração com WhatsApp Web utilizando Selenium*
* *Criação de tags, resumos curtos, resumos detalhados e bulletpoint com GPT-4o-mini*
* *Utilização de agente para utilização dinamica das ferramentas*
* *Formatação e salvamento automático de notas no Obsidian*

## Tecnologias Utilizadas

* *Python 3.10*
* *Poetry* para gerenciamento de dependências
* *Langchain* para criação e execução do agente
* *PyTube* para download de vídeos do YouTube
* *Whisper* para transcrição de áudio
* *OpenAI GPT-4o-mini* para geração de resumos
* *Selenium* para automação do WhatsApp Web
* *Obsidian* como ferramenta de notas
* *dotenv* para gerenciamento de variáveis de ambiente

## Configuração

### Pré-requisitos

* Python 3.10
* Um arquivo .env contendo a sua chave da OpenAI API (OPENAI_API_KEY)
* Google Chrome instalado (para o Selenium)
* Um grupo criado no WhatsApp com um nome especificado no código
* [Poetry](https://python-poetry.org/docs/#installation) instalado

### Instalação e Configuração

1. *Clone este repositório:*

   '''shh
   git clone https://github.com/asimov-academy/Obsidian_enhanced_V2.git
   cd Enhanced_Obsidian_V2
   '''

2. *Inicialize o Projeto com Poetry:*

   '''shh
   poetry init
   '''

   Siga as instruções para configurar o nome do projeto, versão, etc.

3. *Instale as Dependências:*

   Utilize o poetry para instalar as bibliotecas necessárias:

   '''shh
   poetry install
   '''

4. *Crie e Configure o Arquivo .env:*

   Crie um arquivo .env na raiz do projeto e adicione sua chave da OpenAI API:

   plaintext
   OPENAI_API_KEY = 'sua-chave-aqui'
   

5. *Inicie o Projeto:*

   Ative o ambiente virtual com poetry e execute o projeto:

   '''shh
   poetry shell
   poetry run python main.py
   '''

   Isso ativará o ambiente, inicializará o código.

### Execução

1. O Selenium abrirá o Google Chrome, e você deve se logar no WhatsApp Web na primeira execução.

2. Configure também a pasta padrão para downloads no Chrome que abrir através Selenium.

3. Envie mensagens no grupo do WhatsApp configurado para iniciar a criação de notas. 

### Personalização

* Todas as funções, tools e definições de arquivos de saída podem ser alterados.
* Na verdade, encorajamos isso! Desenvolva uma solução ajustada para a sua vontade e necessidade.

## Contribuições

Sinta-se à vontade para enviar issues ou pull requests. Contribuições são bem-vindas!

## Conheça também os cursos da Asimov Academy 🚀:

* Cursos gratuitos de IA e Python do zero, que podem te ajudar a criar suas próprias soluções:
- https://asimov.academy/curso-gratuito-python/
- https://asimov.academy/curso-gratuito-ia/

* E Cursos relevantes para um entendimento mais completo de como utilizar as ferramentas deste projeto:
- https://hub.asimov.academy/curso/agents-de-ia-com-python-e-langchain/
- https://hub.asimov.academy/curso/engenharia-de-prompts/
- https://hub.asimov.academy/curso/navegando-na-internet-automaticamente-com-selenium/

## Licença

Este projeto está licenciado sob a [Asimov Academy](LICENSE).
