#Chapter 8 from Coursera's class taught by Dr. Chuck
#this asks for a file, opens it, reads it, and puts the words in the file into an ABC ordered list (without making duplicates)
#this would be useful for shorter text


fname = raw_input("Enter file name: ")
fh = open(fname)
t = list()
for line in fh:
    line = line.rstrip() #strip out spaces
    words = line.split() #split the lines into individual words
    for word in words: 
        if word not in t:
            t.append(word) #for every word that isn't already in the list, add it
t.sort() #put the list in ABC order
print t
