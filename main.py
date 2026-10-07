
# > Importa biblioteca sys responsável por repassar os argumentos da linha de comando ao Qt e permite encerrar o programa
import sys

# > Importa a classe QApplication, responsável por inicializar o Qt e gerenciar o loop de eventos da aplicação
from PySide6.QtWidgets import QApplication

# > Importa a classe janela responsável por criar e exibir a interface grafica
from interface import Janela

def main():

    # > Inicializa o framework Qt (prepara a comunicação com o SO para desenhar janelas, ler mouse, teclado e cria o gerenciador de eventos) e repassa a ele os argumentos do terminal (sys.argv)
    app = QApplication(sys.argv)

    # > Instancia a classe Janela que é responsável pela criação da interface
    janela = Janela()

    # show > Exibe a janela
    janela.show()

    # app.exec > Inicia o loop de eventos e fica aberto aguardando ações do usuario
    # sys.exit > Recebe o numero retornado:
    #           (0) -> Programa terminou normalmente, sem erro
    #           (!= 0) -> Programa terminou com algum problema
    sys.exit(app.exec())

if __name__ == '__main__':
    main()