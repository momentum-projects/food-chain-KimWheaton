
# save strings as variables and then join them together
# use f-strings to format so the main lyric stays the same but the ending changes
# at the end of every chunk: I don't know why she swallowed the fly. Perhaps she'll die.


# part_verse_1 = "I know an old lady who swallowed a "
#   full_verse_1 = part_verse_1 + "fly"
#   return full_verse_1

# def verse2():
#   part_verse_2 = part_verse_1
#   end_verse_2 = part_verse_2 + "spider"
#   return(end_verse_2)

# print(end_verse_1)

refrain = "I don't know why she swallowed the "
animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow"]

def verse(animal):
    for animal in animals:
        print(f"{refrain}{animal} perhaps she'll die.")

verse(refrain)

# try a different method 
verse_1 = "She swallowed the spider to catch the fly."
verse_2 = "She swallowed the bird to catch the spider."
verse_3 = "She swallowed the cat to catch the bird."

def song(verses):
    for line in verses:
        print(verse_1 + verse_2 + verse_3)

song(verse_1)

# try a third method
# def song (group, verse):
#     for animal in group:
#         if my_verse == "first":
#             print(f"She swallowed the {animal} to catch the fly.")
#         elif my_verse == "second":
#             print(f"She swallowed the {animal} to catch the spider.")
#         else:
#             print("The song continues")

# song(animals, my_verse)
 


# line_1 = "I don't know why she swallowed the fly. Perhaps she'll die."

# line_2 = "I know an old lady who swallowed a spider."
# line_3 = "It wriggled and jiggled and tickled inside her."
# line_4 = "She swallowed the spider to catch the fly."
# repeat_line_1 = "I don't know why she swallowed the fly. Perhaps she'll die."

# verse_2 = line_2 + line_3 + line_4 + line_1

# line_5 = "I know an old lady who swallowed a bird."
# line _6 = "How absurd to swallow a bird!"
# line_7 = "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
# repeat_line_4 = "She swallowed the spider to catch the fly."
# repeat_line_1 = I don't know why she swallowed the fly. Perhaps she'll die."

# verse_3 = line_5 + line_6 + line_7 + line_4 + line_1









