def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
            print("vowel")
    return count

print(count_vowels("Moumita"))
