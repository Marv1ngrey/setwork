import asyncio

async def send_messages():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    try:
        while True:
            message = "Hello, Server!"
            print(f'Sending: {message}')
            writer.write(message.encode())
            await writer.drain()  # Убедитесь, что сообщение отправлено

            await asyncio.sleep(7)  # Ждем 7 секунд перед отправкой следующего сообщения
    finally:
        writer.close()

if __name__ == '__main__':
    asyncio.run(send_messages())
