class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data): #here we are self so that the self keyword is used to reference the instance of the class
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
                
            else:
                self.left.insert(data)#here we are using recurssion function so that we can add the data either left or right side
                
        else:
            if self.right is None:
                self.right = TreeNode(data)
                
            else:
                self.right.insert(data)
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()

if __name__ == "__main__":
    tree = TreeNode(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(2)
    tree.insert(3)
    tree.inorder_traversal()
            