import socket
import threading

q = {
    "What is the currency of the United States? :\na.Dollar\nb.Euro\nThe answer": "a",
    "What is the currency of Japan? :\na.Dollar\nb.Yen\nThe answer": "b",
    "What is the currency of Germany? :\na.Pound\nb.Euro\nThe answer": "b",
    "What is the currency of Australia? :\na.Dollar\nb.Yen\nThe answer": "a",
    "What is the currency of Brazil? :\na.Dollar\nb.Real\nThe answer": "b",
    "What is the currency of India? :\na.Rupee\nb.Euro\nThe answer": "a",
    "What is the currency of Canada? :\na.Dollar\nb.Euro\nThe answer": "a",
    "What is the currency of France? :\na.Dollar\nb.Euro\nThe answer": "b",
    "What is the currency of China? :\na.Ruble\nb.Yuan\nThe answer": "b",
    "What is the currency of Russia? :\na.Ruble\nb.Euro\nThe answer": "a",
    "What is the currency of South Africa? :\na.Rand\nb.Euro\nThe answer": "a",
    "What is the currency of Saudi Arabia? :\na.Riyal\nb.Dollar\nThe answer": "a",
    "What is the currency of Mexico? :\na.Dollar\nb.Peso\nThe answer": "b",
    "What is the currency of Italy? :\na.Euro\nb.Dollar\nThe answer": "a",
    "What is the currency of Egypt? :\na.Pound\nb.Dollar\nThe answer": "a",
    "What is the currency of Argentina? :\na.Euro\nb.Peso\nThe answer": "b",
    "What is the currency of United Kingdom? :\na.Pound\nb.Dollar\nThe answer": "a",
    "What is the currency of Spain? :\na.Euro\nb.Dollar\nThe answer": "a",
    "What is the currency of South Korea? :\na.Won\nb.Dollar\nThe answer": "a",
    "What is the currency of Nigeria? :\na.Naira\nb.Dollar\nThe answer": "a"
}

client_scores = {}

def handleClient(client_soc, client_address):
    try:
        client_soc.send(str(len(q)).encode())

        for question in q:
            client_soc.send(question.encode())

            client_ans = client_soc.recv(1024).decode().strip()

            if client_ans.lower() == q[question].lower():
                client_scores[client_address] = client_scores.get(client_address, 0) + 1

        score = client_scores.get(client_address, 0)
        client_soc.send(f"Score: {score}/{len(q)}\n".encode())

    except ConnectionAbortedError:
        print(f"Connection the client: {client_address}")

    client_soc.close()
    print(f"Disconnected client: {client_address}")

def RUN_server():
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 3333)
    server_soc.bind(server_address)

    server_soc.listen(5)
    print("Server started..........")

    while True:
        client_socket, client_address = server_soc.accept()
        print(f"Connected to {client_address}")

        client_thread = threading.Thread(target=handleClient, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    RUN_server()
