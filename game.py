import random


def game():

    print("Please choose a number")

    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")

    while True:
        user_choice = input(">")

        try:
            user_val = int(user_choice)

            if user_val in [1, 2, 3]:
                break
            else:
                print("Enter a valid number")

        except ValueError:
            print("Enter a valid number")

    computer_choice = random.choice("123")
    computer_val = int(computer_choice)

    def play_again():
        again = input("Enter 1 to play again: ")

        if again == "1":
            game()

    if user_val == 1 and computer_val == 2:
        print("Computer chose Paper")
        print("You lose!")
        play_again()

    elif user_val == 1 and computer_val == 3:
        print("Computer chose Scissors")
        print("You win!")
        play_again()

    elif user_val == 2 and computer_val == 1:
        print("Computer chose Rock")
        print("You win!")
        play_again()

    elif user_val == 2 and computer_val == 3:
        print("Computer chose Scissors")
        print("You lose!")
        play_again()

    elif user_val == 3 and computer_val == 1:
        print("Computer chose Rock")
        print("You lose!")
        play_again()

    elif user_val == 3 and computer_val == 2:
        print("Computer chose Paper")
        print("You win!")
        play_again()

    else:
        print("Draw! Try again.")
        game()


game()
