import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode()

        if message == '':
            break

        print(f"Полученно сообщение: {message.lower()}")
        print(f"Полученное сообщение в нижнем и верхнем регистре:\n1) {message.lower()}\n 2){message.upper()}")
    
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'сервер {addr} подключен')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())