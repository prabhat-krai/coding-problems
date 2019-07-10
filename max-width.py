class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getWidth(level, root):
    if(root == None):
        return 0 
    if(level == 1):
        return 1
    
    elif(level > 1):
        return getWidth(level - 1, root.left) + getWidth(level - 1, root.right)

def height(root):
    if(root == None):
        return 0 

    else: 
        l_height = height(root.left) 
        r_height = height(root.right) 

    return (l_height + 1) if (l_height > r_height) else r_height + 1


def getMaxWidth(root):
    maxWidth = 0
    h = height(root)

    for i in range(0, h + 1):
        width = getWidth(i, root)
        if(width > maxWidth):
            maxWidth = width
    
    return maxWidth


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(8) 
root.right.right.left = Node(6) 
root.right.right.right = Node(7)  


print (getMaxWidth(root))