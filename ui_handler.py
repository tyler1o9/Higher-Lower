def display_card(card):
    print(f"Card: {card['value']} of {card['suit']}")


def get_user_input():
    return input("Higher or lower? ").strip().lower()
