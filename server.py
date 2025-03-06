import socket
from threading import Thread
from game_logic import shuffle_deck, evaluate_guess
from player_handler import handle_player
from utils.constants import HOST, PORT, WINNING_SCORE

players = []
scores = {}


def broadcast_message(message):
    for player in players:
        player["conn"].sendall(message.encode('utf-8'))


def game_loop():
    deck = shuffle_deck()
    current_card = deck.pop(0)

    while True:
        broadcast_message(f"Current Card: {current_card['value']}")
        guesses = {}

        # Get guesses from all players
        for player in players:
            conn = player["conn"]
            guess = conn.recv(1024).decode('utf-8')
            guesses[player["id"]] = guess

        # Draw next card and evaluate results
        next_card = deck.pop(0)
        broadcast_message(f"Next Card: {next_card['value']}")

        for player_id, guess in guesses.items():
            is_correct = evaluate_guess(current_card, next_card, guess)
            scores[player_id] += 1 if is_correct else 0

        current_card = next_card
        broadcast_message(f"Scores: {scores}")

        if any(score >= WINNING_SCORE for score in scores.values()):
            winner = max(scores, key=scores.get)
            broadcast_message(f"Game Over! Winner: Player {winner}")
            break


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(2)
        print("Server is listening for connections...")

        while len(players) < 2:
            conn, addr = server.accept()
            player_id = len(players) + 1
            print(f"Player {player_id} connected from {addr}.")
            players.append({"id": player_id, "conn": conn})
            scores[player_id] = 0

        print("Starting the game...")
        game_loop()

        for player in players:
            player["conn"].close()


if __name__ == "__main__":
    start_server()
