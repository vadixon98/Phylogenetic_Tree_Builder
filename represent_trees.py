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

# The parts of a phylpogenetic tree are reviewed in
# the first video, listed above, and in pp. 145-148.

# An example tree is presented in figure 9.3 (p. 147)
# and is represented by a tuple, as follows and on
# p. 148. --

smallTree = ('A',
                 ('B',
                      ('D', (), ()),
                      ('E', (), ())
                  ),
                 ('C',
                      ('F', (), ()),
                      ('G', (), ())
                  )
             )

# This illustrates the idea that any phylogenetic
# tree comprises:
#   (1) a root, and
#   (2, 3) two subtrees.

# Hence, passing any tree to the len() function
# yields a result of 3.




####################################################
# We can perfrom tasks on a phylogenetic tree
# resursively. For example, we can:
#   (1) Count the number of nodes in a tree,
#   (2) Measure the height of a tree, and
#   (3) Create a list of leaves in a tree.





####################################################
# Counting the nodes in a tree, recursively.

def nodeCount(Tree):
    '''Computes the number of nodes in a tree'''
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]
    if Subtree1 == ():      # base case, subtrees
        return 1            # of a leaf are empty
    else:
        return 1 + nodeCount(Subtree1) + nodeCount(Subtree2)









####################################################         
# Measuring the height of a tree, recursively.

def height(Tree):
    '''Computes height of a tree'''
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]
    if Subtree1 == ():      # base case, 1st subtree
        return 0            # is an empty tuple.
    else:
        return 1 + max(height(Subtree1), height(Subtree2))



####################################################
# Listing the leaves in a tree, recursively.

def leafList(Tree):
    '''Returns the list of leaves in a tree'''
    Root = Tree[0]
    Subtree1 = Tree[1]
    Subtree2 = Tree[2]
    if Subtree1 == ():      # base case, 1st subtree
        return [Root]       # is an empty tuple.
    else:
        return leafList(Subtree1) + leafList(Subtree2)



