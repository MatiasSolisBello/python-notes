"""
Arbol binario
"""

# Representar los nodos
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    # Private functions
    def __init__(self, data):
        self.root = Node(data)

    def __recursive_add(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__recursive_add(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__recursive_add(node.right, data)

    def __recursive_inorder(self, node):
        if node is not None:
            self.__recursive_inorder(node.left)
            print(node.data, end=", ")
            self.__recursive_inorder(node.right)

    def __recursive_preorder(self, node):
        if node is not None:
            print(node.data, end=", ")
            self.__recursive_preorder(node.left)
            self.__recursive_preorder(node.right)

    def __recursive_postorder(self, node):
        if node is not None:
            self.__recursive_postorder(node.left)
            self.__recursive_postorder(node.right)
            print(node.data, end=", ")

    def __search(self, node, search):
        if node is None:
            return None
        if node.data == search:
            return node
        if search < node.data:
            return self.__search(node.left, search)
        else:
            return self.__search(node.right, search)

    # Funciones publicas
    def add(self, data):
        self.__recursive_add(self.root, data)

    def inorder(self):
        print("Printing in-order tree: ")
        self.__recursive_inorder(self.root)
        print("")

    def preorder(self):
        print("Printing pre-order tree: ")
        self.__recursive_preorder(self.root)
        print("")

    def postorder(self):
        print("Printing post-order tree: ")
        self.__recursive_postorder(self.root)
        print("")

    def search(self, search):
        return self.__search(self.root, search)


tree = BinaryTree(5)
tree.add(3)
tree.add(2)
tree.add(8)
tree.add(9)

tree.preorder()
tree.inorder()
tree.postorder()

search_value = int(input("Enter a number to search in the tree: "))
node_result = tree.search(search_value)
if node_result is None:
    print(f"{search_value} does not exist")
else:
    print(f"{search_value} does exist")
