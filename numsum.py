import re
def findSumReg(fileName):
    """
    fileName: name of input file
    returns: sum of all numbers
    """
    ### TODO
    return sum([int(i) for i in (re.findall(r'\d+',open(fileName).read()))])

if __name__ == '__main__':
    test1 = findSumReg("321.txt")
    assert '44' == str(test1)[:2] and '22' == str(test1)[-2:]
    print "1. Amount of test 1 is: " + str(test1)

