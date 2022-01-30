""" MOHAMED MOUBARAK MOHAMED MISBAHOU MKOUBOI (1820705)"""
# Python3 program to implement traveling cities 
# problem using naive approach. 
from sys import maxsize 
from itertools import permutations
V = 8

# implementation of traveling Cities Problem 
def travellingCitiesProblem(graph, s): 

	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	# store minimum weight Hamiltonian Cycle 
	min_path = maxsize 
	next_permutation = permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		# update minimum 
		min_path = min(min_path, current_pathweight) 
		
	return min_path 


# Driver Code 
if __name__ == "__main__": 

	# matrix representation of graph 
	graph = [[0,24,100,100,100,100,48,22],
			 [24,0,16,100,47,100,100,30],
			 [100,16,0,30,43,100,100,100],
			 [100,100,30,0,25,45,100,100],
		     [100,47,43,25,0,32,34,15],
			 [100,100,100,45,32,0,9,100],
			 [48,100,100,100,34,9,0,30],
			 [22,30,100,100,15,100,30,0]]
	s = 0
	print(travellingCitiesProblem(graph, s))
