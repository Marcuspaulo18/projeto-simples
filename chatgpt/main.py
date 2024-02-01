from senha import API_KEY
import requests

headers = {"Authorization": f"Bearer {API_KEY}", "content-type": "application/json"}

link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,
    "messages": [
        {"role": "system", "content": "Você é um assistente virtual que fala sobre previsões de mercado."},
        {"role": "user", "content": "escreva um email para o meu chefe dizendo a previsao do preço do dolar nos proximos dois meses"}
    ]
 }

requisicao = requests.post(link, headers=headers, json=body_mensagem)  # Utilize o parâmetro json

print(requisicao)
print(requisicao.text)


    
    