# write a progrram to print the high score of the game 

import random
def game():
    score = random.randint(0, 100)  # Simulating a game score between 0 and 100
    try:
        with open("highscore.txt") as file:
            highscore_text = file.read().strip()
    except FileNotFoundError:
        highscore_text = ""

    highscore = int(highscore_text) if highscore_text else 0
    print(f"Your score: {score}")

    if score > highscore:
        print("Congratulations! You have the new high score!")
        with open("highscore.txt", "w") as file:
            file.write(str(score))
        highscore = score
    return score, highscore
game()

