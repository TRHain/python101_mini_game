# =========================================
# PYTHON 101 MINI BATTLE GAME
# =========================================

print("=================================")
print("   WELCOME TO BATTLE QUEST")
print("=================================")

# -----------------------------------------
# LOGIN / AUTHENTICATION
# -----------------------------------------

secret_password = "python123"

password = input("Enter game password: ")

if password != secret_password:
    print("ACCESS DENIED")
    print("Game Over")
else:

    print("ACCESS GRANTED")
    print()

    # -----------------------------------------
    # PLAYER SETUP
    # -----------------------------------------

    player1 = input("Enter Player 1 Name: ")
    player2 = input("Enter Player 2 Name: ")

    print()
    print("Welcome warriors!")
    print(player1, "vs", player2)
    print()

    # -----------------------------------------
    # PLAYER STATS
    # -----------------------------------------

    player1_health = 100
    player2_health = 100

    player1_points = 0
    player2_points = 0

    # -----------------------------------------
    # ROUND 1
    # -----------------------------------------

    print("======== ROUND 1 ========")

    move1 = input(f"{player1}, choose your move (slash/fireball): ")
    move2 = input(f"{player2}, choose your move (slash/fireball): ")

    # PLAYER 1 ATTACK
    if move1 == "slash":
        player2_health -= 15
        player1_points += 10
        print(player1, "used SLASH!")
    elif move1 == "fireball":
        player2_health -= 25
        player1_points += 20
        print(player1, "used FIREBALL!")

    # PLAYER 2 ATTACK
    if move2 == "slash":
        player1_health -= 15
        player2_points += 10
        print(player2, "used SLASH!")
    elif move2 == "fireball":
        player1_health -= 25
        player2_points += 20
        print(player2, "used FIREBALL!")

    print()

    # -----------------------------------------
    # BONUS ROUND
    # -----------------------------------------

    print("======== BONUS ROUND ========")

    bonus1 = input(f"{player1}, solve this for bonus points: 5 + 5 = ")
    bonus2 = input(f"{player2}, solve this for bonus points: 7 + 3 = ")

    if bonus1 == "10":
        player1_points += 50
        print(player1, "earned BONUS POINTS!")

    if bonus2 == "10":
        player2_points += 50
        print(player2, "earned BONUS POINTS!")

    print()

    # -----------------------------------------
    # FINAL RESULTS
    # -----------------------------------------

    print("======== FINAL RESULTS ========")

    print()
    print(player1)
    print("Health:", player1_health)
    print("Points:", player1_points)

    print()

    print(player2)
    print("Health:", player2_health)
    print("Points:", player2_points)

    print()

    # -----------------------------------------
    # WINNER
    # -----------------------------------------

    if player1_points > player2_points:
        print(player1, "WINS THE GAME!")
    elif player2_points > player1_points:
        print(player2, "WINS THE GAME!")
    else:
        print("IT'S A TIE!")

    print()
    print("Thanks for playing Battle Quest!")

