import requests
import random
import json
import functions.word_input as word_input
import functions.check_guess as check_guess

url = "https://darkermango.github.io/5-Letter-words/words.json"
response = requests.get(url)
words = json.loads(response.text)["words"]
answer = 'anvil' #words[random.randint(0, len(words) - 1)]

guess = ''

while answer != guess:
    guess = word_input.word_input(words)
    check_result = check_guess.check_guess(answer, guess)
    print(check_result)

print("\n")
print(answer)
print(guess)
print(check_result)