import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.constants import HOST, PORT
import socket
from utils.constants import HOST, PORT




def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected to server.")

        while True:
            server_message = client.recv(1024).decode('utf-8')
            print(server_message)

            if "Game Over" in server_message:
                break

            if "Current Card" in server_message:
                guess = input("Is the next card higher or lower? (higher/lower): ").strip().lower()
                client.sendall(guess.encode('utf-8'))


if __name__ == "__main__":
    main()
