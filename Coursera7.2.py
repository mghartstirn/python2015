# Coursera Chapter 7: reading + calculating the file opened
# March 22, 2015

"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

filename = raw_input("Enter file name: ")
count = 0
base = 0

try: 
    handler = open(filename)
except:
    print "Invalid File Name"
    exit()

for line in handler : 
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    position = line.find('0')
    number = float(line[position: ])
    base = base + number
average = base / count
print 'Average spam confidence:', average
