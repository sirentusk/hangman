import random

random_word = random.choice(["apple", "banana", "cherry", "date", "elderberry"])
correct_letters = {}
no_count = 0
yes_count = 0

def handle_click(letter):
    global correct_letters
    global random_word
    global no_count
    global yes_count

    # Counts the yes answers in the length of the random word and prints a count
    if yes_count >= len(random_word):
        progress_fraction = f" ({yes_count}/{len(random_word)})"
        pyscript.write("result", "You guessed right!")
        return

    # Checks the letter and prints no and it's count
    if letter not in random_word:  
        no_count += 1
        result = "No"
        progress_fraction = f" ({no_count}/10)"
        pyscript.write("result", result + progress_fraction)

    # Checks the letter is new and not a duplicate correct letter
    else:
        if letter not in correct_letters:
            correct_letters[letter] = random_word.count(letter)
            yes_count += random_word.count(letter)
        result = "Yes"
        progress_fraction = f" ({yes_count}/{len(random_word)})"
        pyscript.write("result", result + progress_fraction)

    # Counts the no answers to a maximum
    if no_count >= 10:
        pyscript.write("result", "Maximum number of clicks reached.")
        return
    
    # Counts all the letters are chosen in the random word
    if yes_count == len(random_word):
        pyscript.write("result", f"You guessed right! {random_word}")

# Shows the chosen random word
def reveal_word(reveal):
    global random_word
    pyscript.write('result', random_word)