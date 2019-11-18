class Node:  #define the structure of our nodes
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
       
def printkDistanceNodeDown(root, k): 
      
    if root is None or k< 0 : 
        return 
     
    if k == 0 : 
        print (root.data)  
        return 
      
    printkDistanceNodeDown(root.left, k-1) 
    printkDistanceNodeDown(root.right, k-1) 
  
def printkDistanceNode(root, target, k): 
    
    if root is None: 
        return -1
 
    if root == target: 
        printkDistanceNodeDown(root, k) 
        return 0 

    dl = printkDistanceNode(root.left, target, k) 

    if dl != -1: 
        if dl +1 == k : 
            print (root.data) 
      
        else: 
            printkDistanceNodeDown(root.right, k-dl-2) 
   
        return 1 + dl 
  
    dr = printkDistanceNode(root.right, target, k) 
    if dr != -1: 
        if (dr+1 == k): 
            print (root.data)
        else: 
            printkDistanceNodeDown(root.left, k-dr-2) 
        return 1 + dr 
  

    return -1
  
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
target = root.left.right 

printkDistanceNode(root, target, 2) 