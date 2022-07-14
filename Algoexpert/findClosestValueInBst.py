class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    return findClosestValueInBSTHealper(tree, target, float("inf"))

def findClosestValueInBSTHealper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHealper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHealper(tree.right, target,closest)
    else:
        return closest

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
expected = 13
actual = findClosestValueInBst(root, 12)
print(actual)