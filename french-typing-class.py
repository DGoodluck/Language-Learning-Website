import random
import json
import string
from fuzzywuzzy import fuzz

# Load data from JSON file
with open('phrases.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define proficiency level categories
categories = {'a1': 'A1', 'a2': 'A2', 'b1': 'B1', 'b2': 'B2', 'c2': 'C2', 'slang': 'Slang'}

def get_translation(phrase):
    try:
        print(phrase['English'])
        user_answer = input("Translate this to French: ")
        # Remove punctuation from user_answer and phrase['French']
        user_answer = user_answer.lower().translate(str.maketrans('', '', string.punctuation))
        correct_answer = phrase['French'].lower().translate(str.maketrans('', '', string.punctuation))
        return user_answer, correct_answer
    except KeyError:
        print("An error occurred. Please make sure the phrase dictionary has 'English' and 'French' keys.")
        return None, None

def check_translation(user_answer, correct_answer, phrase):
    if user_answer == correct_answer:
        print("Exactly!")
    else:
        # Calculate the similarity between the user's answer and the first correct answer
        similarity = fuzz.ratio(user_answer, correct_answer)
        if similarity > 95:
            print(f"Good Job, Correct answer: {phrase['French']}")
        # If the similarity is above 80, consider the answer "close"
        elif similarity > 80:
            print(f"Almost there. Correct Answer: {phrase['French']}")
        else:
            print(f"Not quite, Correct Answer: {phrase['French']}")

def translation(phrase):
    user_answer, correct_answer = get_translation(phrase)
    if user_answer is not None:
        check_translation(user_answer, correct_answer, phrase)

while True:
    user_lvl = input("What proficiency level are you? (A1, A2, B1, B2, C2, Slang, or press 'q' to quit) ").lower()

    if user_lvl == 'q':
        break

    if user_lvl in categories:
        phrase = random.choice(data[categories[user_lvl]])
        translation(phrase)
    else:
        print("Invalid Input")
