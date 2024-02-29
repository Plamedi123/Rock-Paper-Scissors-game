import random
import curses

class Action(int):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

    @staticmethod
    def from_number(number):
        return [Action.Rock, Action.Paper, Action.Scissors, Action.Lizard, Action.Spock][number]

    @staticmethod
    def relationships():
        return {
            Action.Scissors: [Action.Lizard, Action.Paper],
            Action.Paper: [Action.Spock, Action.Rock],
            Action.Rock: [Action.Lizard, Action.Scissors],
            Action.Lizard: [Action.Spock, Action.Paper],
            Action.Spock: [Action.Scissors, Action.Rock]
        }

def main(stdscr):
    curses.curs_set(False)
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.timeout(100)

    user_action = None
    computer_action = None
    round_number = 0

    while True:
        win.clear()
        win.addstr(0, (sw - 37) // 2, "ROCK PAPER SCISSORS LIZARD SPOCK", curses.A_STANDOUT)
        win.addstr(2, 1, "User:")
        win.addstr(2, 15, "Computer:")
        win.addstr(4, 1, f"{' ' * (len(action_names[user_action]) + 1)} {action_names[user_action]}" if user_action else " ")
        win.addstr(4, 15, f"{' ' * (len(action_names[computer_action]) + 1)} {action_names[computer_action]}" if computer_action else " ")
        win.addstr(6, 1, "Press any key to continue...")
        win.refresh()

        if not user_action:
            user_action = get_user_selection(win)

        if not computer_action:
            computer_action = get_computer_selection()

        round_number += 1
        result = determine_winner(user_action, computer_action)
        if result == 0:
            win.addstr(8, 1, "It's a tie!")
        elif result == 1:
            win.addstr(8, 1, "You win!")
        elif result == -1:
            win.addstr(8, 1, "You lose!")

        win.addstr(10, 1, f"Round: {round_number}")
        win.refresh()
        win.getkey()

        user_action = None
        computer_action = None

def get_user_selection(win):
    action_names = {
        Action.Rock: "Rock",
        Action.Paper: "Paper",
        Action.Scissors: "Scissors",
        Action.Lizard: "Lizard",
        Action.Spock: "Spock"
    }

    choices = [f"{i + 1}. {action_names[Action.from_number(i)]}" for i in range(len(Action))]
    choices_str = "\n".join(choices)
    win.addstr(8, 1, choices_str)
    win.refresh()
    key = win.getch()
    while key < ord('1') or key > ord('5'):
        key = win.getch()
    return Action.from_number(int(chr(key)) - 1)

def get_computer_selection():
    return Action(random.randint(0, 4))

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return 0
    if computer_action in Action.relationships()[user_action]:
        return 1
    return -1

curses.wrapper(main)
