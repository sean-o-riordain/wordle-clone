import requests
import random
import json

url = "https://darkermango.github.io/5-Letter-words/words.json"
response = requests.get(url)
words = json.loads(response.text)["words"]


print(len(words))

word_index = random.randint(0, len(words) - 1)
print(words[word_index])
