# Check vowels in a word

word = "Santa Islma Runy"
vowels = "aeiou"
count = 0
for letter in word.lower():
    if letter in vowels:
        print("vowel")
        count += 1
        
print("total vowel: ", count)

def cunt_vowels(word):
    vowels = 'aeiou'
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

print(cunt_vowels("She is Runy aaaaaaaa"))