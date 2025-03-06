def handle_player(conn, player_id):
    try:
        conn.sendall(f"Welcome Player {player_id}".encode('utf-8'))
    except Exception as e:
        print(f"Error handling player {player_id}: {e}")
