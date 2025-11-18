import turtle
from draw_trees import *

# Constants
ANGLE = 30              # Angle in degrees for drawing branches (30 degrees left/right)
CORRECTION = 1.155      # Correction factor to adjust horizontal distance calculation

# Example phylogenetic tree with numeric node values representing heights/distances
# Structure: (node_value, left_subtree, right_subtree)
# Numeric values indicate the height/distance at which branches are drawn
myTree = (5,                              # Root node with value 5
          (3,                             # Left child with value 3
           ("A", (), ()),                 # Left leaf node 'A'
           ("B", (), ())                  # Right leaf node 'B'
          ),
          ("C", (), ())                   # Right child (leaf node) 'C'
         )


def drawPhyloTree2(Tree, scale):
    '''Draws a phylogenetic tree using the turtle graphics module.
    
    Args:
        Tree: A tuple representing a tree structure (node_value, left_subtree, right_subtree)
              where node_value is a number (height/distance) or a string (leaf name)
        scale: A scaling factor to adjust the distances between nodes
    '''
    # Base case: empty tree, nothing to draw
    if not Tree:
        return

    # Write the current node's value (number or name) at the current position
    turtle.write(str(Tree[0]), font=("Arial", 12, "normal"))

    # Base case: leaf node (only has a value, no subtrees)
    if len(Tree) == 1:
        return  # Leaf node: nothing more to draw

    # Draw the left subtree
    if Tree[1]:
        # Get the height value of the left child (if it's a number, otherwise use 0)
        left_height = Tree[1][0] if isinstance(Tree[1][0], int) else 0
        # Calculate horizontal distance based on difference between current node and child node
        horizontal_distance = (Tree[0] - left_height) * scale
        # Apply correction factor to adjust the distance (accounts for angle geometry)
        distance_to_move = horizontal_distance * CORRECTION

        # Turn left by the specified angle to draw left branch
        turtle.left(ANGLE)
        # Move forward by the calculated distance
        turtle.forward(distance_to_move)
        # Recursively draw the left subtree
        drawPhyloTree2(Tree[1], scale)
        # Return to the previous position (backtrack)
        turtle.backward(distance_to_move)
        # Turn right to restore original orientation
        turtle.right(ANGLE)

    # Draw the right subtree
    if Tree[2]:
        # Get the height value of the right child (if it's a number, otherwise use 0)
        right_height = Tree[2][0] if isinstance(Tree[2][0], int) else 0
        # Calculate horizontal distance based on difference between current node and child node
        horizontal_distance = (Tree[0] - right_height) * scale
        # Apply correction factor to adjust the distance (accounts for angle geometry)
        distance_to_move = horizontal_distance * CORRECTION

        # Turn right by the specified angle to draw right branch
        turtle.right(ANGLE)
        # Move forward by the calculated distance
        turtle.forward(distance_to_move)
        # Recursively draw the right subtree
        drawPhyloTree2(Tree[2], scale)
        # Return to the previous position (backtrack)
        turtle.backward(distance_to_move)
        # Turn left to restore original orientation
        turtle.left(ANGLE)
