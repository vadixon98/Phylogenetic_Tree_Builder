import turtle
from draw_trees import *

# Constants
ANGLE = 30
CORRECTION = 1.155

myTree = (5,
          (3,
           ("A", (), ()),
           ("B", (), ())
          ),
          ("C", (), ())
         )


def drawPhyloTree2(Tree, scale):
    '''Draws a phylogenetic tree using the turtle graphics module.'''
    if not Tree:
        return

    # Write the current root element
    turtle.write(str(Tree[0]), font=("Arial", 12, "normal"))

    if len(Tree) == 1:
        return  # Leaf node: nothing more to draw

    # Move to draw the left subtree
    if Tree[1]:
        left_height = Tree[1][0] if isinstance(Tree[1][0], int) else 0
        horizontal_distance = (Tree[0] - left_height) * scale
        distance_to_move = horizontal_distance * CORRECTION

        turtle.left(ANGLE)
        turtle.forward(distance_to_move)
        drawPhyloTree2(Tree[1], scale)
        turtle.backward(distance_to_move)
        turtle.right(ANGLE)

    # Move to draw the right subtree
    if Tree[2]:
        right_height = Tree[2][0] if isinstance(Tree[2][0], int) else 0
        horizontal_distance = (Tree[0] - right_height) * scale
        distance_to_move = horizontal_distance * CORRECTION

        turtle.right(ANGLE)
        turtle.forward(distance_to_move)
        drawPhyloTree2(Tree[2], scale)
        turtle.backward(distance_to_move)
        turtle.left(ANGLE)
