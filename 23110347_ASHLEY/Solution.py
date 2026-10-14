# Class Solution:
#   def shortestpath():
#     a=[]
#     for i in x:
#       a[i[0]].append(a[i[1]])
#       a[i[1]].append(a[i[0]])
#     st=[]
#     end=[]
#     while(run):
      







# X=the array of inputs given for the edges
# start = starting node 
# end = ending node
# Algo - 
      # Edges are stored in the form so that they are present in each other's end points array indices
      # The nodes to be traverse from the end and start point in greedy approach or heuristics can be applied by running through the graph once to calcuate their closest points to the end point.
      # When they nodes traversal path meet, that is one of the solution which can be found by this approach. But smallest or optimal path will not be confirmed. And this doesn't solve the case where we have a disconnected graph.
