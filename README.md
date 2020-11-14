## 🤖 Bot de Fila do LOL
O bot utiliza as funcionalidades de reconhecimento de imagem da biblioteca Pyautogui para verificar quando uma fila é encontrada no Lolzin, o bot irá aceitar a fila e 
enviar um email, caso tenha sido passado anteriormente, avisando que uma partidade foi encontrada.

📽 Tutorial no Youtube: https://youtu.be/yN_Gj9AYjF8.

### 🛠 Como rodar 
1. Primeiramente instale as dependências ```pip install pyautogui``` e ```pip install opencv-python```
2. Preencher o email e senha (variáveis ```SENDER_EMAIL``` e ```PASSWORD ``` da função ```send_email```) para o script realizar o login na conta que vai enviar os emails 
  quando as partidas forem encontradas
3. Rode o programa, pelo cmd o comando é ```python bot.py```
4. Deixe o bot rodando e coloque na fila
