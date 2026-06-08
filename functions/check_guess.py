from collections import Counter

def check_guess(answer: str, guess: str) -> list:
    result = []
    answer_counts = Counter(answer)
    guess_counts = Counter(guess)
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result.append("green")
            answer_counts[guess[i]] -= 1
        elif guess[i] in answer and answer_counts[guess[i]] > 0:
            result.append("yellow")
            answer_counts[guess[i]] -= 1
        else:
            result.append("gray")
    return result

