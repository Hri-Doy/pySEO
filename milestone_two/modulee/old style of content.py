name = input("What is your name: ").capitalize()
print(name)

# Do you know Mr. XYZ. He is one of the best actor in bollywood Industry. His height is 175 CM.
full_name = input("Enter your name: ").capitalize()
pronoun = input("Write He or She: ").capitalize()
profession = input("Enter your profession: ").lower()
industry = input("Enter Industry: ").capitalize()
height = input("Enter height: ")

#article = f'Do you know {full_name}? He is one of the best {profession} in {industry} Industry. His height is {height} CM.'

article = "Do you know " + full_name +"?" + pronoun+" is one of the best actor in "+ industry + "Industry. His height is "+ height+" CM."
print(article)