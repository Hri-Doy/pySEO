'''
In string, the usage of:
# split
# rsplit
# lsplit
# splitlines
'''

txt = "hello, my name is Runy, I am 20 years old"
print(txt.split()) 
# If nothing is mentionend, it creats a list. 

# Define a comma
print(txt.split(","))
# Define a emoji
print(txt.split("b"))

book_one = "Jean-Paul Sartres Nausea follows Antoine Roquentin, a lonely historian living in Bouville. He begins to feel a strange, physical disgust — a feeling he calls nausea. Everyday objects, people, even his own hands start to disturb him."

print(book_one.split(",")) # Comma


# use maxsplit=[number] to limit the split
# Remember, maxsplit=[number] starts from 0 always

text_two = "Existence feels heavy, Objects breathe quietly, Meaning slips away, Roquentin feels lost, Time moves slowly, Streets whisper nothing. Hands tremble softly."

print(text_two.split(',', maxsplit=2)) # maxsplit=[number] is used to limit the split 


text_three = "Existence heavy, objects breathe, meaning fades, Roquentin lost, time slows, streets whisper, hands tremble, thoughts scatter, nausea grows, truth cold, silence answers, freedom creates, he writes, he exists."
print(text_three.rsplit(',', maxsplit=5))


poem = "Shadows fall,\n voices fade, hearts ache, \ndreams break, eyes wander, stars dim,\n winds whisper"
print(poem.splitlines(False)) # The False value don't show the line breaker \n but true value does.

rhyme = "Nights linger,\n fear grows, hope flickers,\n truth hides,\n time drifts,\n love fades,\n silence stays"
print(poem.splitlines(True)) # The False value don't show the line breaker \n but true value does.

