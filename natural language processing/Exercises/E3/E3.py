import re

'''Find a regular expression corresponding to the language of all strings over 
the alphabet { a, w } that contain exactly two a’'''

Question_1 = "The world war has done many dameges"
print(re.search("a+.+a", Question_1))
print(re.search("w", Question_1))

'''Find a regular expression corresponding to the language of all strings over 
the alphabet { a, w } that do not end with wa'''

Question_2 = "after the end of the world war, everything became normal"
print(re.search("wa$", Question_1))
