"""
A array is given where 0 is land and 1 is water. 
We want to find all the rivers and length of each. 
A list of all the lengths should be returned.
"""

def river_sizes(land):
    sizes = []
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[i])):
            if visited[i][j]:
                continue
            river_sizes_helper(i, j, land, visited, sizes)
    return sorted(sizes)




def river_sizes_helper(i, j, land, visited, sizes):
    curr_size = 0
    nodes = [[i,j]]
    while(len(nodes)):
        currentNode = nodes.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if (land[i][j] == 0):
            continue
        curr_size += 1
        unvisited_nodes = getUnvisited(i, j, land, visited)
        for node in unvisited_nodes:
            nodes.append(node)
    if (curr_size > 0):
        sizes.append(curr_size)


def getUnvisited(i, j, land, visited):
    unvisited_nodes = []
    if ( i > 0 and not visited[i - 1][j]):
        unvisited_nodes.append([i - 1, j])
    if ( i < len(land) - 1 and not visited[i + 1][j]):
        unvisited_nodes.append([i+1 , j])
    if ( j > 0 and not visited[i][j - 1]):
        unvisited_nodes.append([i, j - 1])
    if ( j < len(land[0]) - 1 and not visited[i][j + 1]):
        unvisited_nodes.append([i, j + 1])
    return unvisited_nodes


def test():

    land = [[1,0,0,1,0,1],
            [1,0,1,0,0,0],
            [0,0,1,0,1,0],
            [1,0,1,0,1,0],
            [1,0,1,1,0,1]]
    assert river_sizes(land) == [1,1,1,2,2,2,5]

    land = [[1,0,0,1]]
    assert river_sizes(land) == [1,1]

    print("Test passed")

test()