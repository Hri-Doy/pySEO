import random

full_name = input("Enter a name: ").capitalize()
pronoun = input("Enter pronoun: ").capitalize()
profession = input("Enter profession: ").lower()
industry = input("Enter industry: ").capitalize()

first_sentence = [
    f"Do you know {full_name}?",
    f"Have you heard the name of {full_name}?",
    f"Are you familiar with {full_name}?"
    f"Do you recognize the name {full_name}?"
    f"Have you come accross {full_name}?"  
]

second_sentence = [
    f"{pronoun} is one of the best {profession} in the {industry} industry.",
    f"{pronoun} is a famous {profession} in the Dallywoood industry.",
    f"{pronoun} is one of the top {profession} in the {industry} industry.",
    f"{pronoun} is a renowned {profession} in the {industry} industry.",
    f"{pronoun} is a celebrated {profession} in the {industry} industry."
]

# {1,2,3} {1, 2,3} = 11, 12, 13, 21, 22, 23, 31, 32, 33

paragraph = random.choice(first_sentence) + random.choice(second_sentence)
print(paragraph)