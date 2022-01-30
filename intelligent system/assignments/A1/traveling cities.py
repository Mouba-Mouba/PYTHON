# Python3 program to implement traveling salesman 
# problem using naive approach. 
from sys import maxsize 
from itertools import permutations
V = 8

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

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
	graph = [[0,24,5000,5000,5000,48,22,5000],
                 [24,0,16,5000,5000,5000,30,47],
                 [5000,16,0,30,5000,5000,5000,43],
                 [5000,5000,30,0,45,5000,5000,25],
                 [5000,5000,5000,45,0,9,5000,32],
                 [48,5000,5000,5000,9,0,30,34],
                 [22,30,5000,5000,5000,30,0,15],
                 [5000,47,43,25,32,34,15,0]] 
	s = 0
	print(travellingSalesmanProblem(graph, s))
