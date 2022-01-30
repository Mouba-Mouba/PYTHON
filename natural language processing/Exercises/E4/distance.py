def distance(target, source, insertcost, deletecost, replacecost):
    
    n = len(target)+1
    m = len(source)+1
    sym = []

    #wfile = open("c:/Users/Public/dist-Leven.dat","w")
       

    # set up dist and initialize values
    # initialize j = 0 for n no. of items in list, i = [j] m no. of times
    dist = [ [0 for j in range(m)] for i in range(n) ]
        
    for i in range(1,n):
        dist[i][0] = dist[i-1][0] + insertcost

    for j in range(1,m):
        dist[0][j] = dist[0][j-1] + deletecost

    # align source and target strings
    for j in range(1,m):

        for i in range(1,n):
            
            inscost = insertcost + dist[i-1][j]
            
            if inscost >= 1:
                sym.append('_')
                #wfile = open("c:/Users/Public/dist-Leven.dat","a")
                #wfile.write('_'+'\t')
                #wfile.close()

            #else:
                
                
            delcost = deletecost + dist[i][j-1]
            if delcost >= 1:
                sym.append('_')
               
            if (source[j-1] == target[i-1]):
                add = 0
            else:
                add = replacecost
                sym.append('|')                
                
            substcost = add + dist[i-1][j-1]
            dist[i][j] = min(inscost, delcost, substcost)
            #print(target[i-1],"\t")
            wfile = open("c:/Users/Public/dist-Leven.dat","a")
            wfile.write(str(target[i-1])+'\t')
            wfile.close()    
        #print("\t")
        #print(source[j-1],"\t")
    #print(sym)
    #return min edit distance    
    return dist[n-1][m-1]

def leven(w1,w2):
    print("levenshtein distance =", distance(w1, w2, 1, 1, 2))
