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
    for num in range(4):
        turtle.forward(sideLength)
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
    if trunkLength < 10:
        return
    else:
        turtle.forward(trunkLength)
        turtle.left(45)
        fractalTree(trunkLength/2.0)
        turtle.right(90)
        fractalTree(trunkLength/2.0)
        turtle.left(45)
        turtle.backward(trunkLength)


# If you don't like viewing trees on their sides,
# you can enter the command 'turtle.left(90)'
# before calling fractalTree().

# Recommedned trunkLength = 300

# Restart shell after each use of turtle.




####################################################

# Section 10.2 (pp. 159 - 161) provides clues for
# you to use to compose a function called
# drawPhyloTree(Tree), which will take a tree in
# the form of a tuple as input.

# Recall smallTree from Chap. 9 --

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

# drawPhyloTree(tree) should write out the names
# of leaf nodes, but should not write out the
# root or internal nodes. 

# Your program should recognize the base case of
# when the tree inhand is actually a leaf node.
# If so, it should write the node's name using
# trutle.write(x), where x is a string.

# In the recursive case drawPhyloTree(tree)
# should draw branches.


