#enter the number to convert to binary and count number of bits
n = 0

#convert to binary and remove 0b prefix
process = (bin(n)).translate(None, "0b")

#prints original output of binary conversion
print bin(n) + "\n\n"

#prints the number of bits
print len(process)
