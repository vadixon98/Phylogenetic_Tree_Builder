# Examples for CFB Chap. 9 with Comments

# Unit III in CFB includes chapters 9 through 11.

# Chap. 9 introduces the notion that trees can be
#   represented as a recursive structure in the
#   form of a tuple.

# Chap. 10 introduces the turtle package, which
#   will be used to draw a tree, recursively.

# Chap. 11 introduces the UPGMA algorithm for
#   inferring a phylogenetic tree from biological
#   data and the end-of-unit programming problem,
#   which explores the evolutionary origins of
#   Neanderthals and modern humans.

# In addition to the above 3 chapters in CFB, I
# have provided 3 additional resources to help
# understand the contents of unit III:
#   (1) A video - "What is a phylogeny?"
#   (2) A video - "How do you build a phylogeny?"
#   (3) A review article - Baldauf (2003),
#           "Phylogeny for the faint of heart"


####################################################
# Chapter 9 introduces the notion of representing
# phylogenetic trees using tuples that have a
# recursive structure.

# The parts of a phylogenetic tree are reviewed in
# the first video, listed above, and in pp. 145-148.

# An example tree is presented in figure 9.3 (p. 147)
# and is represented by a tuple, as follows and on
# p. 148. --
# Tree structure: (node_name, left_subtree, right_subtree)
# Empty subtrees are represented as ()

smallTree = ('A',                              # Root node 'A'
                 ('B',                         # Left child 'B'
                      ('D', (), ()),          # Left leaf 'D'
                      ('E', (), ())           # Right leaf 'E'
                  ),
                 ('C',                         # Right child 'C'
                      ('F', (), ()),          # Left leaf 'F'
                      ('G', (), ())           # Right leaf 'G'
                  )
             )

# This illustrates the idea that any phylogenetic
# tree comprises:
#   (1) a root, and
#   (2, 3) two subtrees.

# Hence, passing any tree to the len() function
# yields a result of 3.


####################################################
# We can perform tasks on a phylogenetic tree
# recursively. For example, we can:
#   (1) Count the number of nodes in a tree,
#   (2) Measure the height of a tree, and
#   (3) Create a list of leaves in a tree.


####################################################
# Counting the nodes in a tree, recursively.

def nodeCount(Tree):
    '''Computes the number of nodes in a tree
    
    Args:
        Tree: A tuple representing a tree (node_name, left_subtree, right_subtree)
    
    Returns:
        int: The total number of nodes in the tree
    '''
    # Extract left and right subtrees
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]
    
    # Base case: leaf node (both subtrees are empty tuples)
    if Subtree1 == ():      # base case, subtrees
        return 1            # of a leaf are empty
    else:
        # Recursive case: count current node (1) plus nodes in left and right subtrees
        return 1 + nodeCount(Subtree1) + nodeCount(Subtree2)


####################################################
# Measuring the height of a tree, recursively.
# Height is defined as the number of edges from root to deepest leaf.
# A tree with only a root has height 0.

def height(Tree):
    '''Computes height of a tree
    
    Args:
        Tree: A tuple representing a tree (node_name, left_subtree, right_subtree)
    
    Returns:
        int: The height of the tree (0 for a leaf, increases by 1 for each level)
    '''
    # Extract left and right subtrees
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]
    
    # Base case: leaf node (subtrees are empty), height is 0
    if Subtree1 == ():      # base case, 1st subtree
        return 0            # is an empty tuple.
    else:
        # Recursive case: height is 1 (for current level) plus maximum height of subtrees
        return 1 + max(height(Subtree1), height(Subtree2))


####################################################
# Listing the leaves in a tree, recursively.

def leafList(Tree):
    '''Returns the list of leaves in a tree
    
    Args:
        Tree: A tuple representing a tree (node_name, left_subtree, right_subtree)
    
    Returns:
        list: A list containing the names of all leaf nodes in the tree
    '''
    # Extract root node and left/right subtrees
    Root = Tree[0]
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]
    
    # Base case: leaf node (subtrees are empty), return root as a list
    if Subtree1 == ():      # base case, 1st subtree
        return [Root]       # is an empty tuple.
    else:
        # Recursive case: combine leaves from left and right subtrees
        return leafList(Subtree1) + leafList(Subtree2)

