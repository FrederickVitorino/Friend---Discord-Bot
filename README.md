PUC Goiás – Pontifícia Universidade Católica de Goiás            
Ciências da Computação
Turma: 2024.1-CMP1066/C01 - PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO

Projeto feito por Frederick Vitorino de Lima

Linguagem Utilizada: Python

Descrição do Projeto: Um Bot da plataforma de comunicação “Discord” que inclui diversas funcionalidades, como uma integração com a API da OpenAI para também tornar o Bot um ChatBot.

- Estrutura do Projeto -
O projeto é dividido em 4 arquivos .py:

main.py: Este é o arquivo principal que inicializa e executa o bot. Neste arquivo também estão localizados os eventos em que o bot interage e a árvore de comandos de barra do bot. 
commands.py: Contém as funções assíncronas usadas pelos eventos e comandos definidos em ‘main.py’.
functions.py: Contém funções utilitárias que suportam as funcionalidades de alguns comandos do bot.
nums.py: Contém um dicionário chamado “nums” que mapeia números inteiros de 1 a 9 para seus respectivos códigos unicode.
