# Examples for CFB Chap. 9 with Comments

# Unit III in CFB includes chapters 9 through 11.

# Chap. 9 introduced the notion that trees can be
#   represented as a recursive structure in the
#   form of a tuple.

# Chap. 10 builds on this notion and introduces
#   the turtle package, which will be used to
#   draw phylogenetic trees, recursively.








####################################################
# Chapter 10 introduces the turtle library and how
# to use it to make simple drawings.

# We will utilize this package to draw phylogenetic
# trees that are supplied in the form of tuples.

# Because turtle is a library that is distinct from
# base Python, it must be imported, as follows:

import turtle

# Now let's write a function that uses two functions
# in the turtle library to draw a square:

def square(sideLength):
    '''Draws a square with a user-given side length.'''
    # Loop 4 times to draw 4 sides of the square
    for num in range(4):
        # Move forward by the side length
        turtle.forward(sideLength)
        # Turn right 90 degrees to form a right angle corner
        turtle.right(90)

# Note the use of dot notation, here taking the form:
#   library_name.function_of_interest(argument)

# The above function works best if the shell is
# restarted (restart the shell with ctrl + F6)

# Recommended sideLength = 250

# Restart shell after each use of turtle.




####################################################
# The turtle package can also be used to draw
# phylogenetic trees that are supplied in the
# form of tuples.

# However, as an intermediate step, let's write a
# function that can draw a fractal tree, as shown
# on the bottom of p. 158, in Fig. 10.4.

def fractalTree(trunkLength):
    '''Draws a tree, recursively, given a trunk length.'''
    # Base case: stop recursion if trunk is too short
    if trunkLength < 10:
        return
    else:
        # Draw the current trunk forward
        turtle.forward(trunkLength)
        # Turn left 45 degrees to draw left branch
        turtle.left(45)
        # Recursively draw left subtree with half the trunk length
        fractalTree(trunkLength/2.0)
        # Turn right 90 degrees (45 + 45) to draw right branch
        turtle.right(90)
        # Recursively draw right subtree with half the trunk length
        fractalTree(trunkLength/2.0)
        # Turn back left 45 degrees to return to original orientation
        turtle.left(45)
        # Move backward to return to starting position
        turtle.backward(trunkLength)


# If you don't like viewing trees on their sides,
# you can enter the command 'turtle.left(90)'
# before calling fractalTree().

# Recommended trunkLength = 300

# Restart shell after each use of turtle.




####################################################

# Section 10.2 (pp. 159 - 161) provides clues for
# you to use to compose a function called
# drawPhyloTree(Tree), which will take a tree in
# the form of a tuple as input.
#
# NOTE: This function has been implemented in draw_phylo_tree.py!
# Import it with: from draw_phylo_tree import drawPhyloTree

# Recall smallTree from Chap. 9 --
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

# drawPhyloTree(tree) should write out the names
# of leaf nodes, but should not write out the
# root or internal nodes. 

# Your program should recognize the base case of
# when the tree inhand is actually a leaf node.
# If so, it should write the node's name using
# turtle.write(x), where x is a string.

# In the recursive case drawPhyloTree(tree)
# should draw branches.
#
# IMPLEMENTATION NOTE:
# The complete implementation is available in draw_phylo_tree.py
# Example usage:
#   import turtle
#   from draw_phylo_tree import drawPhyloTree
#   from draw_trees import smallTree
#   drawPhyloTree(smallTree, branch_length=80, angle=45)
#   turtle.done()


