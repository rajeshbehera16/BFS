from collections import deque
graph = {
   'A': ['B', 'C'],
   'B': ['A', 'D', 'E'],
   'C': ['A', 'F'],
   'D': ['B'],
   'E': ['B', 'F'],
   'F': ['C', 'E']
}
start = 'A'
queue = deque([start]) 
visited = set([start])  

while queue:
   node = queue.popleft()  
   print(node, end=" ")   
  
   for neighbor in graph[node]:
       if neighbor not in visited:
           visited.add(neighbor)  
           queue.append(neighbor) 
   