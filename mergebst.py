class Tree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

bst_1 = []
bst_2 = []
def getSortedBst(root, bst):

    if(root == None):
        return
    getSortedBst(root.left)
    bst.append(root.value)
    getSortedBst(root.right)

    return bst

bst_1 = getSortedBst(root1, bst_1)
bst_2 = getSortedBst(root2, bst_2)

def mergeBstIntoList(bst_1, bst_2):
    i = 0
    j = 0
    final_bst = []
    while (i < len(bst_1) or j < len(bst_2)):
        if(bst_1[i] < bst_2[j]):
            final_bst.append(bst_1[i])
            i += 1
        else:
            final_bst.append(bst_2[j])
            j += 1

    return final_bst

final_bst = mergeBstIntoList(bst_1, bst_2)



