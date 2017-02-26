import re
def findSumReg(fileName):
    """
    Returns amount of all numbers in the input file. Ignores letters, non-characters 
    like punctuation and spaces.

    fileName: name of input file
    returns: sum of all numbers
    """
    ### TODO
    return sum([int(i) for i in (re.findall(r'\d+',open(fileName).read()))])