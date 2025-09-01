from random_word import RandomWords

# Hangman Game
def replace_char(word: str, index: int, new_char: str) -> str:
    if not (0 <= index < len(word)):
        raise IndexError("Index out of range.")
    if len(new_char) != 1:
        raise ValueError("new_char must be a single character.")
    
    return word[:index] + new_char + word[index+1:]

try:
    r = RandomWords()
    word = r.get_random_word()
    print(word)
    incorrect = 0
    count = 0
    blank = ' '.join('_' for i in word)
    while True:
        guess = input('Type and a letter: ')
        if guess in word:
            print('Correct')
            for i in range(len(word)):
                if word[i] == guess:
                    count += 1
                    blank = replace_char(blank, i*2, guess)
            if len(word) == count:
                print(blank)
                print('You win')
                break
        else:
            print('Incorrect')
            incorrect += 1
        if incorrect == 6:
            print('Game Over')
            break
        print(blank)
except Exception as e:
    print(e)