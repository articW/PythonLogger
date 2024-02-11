import socket, ssl, datetime, asyncio
import telegram

HOST = ''
PORT = ''
CERTFILE = ''
KEYFILE = ''
SECRET = ''
#Telegram params
TOKEN = ''
CHATID = ''

async def send_notification(fileName):
    message = f"📂 New file transfer\nName: {fileName}"
    try:
        bot = telegram.Bot(token=TOKEN)
        await bot.send_message(chat_id=CHATID, text=message)
    except Exception as e:
        print(f"Error sending message: {e}")

def receive_file(conn):
    try:
        fileName = conn.recv(1024).decode()
        with open(fileName, 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
            conn.close()
        return fileName
    except:
        pass

def main():
    sslContext = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    sslContext.check_hostname = False
    sslContext.verify_mode = ssl.CERT_NONE
    sslContext.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as netSocket:
            sslSocket = sslContext.wrap_socket(netSocket, server_side=True)
            sslSocket.bind((HOST, PORT))
            sslSocket.listen()
            print('Waiting for connection...')
            conn, addr = sslSocket.accept()
            with conn:
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print(f'Connection established with {addr}')
                clientSecret = conn.recv(1024).decode()
                conn.sendall(b"Secret received")
                if clientSecret == SECRET:
                    fileName = receive_file(conn)
                    print(f'File {fileName} received successfully\n')
                    asyncio.run(send_notification(fileName))
                else:
                    print("Incorrect Secret. Session closed.\n")
                    conn.close()
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    while True:
        main()

