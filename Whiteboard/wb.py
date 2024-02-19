# Write a function that takes in a string of one or more words
# Return the same string, but with all of the words with 5 or more letters reversed

input = "It is monday"
output = "It is yadnom"

input = "Do not flip me"
output = "Do not flip me"

input = "Monkey writes really elegant code"
output = "syeknoM setirw yllaer tnagele code"


def reversed(str):
    listy = []
    for i in str.split():
        if len(i) >= 5:
            listy.append(i[::-1])  # <----- use splicing to reverse the word 
            print(listy)
        else:
            listy.append(i)
    return (" ").join(listy)
            
            

print(reversed("It is monday"))
print(reversed("Do not flip me"))
print(reversed("Monkey writes really elegant code"))

# Time Complexity: O(n*k) due to the splicing inside of the for loop
# Space Complexity: Linear


# William's answer:
def lettersreversed(racecar):
    ferrari = []
    split_words = racecar.split()
    print(split_words)
    for word in split_words:
        if len(word) >=5:
            ferrari.append(word[::-1])
        else:
            ferrari.append(word)
    print(ferrari)
    porsche = " ".join(ferrari)
    return porsche
print(lettersreversed("It is monday"))
print(lettersreversed("Do not flip me"))
print(lettersreversed("Monkey writes really elegant code"))



