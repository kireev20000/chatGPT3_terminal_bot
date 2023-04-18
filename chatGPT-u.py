"""
Заходим на https://ora.sh создаём своего бота или юзаем чужого, переходим в бота, в браузере открываем
инспектора элементов, в mozille это ПКМ исследовать, переходим во вкладку сеть или Ctrl+Shift+E отправляем
боту запрос, в инспекторе сети получаем JSON копируем его как cURL подставляем свои значения в файл python,
запускаем, радуемся! Не забудьте для питона поставить зависимости pip install brotli requests json
"""

import requests
import json
import sys


def chatGPT(text):
    url = 'https://ora.sh/api/conversation'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://ora.sh/chat/defae059-d985-45c7-8876-40a3dd6e855b',
        'Content-Type': 'application/json',
        'Origin': 'https://ora.sh',
        'DNT': '1',
        'Proxy-Authorization': '',
        'Connection': 'keep-alive',
        'Cookie': '__Host-next-auth.csrf-token=d0783bd48c68f0a77fc59c9c03345db5915fd0f3d8770b4b08f9327adfb7f74b%7C9672d5cd3b11e638737d1c951b00e0b625eb6b6df3a1eb4ca8511ab06a8d982d; __Secure-next-auth.callback-url=https%3A%2F%2Fora.sh; _ga_MWL7THFH58=GS1.1.1681805860.1.1.1681805891.0.0.0; _ga=GA1.1.1980635404.1681805860', #сюда свои значения
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'

    }

    data = {
        "chatbotId": "defae059-d985-45c7-8876-40a3dd6e855b",
        "input": f"""{text}""",
        "userId": "auto:7c162d33-b37f-4c01-9cb6-a4cb72767600",
        "provider": "OPEN_AI",
        "includeHistory": True,
    }

    response = requests.post(url, headers=headers,
                             data=json.dumps(data), allow_redirects=False)
    json_data = response.json()

    response_text = json_data['response']
    print(response_text)


print("Для выхода введи q")
while True:
    text = input("User: ")
    if text == "q":
        break
    chatGPT(text)
    print("*" * 30)
