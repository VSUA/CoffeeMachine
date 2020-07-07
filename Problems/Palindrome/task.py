word = list(input())
word_reverse = word[::-1]
i = 0

while i < (len(word) / 2):
    if word[i] != word_reverse[i]:
        print("Not palindrome")
        break
    i += 1
else:
    print("Palindrome")