# Count vowle using range

# word = "apple"
# vowels = "aeiou"
# count = 0

# for letter in word.lower():
#     if letter in vowels:
#         print("Vowel")
#         count = count + 1
# print("Total vowel: ", count)


def cunt_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

print(cunt_vowels("Hapaeiaapy"))