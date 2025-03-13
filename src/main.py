import os
import discord as disc
from src.commands import responderMensagem, enviarMensagemBoasVindas, enviarMensagemDespedida, falar, rolar, criarEnquete
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
    if not mensagem.content or mensagem.content[0] != '=' or mensagem.author == client.user: return
    
    await responderMensagem(mensagem)

@tree.command(name="speak", description="Faz o Friend enviar uma mensagem escrita por você")
@app_commands.describe(mensagem="O que você quer que eu fale?")
async def speak(interaction: disc.Interaction, mensagem: str) -> None:
    await falar(interaction, mensagem)

@tree.command(name="roll", description="Faz o Friend lançar um ou mais dados de 4, 6, 8, 10, 12, 20 ou 100 lados")
@app_commands.describe(dado="Qual o tipo do dado que será lançado?", 
                       qt_dados="Qual a quantidade de dados que serão lançados?", 
                       bonus="Qual o valor do bônus a ser adicionado? (opcional)",
                       esconder="Deseja esconder a rolagem dos outros usuários? (opcional)")
@app_commands.choices(dado=[
    app_commands.Choice(name="d4", value=4),
    app_commands.Choice(name="d6", value=6),
    app_commands.Choice(name="d8", value=8),
    app_commands.Choice(name="d10", value=10),
    app_commands.Choice(name="d12", value=12),
    app_commands.Choice(name="d20", value=20),
    app_commands.Choice(name="100", value=100),
])
@app_commands.choices(esconder=[
    app_commands.Choice(name="Sim", value=1),
    app_commands.Choice(name="Não", value=0),
])
async def roll(interaction: disc.Interaction, dado: int, qt_dados: int, bonus: int = 0, esconder: int = 0) -> None:
    await rolar(interaction, dado, qt_dados, bonus, esconder)

@tree.command(name="create-poll", description="Faz o Friend criar uma enquete com até 9 opções")
@app_commands.describe(nome_enquete="Qual será o nome da enquete?", 
                       opcoes="Quais são as opções da enquete? (Separe por vírgulas, Ex: Opção 1, Opção 2)")
async def createPoll(interaction: disc.Interaction, nome_enquete: str, opcoes: str) -> None:
    await criarEnquete(interaction, nome_enquete, opcoes)

def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()