class bfs:
    def __init__(self, node_name):
        self.children = []
        self.node = node_name 

    def addChild(self, name_child):
        self.children.append(bfs(name_child))
        return self

    def BFS(self, arr):
        queue = [self]
        while(len(queue) > 0 ):
            current = queue.pop(0)
            arr.append(current.node)
            for child in current.children:
                queue.append(child)
        return arr