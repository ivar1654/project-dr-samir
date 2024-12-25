import heapq

def prim(graph, start):
  
    V = len(graph)
    
   
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

   
    key[start] = 0
    minHeap = [(0, start)] 
    
    while minHeap:
        
        weight, u = heapq.heappop(minHeap)
        
        
        if mstSet[u]:
            continue
        
        
        mstSet[u] = True
        
        
        for v, weight_uv in enumerate(graph[u]):
            if not mstSet[v] and weight_uv < key[v]:
                key[v] = weight_uv
                parent[v] = u
                heapq.heappush(minHeap, (key[v], v))

    
    mst = []
    for i in range(1, V):
        if parent[i] != -1:
            mst.append((parent[i], i, key[i]))  
    
    return mst


graph = [
    [0, 3, 0, 9, 0],
    [2, 0, 7, 6, 4],
    [0, 3, 0, 0, 3],
    [6, 8, 0, 0, 8],
    [0, 5, 4, 5, 0]
]

start_node = 0
mst = prim(graph, start_node)
print("Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"({u}, {v}) -> {weight}")