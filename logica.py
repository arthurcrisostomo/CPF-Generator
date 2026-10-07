
import random

def gerar_cpf():

    # > Pega 9 numeros entre 0 e 9 convertendo-os para str e vai juntando todos e armazena na variavel cpf
    cpf = ''.join(str(random.randint(0, 9)) for _ in range(9))

    # > Define o valor inicial do multiplcador para calcular o DV 1
    multiplicador = 10

    # > Itera duas vezes
    for i in range(2):

        # > Cria a lista responsável por armazenar a multiplação a seguir
        lista_resultado_multiplicacao = []

        # > Itera sobre cada numero do cpf
        for numero in cpf:

            # > Multiplica o numero convertido pra inteiro pelo valor do multiplicador atual
            lista_resultado_multiplicacao.append(int(numero) * multiplicador)

            # > Decrementa o valor do multiplicador em -1
            multiplicador -= 1

        # > Soma todas as multiplicações da lista_resultado_multiplicação e calcula o resto da divisão (%)
        resto = sum(lista_resultado_multiplicacao) % 11

        # > Caso o resto da divisão seja 1 ou 0 adiciona o numero 0, se não apenas faz o calculo de 11 - o resto,
        # isso é importante porque se não tiver essa verificaçao o cpf vai ser gerado com 1 numero a mais
        cpf += '0' if resto < 2 else str(11 - resto)

        # > Define o novo valor do multiplcador para calcular o DV 2
        multiplicador = 11

    # > Retorna o cpf formatado para quem o chamou
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
