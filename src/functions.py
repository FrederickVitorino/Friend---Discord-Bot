import os
import random
from openai import OpenAI
from dotenv import load_dotenv

def gerarResposta(msg: str, systemContent: str) -> str:
    load_dotenv()
    OAIKey: str = os.environ["OAIKey"]
    client: OpenAI = OpenAI(api_key=OAIKey)

    resposta = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{
            "role": "system", 
            "content": systemContent
        }, {
            "role": "user",
            "content": msg
        }]
    )

    return resposta.choices[0].message.content

def gerarNumero(num: int) -> int:
    return random.randint(1, num)