#chapter 8 with Dr. Chuck
#this program reads a string of emails and counts how many are in the file- 
#it's asking specifically for a "From" line, so this could work with "To" as well



fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line == '' : continue #if the line is plank, ignore
    words = line.split()
    if not line.startswith('From ') : continue #if the line does not start with FROM, ignore
    count = count + 1
    print words[1]
    
print "There were", count, "lines in the file with From as the first word"
