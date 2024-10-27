def typing_time(layout, word):
    positions = {letter: pos for pos, letter in enumerate(layout)}
    location = 0
    typed_time = 0

    for letter in word:
        next_loc = positions[letter]
        typed_time += abs(next_loc - location)
        location = next_loc

    return typed_time
    
# skipping error handling
# empty keys? empty word? repeated letters in keys?

