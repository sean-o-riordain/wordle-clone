from collections import Counter

def check_guess(answer: str, guess: str) -> list:
    result = []
    answer_counts = Counter(answer)

    for i, letter in enumerate(guess):
        if letter == answer[i]:
            result.append("green")
            answer_counts[letter] -= 1
        else:
            result.append("gray")
    
    for i, letter in enumerate(guess):
        if letter in answer and answer_counts[letter] > 0 and result[i] == "gray":
            result[i] = "yellow"
            answer_counts[letter] -= 1
            
    return result

