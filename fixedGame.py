import random

def hangman():
    words = ["Vert", "Chercheur", "Mercure", "Corde", "Plomb", "Scalpel", "Tremblement", "Fibre", 
             "Bleu", "Chemin", "Parcours", "Enterrement", "Chapelle"]
    secret_word = random.choice([w for w in words if len(w) == 6]).upper()
    guessed_word = ["_"] * len(secret_word)
    retries = 0
    max_attempts = 6
    guessed_letters = set()
    
    print("Hangman v1")
    print(f"Essayez de deviner un mot de {len(secret_word)} lettres en moins de {max_attempts} tentatives échouées.")
    
    while retries < max_attempts:
        print(" ".join(guessed_word))
        guess = input(f"Tentative {retries + 1} : ").strip().upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        if guess in guessed_letters:
            print("Vous avez déjà essayé cette lettre.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            retries += 1
        
        if "_" not in guessed_word:
            print("Bravo ! Vous avez trouvé le mot :", secret_word)
            return
    
    print("Le joueur a perdu. Le mot était :", secret_word)

if __name__ == "__main__":
    hangman()