phrase = list(input())
result_phrase = []
for char_num, char in enumerate(phrase):
    if char.isupper() and char_num == 0:
        result_phrase.append(char.lower())
    elif char.isupper():
        result_phrase.append('_' + char.lower())
    else:
        result_phrase.append(char)
print(''.join(result_phrase))
