


from flask import Flask, render_template, request
from botcity.core import DesktopBot
import threading
import time

app = Flask(__name__)

numero_de_pedidos = 50
bot_running = False
bot_thread = None
stop_automation = False
class MyBot(DesktopBot):
    def action(self, execution=None):
        primeira_execucao = True
        while not stop_automation:
            if primeira_execucao:
                time.sleep(5)  # Executa apenas na primeira iteração
                primeira_execucao = False
            self.space()
            self.space()  
            self.control_c()
            self.type_keys(["alt", "tab"])
            if self.find( "garantianova", matching=0.97, waiting_time=300):
                self.tab()
            else:
                raise ValueError("Elemento 'garantianova' não foi encontrado.")
            self.type_keys(["alt", "o"])
            self.type_keys(["m"])
            self.type_keys(["m"])
            self.control_v()
            self.enter()
            # SE NAO ENCONTRAR PULE PARA O PROXIMO
            # IMAGENS DE ENTRADA
            if self.find( "saldodevolução", matching=0.97, waiting_time=200):
                self.enter()
            if self.find( "saldodevolução", matching=0.97, waiting_time=200):
                self.enter()
            if self.find( "parcelasematraso", matching=0.97, waiting_time=200):
                self.enter()

            if self.find( "relacaodedocumentos", matching=0.97, waiting_time=200):
                self.enter()
            if self.find( "recado", matching=0.97, waiting_time=10000):
                self.enter()
            if self.find( "vendaspendentes", matching=0.97, waiting_time=200):
                self.enter()
            time.sleep(2)
            if self.find( "obs", matching=0.97, waiting_time=200):
                self.enter()
            time.sleep(2)
            self.type_keys(["alt", "o"])
            self.type_keys(["e"])
            time.sleep(1)
            self.key_f9()
            #   #FINALIZANDO VENDA
            if self.find( "confirmacaooutrass2", matching=0.97, waiting_time=1000):
                self.click()
                self.type_left()
                self.enter()
          #  if self.find("limitedecreditook", matching=0.97, waiting_time=200):
           #     self.enter()
            self.type_keys(["alt", "tab"])

            if self.find( "procuraonumerovenda", matching=0.97, waiting_time=10000):
                self.doubleClickRelative(57, 8)
            else:
                print("Não encontrado")
            self.control_c()
            self.type_keys(["alt", "tab"])
            self.kb_type(" - NUMERO DO PEDIDO - ")
            self.control_v()
            time.sleep(1)
            self.enter()
            if self.find( "garantianova", matching=0.97, waiting_time=300):
                self.tab()
            else:
                raise ValueError("Elemento 'garantianova' não foi encontrado.")
            # # NOTA DE BONI
            self.type_keys(["alt", "tab"])
            self.clickAt(x=8, y=122)

            self.type_down()
            self.space()
            self.space()
            self.control_c()
            self.type_keys(["alt", "tab"])
            if self.find( "garantianova", matching=0.97, waiting_time=300):
                self.tab()
            else:
                raise ValueError("Elemento 'garantianova' não foi encontrado.")
            self.type_keys(["alt", "o"])
            self.type_keys(["m"])
            self.type_keys(["m"])
            self.control_v()
            self.enter()
            # #SE NAO ENCONTRAR PULE PARA O PROXIMO
            #  #IMAGENS DE ENTRADA
            if self.find( "saldodevolução", matching=0.97, waiting_time=200):
                self.enter()
            if self.find( "saldodevolução", matching=0.97, waiting_time=200):
                self.enter()
            if self.find( "parcelasematraso", matching=0.97, waiting_time=200):
                self.enter()

            if self.find( "relacaodedocumentos", matching=0.97, waiting_time=200):
                self.enter()
            if self.find( "recado", matching=0.97, waiting_time=10000):
                self.enter()
            if self.find( "vendaspendentes", matching=0.97, waiting_time=200):
                self.enter()
            time.sleep(2)
            if self.find( "obs", matching=0.97, waiting_time=200):
                self.enter()
            time.sleep(2)
            self.type_keys(["alt", "o"])
            self.type_keys(["t"])
            self.type_down()
            self.type_down()
            self.type_down()
            self.enter()
            if self.find( "confirmaboni", matching=0.97, waiting_time=300):
                self.type_left()
                self.enter()
            else:
                print("Não encontrado")
            self.key_f9()
            if self.find("confirmavend", matching=0.97, waiting_time=300):
                self.type_left()
                self.enter()
                self.kb_type(" Mercadoria Bonificada Referente A Nf de Venda N: . O Icms-st Deverá Ser Calculado Pelo Estabelecimento Varejista No Momento do Recebimento da Mercadoria - Art. 46, 5 , Livro I - Ricms/rs. ")
                time.sleep(1)
                self.enter()
            if self.find( "garantianova", matching=0.97, waiting_time=300):
                self.tab()
            else:
                raise ValueError("Elemento 'garantianova' não foi encontrado.")

            self.type_keys(["alt", "tab"])
            self.clickAt(x=8, y=122)
            self.type_down()

        def not_found(self, label):
            print(f"Element not found: {label}")


def run_bot():
    global bot_running, bot_thread
    bot_running = True
    bot = MyBot()
    bot.main()
    bot_running = False


def stop_bot():
    global stop_automation, bot_thread
    stop_automation = True
    if bot_thread:
        bot_thread.join()
    stop_automation = False


@app.route('/')
def index():
    return render_template('index.html', bot_running=bot_running)


@app.route('/start_bot', methods=['POST'])
def start_bot():
    global bot_running, bot_thread
    if not bot_running:
        bot_thread = threading.Thread(target=run_bot)
        bot_thread.start()
    return render_template('index.html', bot_running=bot_running)


@app.route('/stop_bot', methods=['POST'])
def stop_bot_route():
    global bot_running
    if bot_running:
        stop_bot()
        bot_running = False
    return render_template('index.html', bot_running=bot_running)


if __name__ == '__main__':
    app.run(debug=True)









