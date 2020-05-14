import heapq

# Network Delay Time
# https://leetcode.com/problems/network-delay-time/

def networkDelayTime(times, N, K):
    # Just a variation of Dijkstra's
    pq = [(0, K)]

    paths = dict()
    paths[K] = 0 # free to get to starting node

    visited = set()

    while len(pq) > 0:
        distance, node = heapq.heappop(pq)

        if node in visited:
            continue
        else:
            visited.add(node)

        neighbors = [n for n in times if n[0] == node] # I should probably only build this once at the beginning

        for edge in neighbors:
            _, neighbor, neighbor_distance = edge
            total_distance = distance + neighbor_distance
            if neighbor not in paths or total_distance < paths[neighbor]:
                paths[neighbor] = total_distance
                heapq.heappush(pq, (total_distance, neighbor))

    if len(paths.keys()) != N: # check if all paths have been visited, if not return -1
        return -1

    return max(paths.values()) # since we care about all nodes receiving, it is the max distance from the starting node

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

print(networkDelayTime(times, N, K))