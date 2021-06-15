class Node:
	value = None
	right = None
	left = None

	def __init__(self, val):
		self.value = val

def add_node(node, val):
	if node.value < val:
		if node.right == None:
			node.right = Node(val)
		else:
			add_node(node.right, val)
	elif node.value > val:
		if node.left == None:
			node.left = Node(val)
		else:
			add_node(node.left, val)

def find_node(node, val):
	if node.value == val:
		return node
	if node.value < val:
		return find_node(node.right, val)
	else:
		return find_node(node.left, val)

def get_view_node(node, depth=0):
	if node.left != None:
		if node.right != None:
			return f'{node.value}\n{get_view_node(node.left, depth + 1)} {get_view_node(node.right, depth + 1)}'
		else:
			return f'{node.value}\n{get_view_node(node.left, depth + 1)}'
	elif node.right != None:
		return f'{node.value}\n{get_view_node(node.right, depth + 1)}'
	else:
		return node.value

root = Node(8)
add_node(root, 5)
add_node(root, 11)
add_node(root, 3)
add_node(root, 7)
add_node(root, 13)

print(get_view_node(root))
