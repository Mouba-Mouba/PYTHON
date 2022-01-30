# MOHAMED MOUBARAK MOHAMED MISBAHOU MKOUBOI (1820705)
# ISLAM MD SHARIFUL (1720601)
'''
1) Using the file distance.py, compute the distance between the following words:
 - translating vs traversing
 - precaution vs prevention
 - reliability vs responsibility 
'''
def iterative_levenshtein(s, t):
    """ 
        iterative_levenshtein(s, t) -> ldist
        ldist is the Levenshtein distance between the strings 
        s and t.
        For all i and j, dist[i,j] will contain the Levenshtein 
        distance between the first i characters of s and the 
        first j characters of t
    """

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    # source prefixes can be transformed into empty strings 
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i

    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution

    for r in range(rows):
        print(dist[r])
    
 
    return dist[row][col]

print("\ntranslating vs traversing")
print(iterative_levenshtein("translating", "traversing"))
print("\nprecaution vs prevention")
print(iterative_levenshtein("precaution", "prevention"))
print("\nreliability vs responsibility")
print(iterative_levenshtein("reliability", "responsibility"))