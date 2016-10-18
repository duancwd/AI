'''
file contains miscellaneous helper functions
'''

def parseStringToArray(string):
    ###
    # this function will take strings in the form '?var constant constant ?var' and convert it to a form understandable by
    # the inference engine, which will look like ['?var', 'constant', 'constant', '?var']
    ###
    word = ""
    string = string
    returnArray = []
    for character in string:
        if character == " ":
            returnArray.append(word)
            word = ""
        else:
            word += character
    if word:
        returnArray.append(word)
    return returnArray

def parseArrayToString(array):
    ###
    # helper function to convert array format back to strings, much easier
    ###
    return " ".join(array)
