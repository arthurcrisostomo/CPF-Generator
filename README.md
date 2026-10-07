# Gerador de CPF

Aplicativo desktop que gera CPF válido, feito em Python com interface gráfica em PySide6 (Qt).

<img width="1164" height="824" alt="{4B37800A-A2BC-4E0A-96DD-49093DE77418}" src="https://github.com/user-attachments/assets/bf5abed8-7ff2-4dc3-ab6c-264d86d1360d" />

## Funcionalidades

- Gera um CPF ao clicar no botão **Gerar CPF**
- Exibe o resultado em um campo de texto, pronto para copiar
- Janela **Regras** com as informações sobre a formação do CPF

## Requisitos

- PySide6

## Como executar

```bash
python main.py
```

## Estrutura do projeto

```
.
├── main.py             # Ponto de entrada: cria o QApplication e abre a janela
├── interface.py        # Interface gráfica (janela principal e janela de regras)
├── logica.py           # Lógica de geração do CPF (sem dependência do Qt)
├── requirements.txt    # Dependências do projeto
└── README.md
```

A lógica fica separada da interface: o `logica.py` só gera os dados, e o `interface.py` decide como exibi-los.

## Aviso

Os CPFs gerados são apenas para fins de teste e estudo. Não representam pessoas reais.
