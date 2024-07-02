from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

class Tree:
    def __init__(self,data):
        self.root = TreeNode(data)

    def insertNode(self,node,data):
        if node == None:
            return TreeNode(data)
        if node.data > data:
            if node.leftNode is None:
                node.leftNode = TreeNode(data)
            else:
                self.insertNode(node.leftNode,data)

        elif node.data < data:
            if node.rightNode is None:
                node.rightNode  = TreeNode(data)
            else:
                self.insertNode(node.rightNode,data)

if __name__ == "__main__":
    a = deque([4,1,2,3,5,6,7,8])
    tree = Tree(a[0])
    tree.insertNode(tree.root,a[1])
    tree.insertNode(tree.root,a[2])

    print(tree.root.leftNode.data)
    print(tree.root.leftNode.rightNode.data)


