#python 3.5.2

import re

def Main():

    line = "I think I understand regular expressions"
    
    matchResult = re.match("think" , line, re.IGNORECASE|re.MULTILINE)
    if matchResult:
        print("Match Found: " + matchResult.group())
    else:
        print("No match was found")
        
    searchResult = re.search("think" , line, re.IGNORECASE|re.MULTILINE)
    if searchResult:
        print("Search Found: " + searchResult.group())
    else:
        print("Nothing found in search")
        
      
if __name__ == '__main__':
    Main()

    
'''
OUTPUT:

No match was found
Search Found: think

'''