# =============================================================
#  DOG ADVENTURE  -  main.py
#
#  This file is the brain of the game. The webpage (index.html)
#  runs feed(), play() and rest() when you click the buttons.
#
#  YOUR MISSION: find all 10 "TODO" comments and complete them.
#  Save the file and refresh the page after each one to see
#  what changed.
#
#  Where do print() messages go?
#  They appear in the browser console, not on the page.
#  Open it with:  Cmd + Option + J  (Mac)  or  Ctrl + Shift + J  (Windows)
# =============================================================

import random
from pyscript import document, window


# -------------------------------------------------------------
#  HELPERS - already done for you. Read them, but don't change them.
# -------------------------------------------------------------

def show(element_id, text):
    """Put some text on the page, inside the element with this id."""
    document.getElementById(element_id).innerText = str(text)


def set_bar(element_id, value):
    """Make a stat bar as wide as the value (0 to 100)."""
    document.getElementById(element_id).style.width = str(value) + "%"


def add_to_journal(message):
    """Add a new line to the top of the Journal on the page."""
    journal = document.getElementById("journal-content")
    entry = document.createElement("div")
    entry.className = "log-entry"
    entry.innerText = message
    journal.prepend(entry)


def input(question=""):
    """Normal input() doesn't work on a webpage, so this version shows a
    pop-up box instead. You use it exactly like the normal input()."""
    try:
        answer = window.prompt(question)
    except Exception:
        answer = None  # some browsers block pop-ups
    if not answer:
        return "Player"
    return answer


def keep_in_range(number):
    """Stats can't go below 0 or above 100."""
    if number < 0:
        return 0
    if number > 100:
        return 100
    return number


# -------------------------------------------------------------
#  GAME SETUP - this part runs once, when the page loads
# -------------------------------------------------------------

# TODO 1: This list only has one name. Add at least 4 more dog names.
#         Every name needs "quotes" and a comma between names.
#         Example: ["Rex", "Biscuit", "Luna"]
dog_names = ["Rex","Biscuit", "Luna","rock ruff"]



# TODO 2: Right now the dog is always the first name in the list.
#         Change this line so the game picks a RANDOM name instead.
#         Hint: random.choice(dog_names)
dog_name = random.choice(dog_names)


# TODO 3: Ask the player for their name using input().
#         A pop-up box will appear when the page loads.
#         Hint: player_name = input("What is your name? ")
player_name = input("what do you want your nick name to be")


# TODO 4: Every dog starts at 50. Pick your own starting numbers
#         between 0 and 100. Maybe your dog starts out very hungry?
happiness = random.randint(20,100)
hunger = random.randint(20,100)
energy = random.randint(20,100)


# TODO 5: Use print() to write a welcome message to the console.
#         Include the player's name AND the dog's name.
#         Hint: print("Welcome", player_name, "! Your dog is", dog_name)
print("Welcome", player_name, "! Your dog is", dog_name)



# -------------------------------------------------------------
#  UPDATE THE SCREEN - shows the latest stats on the page
# -------------------------------------------------------------

def update_screen():
    show("happiness", happiness)
    show("hunger", hunger)
    show("energy", energy)
    set_bar("happiness-bar", happiness)
    set_bar("hunger-bar", hunger)
    set_bar("energy-bar", energy)

    # TODO 9: Use a FOR LOOP to make one heart for every 20 happiness.
    #         Example: 60 happiness = 3 hearts, 100 happiness = 5 hearts.
    #         Hint:
    #             for i in range(happiness // 20):
    #                 hearts = hearts + "❤️"
    hearts = ""
    for i in range(happiness// 20):
        hearts = hearts + "❤️"

    show("hearts", hearts)


def say(message, icon):
    """Show a message in the dialogue box AND add it to the Journal."""
    show("status-text", message)
    show("status-icon", icon)
    add_to_journal(message)


# -------------------------------------------------------------
#  RANDOM EVENTS - a surprise that sometimes happens after an action
# -------------------------------------------------------------

def random_event():
    global happiness

    # TODO 10: Add at least 3 more surprises to this list.
    #          Then write a FOR LOOP that prints every event in the list
    #          to the console, so you can check they're all there.
    #          Hint:
    #              for event in events:
    #                print(event)
    events = [
        dog_name + " found a stick!",
    ]
    for event in events:
        print(event)

    # 1 in 4 chance that a surprise happens (this part is done for you)
    if random.randint(1, 4) == 1:
        surprise = random.choice(events)
        happiness = keep_in_range(happiness + 5)
        say(surprise, "✨")
        update_screen()


# -------------------------------------------------------------
#  BUTTON ACTIONS - the webpage runs these when buttons are clicked
#  ("global" lets the function change the stats from GAME SETUP.)
# -------------------------------------------------------------

def feed(event):
    global happiness, hunger, energy

    # TODO 6: Feeding should make the dog LESS hungry and a little happier.
    #         Hint: hunger = keep_in_range(hunger - 20)
    #         Then change happiness the same way.
    hunger = keep_in_range(hunger - 20)
    happiness = keep_in_range(happiness + 5)

    say(dog_name + " ate dinner.", "🍖")
    update_screen()
    random_event()


def play(event):
    global happiness, hunger, energy

    # TODO 7: Playing makes the dog happier, but it uses up energy
    #         and makes the dog hungrier. Change all three stats.
    #         Remember to use keep_in_range() each time!
    happiness = keep_in_range(happiness+15)
    energy = keep_in_range(energy-10)
    hunger = keep_in_range(hunger + 10)
    

    say(dog_name + " chased the ball!", "🎾")
    update_screen()
    random_event()


def rest(event):
    global happiness, hunger, energy

    # TODO 8: Resting gives the dog more energy.
    #         Change energy, then write your own message in say()
    #         below instead of "...". Use the player's name in it.
    #         Hint: dog_name + " took a nap next to " + player_name + "."
    energy = keep_in_range(energy+20)
    hunger = keep_in_range(hunger+20)
    happiness = keep_in_range(happiness-20)
    

    say("...", "💤")
    update_screen()
    random_event()


# -------------------------------------------------------------
#  START THE GAME (already done for you)
# -------------------------------------------------------------

show("dog-name", dog_name)
update_screen()
say(dog_name + " is ready for an adventure, " + player_name + "!", "🐾")
