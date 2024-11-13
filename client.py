import asyncio

async def send_messages():
    reader, writer = await asyncio.open_connection('192.168.1.107', 8888)
  
    try:
        while True:
            message = input()
            print(f'сообщение отправленно')
            writer.write(message.encode())
            await writer.drain()  # Убедитесь, что сообщение отправлено

            #await asyncio.sleep(7)  # Ждем 7 секунд перед отправкой следующего сообщения

            data = await reader.read(10000)
            message2 = data.decode()
            print(f"Длина сообщение состовляет: {message2} символов")

    finally:
        writer.close()

if __name__ == '__main__':
    asyncio.run(send_messages())
