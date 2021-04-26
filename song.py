
# save strings as variables and then join them together
# use f-strings to format so the main lyric stays the same but the ending changes
# at the end of every chunk: I don't know why she swallowed the fly. Perhaps she'll die.

################################################################

# Here are my initial ideas:

# part_verse_1 = "I know an old lady who swallowed a "
#   full_verse_1 = part_verse_1 + "fly"
#   return full_verse_1

# def verse2():
#   part_verse_2 = part_verse_1
#   end_verse_2 = part_verse_2 + "spider"
#   return(end_verse_2)
# print(end_verse_1)

################################################################

# Here I am thinking about how to do the same lyrics but using a dictionary with key and value pairs

# variations = {
#         "verse_2": ["bird", "How absurd to swallow a bird!"], 
#         "verse_3": ["cat", "Imagine that, to swallow a cat!"]
#           }

################################################################

animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow"]
refrain = "I know an old lady who swallowed a"
line_7 = "I know an old lady who swallowed a horse. She's dead, of course!"
line_6 = "She swallowed the cow to catch the goat."
line_5 = "She swallowed the goat to catch the dog."
line_4 = "She swallowed the dog to catch the cat."
line_3 = "She swallowed the cat to catch the bird."
line_2 = "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
line_1 = "She swallowed the spider to catch the fly."
close = "I don't know why she swallowed the fly. Perhaps she'll die. "

# This was my first working attempt with an f-string, getting the list of animals to repeat with the same refrain and close.
# def verse(animal):
#     for animal in animals:
#         print(f"{refrain} {animal}. {close}")      
# verse(refrain)

# Now here is basic working code for the assignment that at least uses f-strings

def verse_1(spider):
    print("")
    print(f"{close}")
    print("")
    print(f"{refrain} spider.") 
    print(f"It wriggled and jiggled and tickled inside her.")
    print(f"{line_1} {close}")
    print("")
verse_1(refrain)

def verse_2(bird):
    print(f"{refrain} bird.") 
    print("How absurd to swallow a bird!")
    print("She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.") 
    print(f"{line_1} {close}")
    print("")
verse_2(refrain)        

def verse_3(cat):
    print(f"{refrain} cat.") 
    print("Imagine that, to swallow a cat!")
    print(f"{line_2}")
    print(f"{line_1} {close}")
    print("")
verse_3(refrain)

def verse_4(dog):
    print(f"{refrain} dog.")
    print("What a hog, to swallow a dog!")
    print(f"{line_4}")
    print(f"{line_3}")
    print(f"{line_2}")
    print(f"{line_1} {close}")
    print("")
verse_4(refrain)    

def verse_5(goat):
    print(f"{refrain} goat.")
    print("Just opened her throat and swallowed a goat!")
    print(f"{line_5}")
    print(f"{line_4}")
    print(f"{line_3}")
    print(f"{line_2}")
    print(f"{line_1} {close}")
    print("")
verse_5(refrain)

def verse_6(cow):
    print(f"{refrain} cow.")
    print("I don't know how she swallowed a cow!")
    print(f"{line_6}")
    print(f"{line_5}")
    print(f"{line_4}")
    print(f"{line_3}")
    print(f"{line_2}")
    print(f"{line_1} {close}")
    print("")
    print(f"{line_7}")
verse_6(refrain)

# start here to put verse functions within the song function 
def song(verses):
    pass




##########################################################
# this code is to start making an INDEX for the animals

# for i in range(len(animals)):
#     print(i)
#     print(animals[i], animals[i - 1])





# def song(verses):
#     for line in verses:
#         print(verse_1 + verse_2 + verse_3)

# song(verse_1)

# try a third method
# def song (group, verse):
#     for animal in group:
#         if my_verse == "first":
#             print(f"She swallowed the {animal} to catch the fly.")
#         elif my_verse == "second":
#             print(f"She swallowed the {animal} to catch the spider.")
#         else:
#             print("I know an old lady who swallowed a horse. She's dead, of course!")

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









