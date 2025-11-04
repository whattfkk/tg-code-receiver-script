from pyrogram import Client
import requests
import asyncio

print('Привет! Это программа для получения кода подтверждения от Telegram в SMS. Сейчас я получу актуальные данные для авторизации, подожди секунду...')
# Сейчас введи свой номер телефона, на который надо получить SMS: ')

credentials = requests.get("https://other.littleusername.ru/tg/telega/credentials")
if credentials.status_code == 200:
    print('Получаю данные...')
    api_id = credentials.json()['api_id']
    api_hash = credentials.json()['api_hash']
input('Данные получены.\n\nПредупреждаю, что код в SMS отправится, только если ни на одном телефоне/ПК сейчас нет этого аккаунта, иначе код придет именно туда.\nТвои данные никуда не отправляются.\nНажми Enter, если согласен со всем, или Ctrl-C, если хочешь выйти.')
phone_number = input('\n\n\n\n\nГотово! Сейчас введи свой номер телефона, на который надо получить SMS. Нажми Ctrl-C через примерно пять секунд после ввода кода. ')

app = Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash,
    test_mode = True,
    phone_number = phone_number
)

app.run()

input('Теперь отправь запрос на код на телефон и нажми Enter, когда сделаешь это.')

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        async for message in app.get_chat_history(777000):
            print(message.text)
            break

asyncio.run(main())
print('Спасибо за использование!')