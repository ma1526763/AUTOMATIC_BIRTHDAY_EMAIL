import random
def random_quote():
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        return random.choice(all_quotes)
def random_letter(name):
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_data = letter.read()
        return letter_data.replace("[NAME]", name)
