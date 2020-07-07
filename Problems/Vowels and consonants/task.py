word = input().strip()
vowel = "aeiou"

for letter in word:
    if not letter.isalpha():
        break
    elif letter in vowel:
        print("vowel")
    else:
        print("consonant")
