"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Radka Filipová
email: r.filipova@email.cz
"""
import random
import time

def greet_user():
    """Vypíše uvítací zprávu pro hráče."""
    print("Hi there!")
    print("-" * 40)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 40)

def generate_secret_number():
    """Vygeneruje 4místné číslo s unikátními číslicemi, nezačíná nulou."""
    digits = list('0123456789')
    first_digit = random.choice(digits[1:])
    digits.remove(first_digit)
    remaining_digits = digits.copy()
    random.shuffle(remaining_digits)
    number = first_digit + ''.join(remaining_digits[:3])
    return number

def is_valid_guess(guess):
    """Funkce pro kontrolu správného vstupu od uživatele (kontroluje čtyřmístný unikátní číselný řetězec)."""
    if not guess.isdigit():
        return False, "Input contains non-digit characters."
    if len(guess) != 4:
        return False, "Input must be exactly 4 digits."
    if guess[0] == '0':
        return False, "Number cannot start with 0."
    if len(set(guess)) != 4:
        return False, "Digits must be unique."
    return True, ""

def count_bulls_and_cows(secret, guess):
    """Spočítá počet bulls a cows mezi tajným číslem a tipem hráče."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def print_bulls_and_cows(bulls, cows):
    """Vypíše výsledek jednoho kola hádání ve formátu X bulls, Y cows s ohledem na jednotné a množné číslo."""
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")
    print("-" * 40)

def main():
    """Spustí hlavní smyčku hry."""
    greet_user()
    secret = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ").strip()
        valid, error = is_valid_guess(guess)
        if not valid:
            print(f"Invalid input: {error}")
            print("-" * 40)
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret, guess)
        if bulls == 4:
            duration = round(time.time() - start_time, 2)
            print(
                f"Correct, you've guessed the right number in {attempts} guesses!"
                )
            print("-" * 40)
            print(f"That's amazing! Time taken: {duration} seconds")
            break
        else:
            print_bulls_and_cows(bulls, cows)
if __name__ == "__main__":
    main()
