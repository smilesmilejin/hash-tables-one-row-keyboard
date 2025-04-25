# def typing_time(layout, word):
#     pass

########################### Method 1 use: live code
# # time complexity: n * k ( n length of layout, and w is the length of word)
# Space complexity: constant O(1)
# def typing_time(layout, word):
#     curr_pos = 0
#     total_time = 0
#     for letter in word:
#         # find letter position
#         letter_pos = 0
#         for key in layout:
#             if key == letter:
#                 break

#             letter_pos += 1
    
#         # letter_pos is the position of the next letter
#         time = abs(letter_pos - curr_pos)
#         total_time += time

#         curr_pos = letter_pos
    
#     return total_time


########################### Method 2 use: live code using dict
# time complexity: n + k ( n length of layout, and w is the length of word)
# Space complexity: linear O(n), n is the size of layout
def typing_time(layout, word):
    curr_pos = 0
    total_time = 0

    letter_positions = {}
    for index, key in enumerate(layout):
        letter_positions[key] = index
            
    for letter in word:
        # find letter position
        letter_pos = letter_positions[letter]
    
        # letter_pos is the position of the next letter
        time = abs(letter_pos - curr_pos)
        total_time += time
        curr_pos = letter_pos
    
    return total_time



########################## Method 3 self try: passed the test
# time complexity: 
# def typing_time(layout, word):
#     curr_pos = 0
#     total_time = 0
#     for letter in word:
#         # find letter position
#         letter_pos = 0
#         for i in range(len(layout)):
#             if layout[i] == letter:
#                 letter_pos = i
    
#         # letter_pos is the position of the next letter
#         time = abs(letter_pos - curr_pos)
#         total_time += time

#         curr_pos = letter_pos
    
#     return total_time


# ########################## Method 4 self try passed the test
# # Time Complexity O(n + k)
# def typing_time(layout, word):
#     layout_map = {}
#     for index in range(len(layout)):
#         layout_map[layout[index]] = index
    
#     curr_pos = 0
#     total_time = 0
#     for letter in word:
#         total_time += abs(layout_map[letter] - curr_pos)
#         curr_pos = layout_map[letter]
    
#     return total_time

# skipping error handling
# empty keys? empty word? repeated letters in keys?

