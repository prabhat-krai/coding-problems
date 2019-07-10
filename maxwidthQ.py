class Node:
    def __init__(self,  data):
        self.data = data
        self.right = None
        self.left = None


def getMaxWidth(root):
    if (root == None):
        return 0 

    max_width = 0 
    q = []
    
    q.insert(0, root)

    while (len(q) > 0):
        count= len(q)

        max_width = max(count, max_width)

        while(count != 0):
            count -= 1
            temp = q[-1]
            q.pop()

            if(temp.left is not None):
                q.insert(0, temp.left)

            if(temp.right is not None):
                q.insert(0, temp.right)

    return max_width



root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(8) 
root.right.right.left = Node(6) 
root.right.right.right = Node(7)  

print(getMaxWidth(root))

