class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        clone_root = self.helper(node, visited)
        
        
        return clone_root
                    
                    
    def helper(self, node, visited):        
        if not node:
            return None
        
        if node in visited:
            return visited[node]
        
        if not node.neighbors:
            return Node(node.val)
        
        
        clone = Node(node.val)
        
        visited[node] = clone
        
        for neighbor in node.neighbors:            
            clone_neighbor = self.helper(neighbor, visited)
            
            clone.neighbors.append(clone_neighbor)
        
        return clone