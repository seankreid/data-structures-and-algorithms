#!/usr/bin/env python3

# Sean Reid


class ArrayBinaryTree(BinaryTree, DynamicArray):


	def __init__(self):
		self._root = 0

	def root(self, node):
		self._str[0] = i

	def left(self, node, root):
		i = (root * 2) + 1
		self._str[i] = node
		
	def right(self, node, root):
		i = (root * 2) + 2
		self._str[i] = node

	def inorder(self):
    if not self.is_empty():
      for i in self._subtree_inorder(self.root()):
        yield i

    def _subtree_inorder(self, i):
    if self.left(i) is not None:         
      for other in self._subtree_inorder(self.left(i)):
        yield other
    yield i                               
    if self.right(i) is not None:          
      for other in self._subtree_inorder(self.right(i)):
        yield other

	def printExpression(i):
		if self.left(i) is not None:
			print("(")
			inorder(left(i))
		print(i.element())
		if self.right(i) is None:
			inorder(right(i))
			print(")")


	def main():
		exp = ("-*+-2*5+7 10 4 2 3")
		printExpression(exp)

	if __name__ == '__main__':
		main()



