import requests
import random
import json
import functions.word_input as word_input
import functions.check_guess as check_guess

url = "https://darkermango.github.io/5-Letter-words/words.json"
response = requests.get(url)
words = json.loads(response.text)["words"]
answer = words[random.randint(0, len(words) - 1)]

guess = ''

game_over = False
guess_count = 0

while answer != guess and not game_over:
    guess = word_input.word_input(words)
    check_result = check_guess.check_guess(answer, guess)
    guess_count += 1
    if guess_count >= 5:
        game_over = True
    print(check_result)

print("\n")
print(answer)
print(guess)
print(check_result)