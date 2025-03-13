import discord as disc
from typing import List
from src.nums import nums
from src.functions import gerarResposta, gerarNumero

async def responderMensagem(mensagem: disc.Message) -> None:
    msg: str = mensagem.content[1:]
    systemContent: str = "Seu nome é Friend e você é um Bot do Discord. Você é um assistente prestativo."
    resposta: str = gerarResposta(msg, systemContent)
    try:
        await mensagem.channel.send(resposta)
    except Exception as e:
        print(e)

async def enviarMensagemBoasVindas(novoMembro: disc.Member) -> None:
    novoUsuario: str = '<@' + str(novoMembro.id) + '>'
    mensagem: str = f'Olá {novoUsuario}:smiley:! Bem vindo(a) ao servidor "{novoMembro.guild.name}"!'
    try:
        await novoMembro.guild.system_channel.send(mensagem)
    except Exception as e:
        print(e)

async def enviarMensagemDespedida(membroAntigo: disc.Member) -> None:
    usuarioAntigo: str = '<@' + str(membroAntigo.id) + '>'
    mensagem: str = f'{usuarioAntigo} acabou de sair do servidor... :frowning2:'
    try:
        await membroAntigo.guild.system_channel.send(mensagem)
    except Exception as e:
        print(e)

async def falar(interaction: disc.Interaction, mensagem: str) -> None:
    resposta: str = mensagem
    try:
        await interaction.channel.send(resposta)
        await interaction.response.send_message(content="Comando executado com sucesso!", ephemeral=True, delete_after=2.0)
    except Exception as e:
        print(e)

async def rolar(interaction: disc.Interaction, ladosDado: int, qt_dados: int, bonus: int, esconder: bool) -> None:
    mensagem: str = f":game_die: <@{interaction.user.id}> O resultado do lançamento de **{qt_dados}** dado(s) de **{ladosDado}** lados com +**{bonus}** foi:"
    for i in range(qt_dados):
        resultado: int = gerarNumero(ladosDado)
        mensagem = mensagem + f'\n:game_die:: **{resultado}** + **{bonus}** = **{resultado + bonus}**'

    try:
        if esconder == 1:
            await interaction.response.send_message(content=mensagem, ephemeral=True)
        else:
            await interaction.response.send_message(content=mensagem)
    except Exception as e:
        print(e)

async def criarEnquete(interaction: disc.Interaction, nome_enquete:str, opcoes: str) -> None:
    listaOpcoes: List[str] = opcoes.split(", ")
    tamanhoLista: int = len(listaOpcoes)
    if tamanhoLista > 9 or tamanhoLista < 2:
        mensagem: str = f'Quantidade de opções inválida! :rage: Só consigo criar enquetes de 2 até 9 opções!'
        mensagem = mensagem + f'\n(Opções: **"{opcoes}"** ``|`` Quantidade de opções: **{tamanhoLista}**)'
        await interaction.response.send_message(content=mensagem, ephemeral=True)
        return

    mensagem: str = f'\nEnquete: **"{nome_enquete}"** criada por <@{interaction.user.id}>\n'
    for i in range(tamanhoLista):
        unicodeReacao = nums[i+1][0]
        mensagem = mensagem + f"\n{unicodeReacao}: {listaOpcoes[i]}"

    try:
        await interaction.response.send_message(content=mensagem)
        respostaInteracao = await interaction.original_response()
        for i in range(tamanhoLista):
            unicodeReacao = nums[i+1][0]
            await respostaInteracao.add_reaction(f"{unicodeReacao}")
    except Exception as e:
        print(e)