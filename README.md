 * Funcionalidades do script

Gravação de áudio: Utiliza pyaudio para capturar o áudio do microfone e salva em um arquivo WAV.

Gravação de vídeo: Utiliza pyautogui e cv2 para capturar a tela e salvar em um arquivo AVI.
Threads: Utilizamos threads para gravar áudio e vídeo simultaneamente.
Combinação de áudio e vídeo: Utilizamos moviepy para combinar o áudio e o vídeo em um único arquivo MP4.
Parar a gravação: Pressione Ctrl+C para parar a gravação.
Este script básico grava a tela e o áudio do microfone e combina os dois em um único vídeo.





* Instrições de uso


1 - Clonar ou copiar o projeto

 Copie ou clone o repositório do projeto para a outra máquina.

2 - Criar e ativar um ambiente virtual:

python -m venv venv
.\venv\Scripts\activate

3 - Instalar as dependências:

Com o ambiente virtual ativado, execute.
pip install -r requirements.txt


4 - Executar o script.
python screen_recorder.py

5 - Desativar o ambiente virtual após uso.
deactivate
