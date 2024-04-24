import random
import os


def clear():
    return os.system("clear")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deck = []

players = {"you": {}, "dealer": {}}


def reset_game():
    for player in players:
        players[player] = {"score": 0, "cards": []}
    return cards * 4


def get_card(player):
    random_card = random.choice(deck)
    deck.remove(random_card)
    player["cards"].append(random_card)
    player["score"] = calculate_score(player["cards"])


def initial_shuffle():
    for player in players:
        for _ in range(2):
            get_card(players[player])


def calculate_score(cards):
    has_ace = False
    score = 0

    for card in cards:
        score += card
        if card == 1:
            has_ace = True

    if score > 21 and has_ace:
        score -= 10

    return score


def output_cards(only_first=True):
    clear()
    print(
        f'Your Cards are: {players["you"]["cards"]} (Score: {players["you"]["score"]}).'
    )
    if only_first:
        print(f'Dealers Cards: [{players["dealer"]["cards"][0]}]')
    else:
        print(
            f'Dealers Cards: {players["dealer"]["cards"]} (Score: {players["dealer"]["score"]})'
        )


def output_win():
    if players["you"]["score"] > 21 or (
        21 >= players["dealer"]["score"] > players["you"]["score"]
    ):
        print("You loose.")
    elif players["dealer"]["score"] > 21 or (
        21 >= players["you"]["score"] > players["dealer"]["score"]
    ):
        print("You win.")
    else:
        print("It's a draw.")


end_of_game = False

while not end_of_game:
    deck = reset_game()
    initial_shuffle()

    end_of_turn = False

    if players["dealer"]["score"] == 21:
        end_of_turn = True

    while not end_of_turn:
        output_cards()

        if players["you"]["score"] < 21:
            answer = input("Another card (y) or pass (p)? ")

            if answer == "p":
                end_of_turn = True
            else:
                get_card(players["you"])

        else:
            end_of_turn = True

    if players["you"]["score"] <= 21 and players["dealer"]["score"] != 21:
        end_of_turn = False
        while not end_of_turn:
            if players["dealer"]["score"] > 21 or (
                players["dealer"]["score"] >= players["you"]["score"]
                and players["dealer"]["score"] > 17
            ):
                end_of_turn = True
            else:
                get_card(players["dealer"])

    output_cards(False)
    output_win()

    answer = input("Another game? (y/n) ")

    if answer != "y":
        end_of_game = True

clear()
print("Goodbye.")
