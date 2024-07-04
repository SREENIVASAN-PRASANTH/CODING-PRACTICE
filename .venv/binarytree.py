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
        # if node == None:
        #     return TreeNode(data)
        # if node.data > data:
        #     if node.leftNode is None:
        #         node.leftNode = TreeNode(data)
        #     else:
        #         self.insertNode(node.leftNode,data)
        #
        # elif node.data < data:
        #     if node.rightNode is None:
        #         node.rightNode  = TreeNode(data)
        #     else:
        #         self.insertNode(node.rightNode,data)
        # return node
        if node == None:
            return TreeNode(data)
        if node.data > data:
            node.leftNode = self.insertNode(node.leftNode,data)
        else:
            node.rightNode = self.insertNode(node.rightNode,data)
        return node

    def preorderTraversal(self,node):
        if node == None:
            return
        print(node.data,end = " ")
        self.preorderTraversal(node.leftNode)
        self.preorderTraversal(node.rightNode)

    def level_order_traversal(self):
        queue =  deque([self.root])

        while len(queue) != 0:
            node = queue.popleft()
            print(node.data)
            if node.leftNode:
                queue.append(node.leftNode)
            if node.rightNode:
                queue.append(node.rightNode)
            # queue.popleft()
if __name__ == "__main__":
    a = [1,2,3,5,6,7,8]
    tree = Tree(4)
    for i in a:
        tree.insertNode(tree.root,i)
    tree.preorderTraversal(tree.root)
    print("\n")
    tree.level_order_traversal()

