# def greet(first_name, last_name):
#     msg = f'Howdy, {first_name} {last_name}'
#     return msg
# output = greet('Abdul', 'Aoual')
# print(output)

def add(a, b):
    sum = a+b
    return sum
output = add(12, 25)
print(output)

#Salman Khan is an actor. He is 56 years old.
def bio(name, profession, gender, age):
    if gender.lower() == "male":
        pronoun = "He"
    else:
        pronoun = "She"
    sentence = f'{name} is an {profession}. {pronoun} is {age} years old.'
    return sentence
actor = bio('Salman Khan', 'actor', 'male', '56')
print(actor)