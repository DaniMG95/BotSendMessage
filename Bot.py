import telegram
from twisted.internet import task, reactor
import logging

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = "1155082026:AAHBYlC2LFfNP7s_iLIMj6014Qnz-T3K76M"
CHAT_ID = "@pruebasdanimunoz"


timeout = 120.0 # Sixty seconds

# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start():
    """Envia un mensaje cuando se emita el comando /start."""
    global TOKEN
    global CHAT_ID
    bot = telegram.Bot(token=TOKEN)
    bot.send_photo(chat_id = CHAT_ID,photo="https://i.ytimg.com/vi/mrRRZVmnrXY/maxresdefault.jpg", caption ="Hola soy la topacio, ¿quieres coño?")

def do_something():
    print("Doing stuff...")
    start()



def main():
    """Inicio del Bot"""
    l = task.LoopingCall(do_something)
    l.start(timeout) # call every sixty seconds

    reactor.run()


if __name__ == '__main__':
    main()