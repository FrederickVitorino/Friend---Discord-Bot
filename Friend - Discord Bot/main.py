import os
import discord as disc
from commands import responderMensagem, enviarMensagemBoasVindas, enviarMensagemDespedida, falar, rolar, criarEnquete
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()
TOKEN = os.environ["TOKEN"]

intents: disc.Intents = disc.Intents.default()
intents.message_content = True
intents.members = True
client: disc.Client = disc.Client(intents=intents)
tree: app_commands.CommandTree = app_commands.CommandTree(client)

@client.event
async def on_ready() -> None:
    print(f"{client.user} está rodando!")
    try:
        await tree.sync()
        print("Comandos sincronizados!")
    except app_commands.CommandSyncFailure as e:
        print(f"Falha ao sincronizar comandos: {e}")

@client.event
async def on_member_join(novoMembro: disc.Member) -> None:
    await enviarMensagemBoasVindas(novoMembro)

@client.event
async def on_member_remove(membroAntigo: disc.Member) -> None:
    await enviarMensagemDespedida(membroAntigo)

@client.event
async def on_message(mensagem: disc.Message) -> None:
    if mensagem.author == client.user or mensagem.content[0] != '=': return
    
    try:
        await responderMensagem(mensagem)
    except Exception as e:
        print(e)

@tree.command(name="speak", description="Faz o Friend enviar uma mensagem escrita por você")
@app_commands.describe(mensagem="O que você quer que eu fale?")
async def speak(interaction: disc.Interaction, mensagem: str) -> None:
    await falar(interaction, mensagem)

@tree.command(name="roll", description="Faz o Friend lançar um d6, d20 ou d100")
@app_commands.describe(dado="Qual o tipo do dado que será lançado?")
@app_commands.choices(dado=[
    app_commands.Choice(name="d6", value=6),
    app_commands.Choice(name="d20", value=20),
    app_commands.Choice(name="d100", value=100),
])
async def roll(interaction: disc.Interaction, dado: int) -> None:
    await rolar(interaction, dado)

@tree.command(name="create-poll", description="Faz o Friend criar uma enquete com até 9 opções")
@app_commands.describe(nome_enquete="Qual será o nome da enquete?", opcoes="Quais são as opções da enquete? (Separe por vírgulas, Ex: Opção 1, Opção 2)")
async def createPoll(interaction: disc.Interaction, nome_enquete: str, opcoes: str) -> None:
    await criarEnquete(interaction, nome_enquete, opcoes)

def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()