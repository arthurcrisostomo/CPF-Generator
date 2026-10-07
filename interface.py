
# > Importa a classe QWidget responsável pela criação da janela e widgets
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit

# > Importa a classe QFont responsável pelos elementos gráficos (fonte, tamanho do texto)
from PySide6.QtGui import QFont

# > Importa a função responsável por retornar um cpf aleatório
from logica import gerar_cpf

# > Janela é uma classe que herda os métodos e atributos da classe pai QWidget
class Janela(QWidget):

    # > Roda automaticamente ao instanciar a classe -> Monta a interface
    def __init__(self):

        # > Executa o __init__ da classe pai (QWidget), responsável por criar a janela
        super().__init__()

        # > Armazena a janela regras ao apertar no botão Regras
        self.janela_regras = None

        # > Armazena o cpf atual a ser exibido
        self._cpf = ''

        # > Armazena o entry_cpf_gerado que vai ser utilizado pelo property
        self.entry_cpf_gerado = None

        # > Define o titulo da janela
        self.setWindowTitle("Gerador de CPF")

        # > Define o tamanho da janela
        self.resize(500, 200)

        # Cria o Organizador da janela que organiza os widgets empilhando-os na vertical
        layout_janela = QVBoxLayout(self)

        # > Cria o objeto do frame responsável por armazenar os widgets relacionados ao usuario
        frame_usuario = QFrame()

        # > Adiciona o frame_usuario dentro do organizador da janela
        layout_janela.addWidget(frame_usuario)

        # > Cria o Organizador do frame que organiza os widgets empilhando-os na Horizontal
        layout_frame_usuario = QHBoxLayout(frame_usuario)

        # > Cria o botão Gerar CPF
        button_gerar_cpf = QPushButton("Gerar CPF")

        # QFont('Arial', 18) > Cria o objeto que descreve a fonte, tamanho da fonte
        # setFont() > Recebe o objeto criado e aplica o estilo ao botão Gerar CPF
        button_gerar_cpf.setFont(QFont('Arial', 18))

        # Chama a função que vai gerar o cpf
        button_gerar_cpf.clicked.connect(self.gerar_cpf)

        # > Adiciona o botão Gerar CPF dentro do frame_usuario
        layout_frame_usuario.addWidget(button_gerar_cpf)

        # > Cria o botão Regras
        button_regras = QPushButton('Regras')

        # > Abre uma nova janela regras
        button_regras.clicked.connect(self.abrir_janela_regras)

        # QFont() > Cria o objeto que descreve a fonte e o tamanho do texto
        # setFont() > Recebe o objeto criado e aplica o estilo ao botão Regras
        button_regras.setFont(QFont('Arial', 18))

        # > Adiciona o botão Regras dentro do frame_usuario
        layout_frame_usuario.addWidget(button_regras)

        # > Cria o objeto do frame responsável por armazenar os widgets relacionados a resposta
        frame_resposta = QFrame()

        # > Adiciona o frame_resposta dentro do organizador da janela
        layout_janela.addWidget(frame_resposta)

        # > Cria o Organizador do frame_resposta que organiza os widgets empilhando-os na Vertical
        layout_frame_resposta = QHBoxLayout(frame_resposta)

        # > Cria o texto CPF Gerado:
        label_cpf_gerado = QLabel('CPF Gerado:')

        # QFont() > Cria o objeto que descreve a fonte e o tamanho do texto
        # setFont() > Recebe o objeto criado e aplica o estilo ao botão Regras
        label_cpf_gerado.setFont(QFont('Arial', 18))

        # > Adiciona a label CPF Gerado e Entry dentro do frame_usuario
        layout_frame_resposta.addWidget(label_cpf_gerado)

        # > Cria o Entry que exibe o cpf gerado e atribui a self.entry_cpf_gerado
        self.entry_cpf_gerado = QLineEdit()

        # QFont() > Cria o objeto que descreve a fonte e o tamanho do texto
        # setFont() > Recebe o objeto criado e aplica o estilo ao botão Regras
        self.entry_cpf_gerado.setFont(QFont('Arial', 18))

        # > Adiciona o Entry no organizador do frame resposta
        layout_frame_resposta.addWidget(self.entry_cpf_gerado)

    @property # -> GETTER: Roda quando alguem le self.cpf
    def cpf(self):
        return self._cpf

    @cpf.setter # -> SETTER: roda quando alguem atribui self.cpf = ...
    def cpf(self, cpf_gerado):

        # > Atribui o cpf gerado ao atributo interno cpf
        self._cpf = cpf_gerado

        # > Coloca o cpf gerado no entry
        self.entry_cpf_gerado.setText(cpf_gerado)

    def gerar_cpf(self):
        # > Chama a funçao responsável por gerar o cpf valido e retorna para o property cpf
        self.cpf = gerar_cpf()

    def abrir_janela_regras(self):

        # > Verifica se o atributo self.janela_regras é None
        if self.janela_regras is None:

            # > Cria a tela e armazena no atributo self.janela_regras da janela principal para não encerrar ao finalizar a função
            self.janela_regras = JanelaRegras()

        # > Exibe a janela regras
        self.janela_regras.show()

        # > Foca a janela caso ja esteja aberta
        self.janela_regras.raise_()

    def closeEvent(self, event):

        # > Verifica se o atributo self.janela_regras não é None
        if self.janela_regras is not None:

            # > Fecha a janela regras
            self.janela_regras.close()

class JanelaRegras(QWidget):
    def __init__(self):
        super().__init__()

        # > Define o titulo da janelas
        self.setWindowTitle('Regras')

        # > Define o tamanho da janela regras
        self.resize(400, 400)

        # > Cria o Organizador da janela regras que organiza os widgets empilhando-os na Horizontal
        layout_janela_regras = QVBoxLayout(self)

        # > Cria o espaço para texto
        text_regras = QPlainTextEdit()

        # > Define o estilo a ser aplicado no espaço do texto
        text_regras.setFont(QFont('Arial', 12))

        # > Define apenas para leitura
        text_regras.setReadOnly(True)

        # > Define o texto a ser inserido no espaço
        text_regras.setPlainText("""Um CPF válido possui 11 dígitos, sendo os dois últimos dígitos verificadores. Para validar o número, são realizados cálculos matemáticos com os primeiros 9 dígitos, usando multiplicações, somas e divisões por 11 para determinar os dígitos verificadores. Além disso, CPFs formados pelos mesmos dígitos, como 111.111.111-11, são considerados inválidos. O CPF também deve seguir corretamente o algoritmo oficial de validação dos dígitos verificadores.
        """)

        # > Adiciona o campo de texto dentro do organizador
        layout_janela_regras.addWidget(text_regras)




