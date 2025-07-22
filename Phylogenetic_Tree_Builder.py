
from represent_trees import *

# Write the following functions:

# Problem 1. leafCount(Tree)
# returns the count of leafs in the tree


def leafCount(Tree):
    '''counts the number of leaf nodes in the tree.'''
    if not Tree:
        return 0
    if not Tree[1] and not Tree[2]:  # If both left and right subtrees are empty
        return 1
    return leafCount(Tree[1]) + leafCount(Tree[2])


# Problem 2. find(node, Tree)
# returns True if the given node is in the given Tree and returns
# False otherwise. 


def find(node, Tree):
    '''checks if a node is present in the tree'''
    if not Tree:
        return False
    if Tree[0] == node:
        return True
    return find(node, Tree[1]) or find(node, Tree[2])


# Problem 3. subtree(node, Tree)
# which returns the subtree of the given Tree rooted at the given node.
# Said another way, this function returns the tree beginning at node.


def subtree(node, Tree):
    '''returns the subtree rooted at the given node'''
    if not Tree:
        return None
    if Tree[0] == node:
        return Tree
    left_subtree = subtree(node, Tree[1])
    if left_subtree:
        return left_subtree
    return subtree(node, Tree[2])


# Problem 4. nodeList(Tree)
# takes a Tree as input and returns a list of all the nodes in that tree
# (including both leaves and ancestral nodes)


def nodeList(Tree):
    ''' returns a list of all nodes in the tree'''
    if not Tree:
        return []
    return [Tree[0]] + nodeList(Tree[1]) + nodeList(Tree[2])


# Problem 5. descendantNodes(node, Tree)
# returns the list of all descendant nodes of the given node in the Tree.
# This function will not be recursive itself, but it will call the
# nodeList and subtree functions for help. 


def descendantNodes(node, Tree):
    '''returns a list of all descendant nodes of the given node'''
    sub_tree = subtree(node, Tree)
    return nodeList(sub_tree)[1:]  # Exclude the node itself


# Problem 6. parent(node, Tree)
# returns the parent of the given node in the Tree. If the node has no parent
# in the tree, the function should return the special value None. 


def parent(node, Tree, parent_node=None):
    '''returns the parent of the given node in the tree'''
    if not Tree:
        return None
    if Tree[0] == node:
        return parent_node
    left_parent = parent(node, Tree[1], Tree[0])
    if left_parent is not None:
        return left_parent
    return parent(node, Tree[2], Tree[0])


# Problem 7. scale(Tree,scaleFactor)
# takes a Tree as input, multiplies the numbers at its internal nodes
# by scaleFactor, and returns a new tree with those values. 


def scale(Tree, scaleFactor):
    '''takes a Tree as input, and multiplies the numbers at its
internal nodes by scaleFactor and returns a new tree with those values'''
    if not Tree:
        return Tree
    value, left, right = Tree
    if isinstance(value, (int, float)): # Check if current node is internal node
        value *= scaleFactor
        
    # Recursively scale the left and right subtrees
    left_scaled = scale(left, scaleFactor)
    right_scaled = scale(right, scaleFactor)
    
    return (value, left_scaled, right_scaled)


