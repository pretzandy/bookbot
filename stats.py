def get_num_words(text):
    word = text.split()   #splits everything up to word, is, a,
    return len(word)    #len will use the split up words and do a count

def get_num_chars(text):
    word = text.lower()  #forces everything to be lower case aka uniform
    num_chars = {}    #must have a dictionary for this funtion not a [] list
    for char in word:  #lets loop through the characters in the word
        if char in num_chars:   #if it can find the character in the dict then lets add 1
            num_chars[char] += 1
        else:
            num_chars[char] = 1    #first instance of the character lets make it a count of 1
    return num_chars

def get_sorted(num_chars):
    sorts = []
    for char in num_chars: #loops over the charcters
        if char.isalpha(): #only work if it's a letter
            count=num_chars[char] #pulls the count from the dictionary
            sorts.append((char, count))
    def sort_umm(dict):  #made only for the sort
        return dict[1]   #this tells it to look at the tuple[1] aka the count in the list
    
    sorts.sort(reverse=True, key=sort_umm) #reverse make it go largest to smallets and the key tell it how to sort
    sorted_sorts = ""         #lets turn this into a string
    for char, count in sorts: # pull and loop over the tuple data out of the list
        sorted_sorts += f"{char}: {count}\n" # add an addition line here
    if len(sorted_sorts) !=0:
        sorted_sorts=sorted_sorts[:-1]

    return sorted_sorts