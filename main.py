from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    Finds the shortest path between 'start' and 'goal' in an unweighted graph
    using Breadth-First Search (BFS).

    Args:
        graph (dict): The graph represented as an adjacency list.
        start: The starting node.
        goal: The destination node.

    Returns:
        list: The shortest path from start to goal as a list of nodes, 
              or an empty list if no path exists, or if start/goal are missing 
              from the graph keys.
    """

    # --- Initial Checks for Missing or Trivial Nodes ---

    # 1. If 'start' is not a key in the graph, we can't begin.
    # Note: If start == goal, we check if it's a known node in the graph.
    if start not in graph:
        return []

    # 2. If 'goal' is not a key in the graph, we can't reach it.
    if goal not in graph:
        return []

    # 3. Handle the trivial case where the start and goal are the same node.
    if start == goal:
        return [start]
    
    # --- BFS Implementation ---

    # Queue stores the paths explored so far (list of nodes). 
    # Starts with the path containing only the start node.
    queue = deque([[start]])
    
    # Keep track of visited nodes to prevent cycles and redundant work.
    visited = {start}

    while queue:
        # Dequeue the oldest path
        path = queue.popleft()
        node = path[-1] # The last node in the current path
        
        # Explore neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                
                # Check if the neighbor is the goal
                if neighbor == goal:
                    # Found the shortest path, return immediately
                    return path + [neighbor]
                
                # If not the goal, mark as visited and enqueue the new path
                visited.add(neighbor)
                queue.append(path + [neighbor])

    # If the queue is exhausted and the goal was never reached
    return []