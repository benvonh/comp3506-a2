"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""

from structures.entry import Entry
from structures.dynamic_array import DynamicArray
from structures.graph import Graph, LatticeGraph
from structures.map import Map
from structures.pqueue import PriorityQueue
from structures.bloom_filter import BloomFilter
from structures.util import Hashable

def bfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
    ) -> tuple[DynamicArray, DynamicArray]:
    """
    Task 2.1: Breadth First Search

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()

    # ALGO GOES HERE
    ############################################################################
    predecessors = DynamicArray()
    Q = PriorityQueue()
    Q.insert_fifo(origin)
    visited_order.append(origin)
    searching = True
    while not Q.is_empty() and searching:
        v: int = Q.remove_min()
        for node in graph.get_neighbours(v):
            w: int = node.get_id()
            if w == goal:
                visited_order.append(w)
                predecessors.append(v)
                searching = False
                break
            if not visited_order.has(w):
                visited_order.append(w)
                predecessors.append(v)
                if not Q.has(w):
                    Q.insert_fifo(w)
    if not searching: # otherwise failed to find goal
        # Backtrack
        backtrack_path = DynamicArray()
        backtrack: int = predecessors[predecessors.get_size() - 1]
        backtrack_path.append(backtrack)
        while backtrack != origin:
            idx = visited_order.index_at(backtrack)
            backtrack = predecessors[idx - 1]
            backtrack_path.append(backtrack)
        # Flip order
        for i in range(backtrack_path.get_size() - 1, -1, -1):
            path.append(backtrack_path[i])
        path.append(goal)
    ############################################################################

    # Return the path and the visited nodes list
    return (path, visited_order)


def dijkstra_traversal(graph: Graph, origin: int) -> DynamicArray:
    """
    Task 2.2: Dijkstra Traversal

    @param: graph
      The *weighted* graph to process (POSW graphs)
    @param: origin
      The ID of the node from which to start traversal.

    @returns: DynamicArray containing Entry types.
      The Entry key is a node identifier, Entry value is the cost of the
      shortest path to this node from the origin.

    NOTE: Dijkstra does not work (by default) on LatticeGraph types.
    This is because there is no inherent weight on an edge of these
    graphs. It should of course work where edge weights are uniform.
    """
    valid_locations = DynamicArray() # This holds your answers

    # ALGO GOES HERE
    ############################################################################
    visited = DynamicArray()

    distances = Map()
    distances[origin] = 0

    pq = PriorityQueue()
    pq.insert(0, origin)

    while not pq.is_empty():
        v: int = pq.remove_min()
        visited.append(v)
        for node, weight in graph.get_neighbours(v):
            u: int = node.get_id()
            new_dist = distances[v] + weight
            old_dist = distances.find(u)

            dist = new_dist if old_dist is None else min(new_dist, old_dist)

            if not visited.has(u):
                pq.update(u, dist)

            distances[u] = dist

    for e in distances.iterate():
        valid_locations.append(e)
    ############################################################################

    return valid_locations


def dfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
    ) -> tuple[DynamicArray, DynamicArray]: 
    """
    Task 2.3: Depth First Search **** COMP7505 ONLY ****
    COMP3506 students can do this for funsies.

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.
    
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()

    # ALGO GOES HERE

    # Return the path and the visited nodes list
    return (path, visited_order)
