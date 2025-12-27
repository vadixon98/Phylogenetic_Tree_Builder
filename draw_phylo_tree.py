"""Complete implementation of drawPhyloTree function.

This module implements the drawPhyloTree() function that was mentioned
but not implemented in draw_trees.py. This function draws phylogenetic
trees using turtle graphics, writing only leaf node names.

Based on Section 10.2 (pp. 159 - 161) of CFB Chapter 10.
"""

import turtle


def drawPhyloTree(Tree, branch_length=50, angle=30):
    """Draws a phylogenetic tree, writing leaf node names only.
    
    This function draws a phylogenetic tree using turtle graphics.
    Unlike drawPhyloTree2, this function:
    - Writes only leaf node names (not internal nodes or root)
    - Uses fixed branch lengths (configurable)
    - Uses a simpler drawing algorithm
    
    Args:
        Tree: A tuple representing a tree structure (node_name, left_subtree, right_subtree)
              Empty subtrees are represented as ()
        branch_length: Length of branches to draw (default: 50)
        angle: Angle for branch turns in degrees (default: 30)
    
    Examples:
        >>> import turtle
        >>> from draw_phylo_tree import drawPhyloTree
        >>> from represent_trees import smallTree
        >>> 
        >>> turtle.speed(3)
        >>> drawPhyloTree(smallTree, branch_length=80, angle=45)
        >>> turtle.done()
    """
    # Base case: empty tree, nothing to draw
    if not Tree:
        return
    
    # Base case: leaf node (only has a value, no subtrees)
    # A leaf is either:
    # - A tuple with 1 element: (node_name,)
    # - A tuple with 3 elements where both subtrees are empty: (node_name, (), ())
    if len(Tree) == 1:
        # Write the leaf node name
        turtle.write(str(Tree[0]), font=("Arial", 12, "normal"))
        return
    
    # Check if this is a leaf node (both subtrees are empty)
    if not Tree[1] and not Tree[2]:
        # Write the leaf node name
        turtle.write(str(Tree[0]), font=("Arial", 12, "normal"))
        return
    
    # Recursive case: internal node - draw branches recursively
    # Note: We don't write the internal node name, only leaf names
    
    # Draw the left subtree
    if Tree[1]:
        # Turn left by the specified angle to draw left branch
        turtle.left(angle)
        # Move forward by the branch length
        turtle.forward(branch_length)
        # Recursively draw the left subtree with slightly shorter branches
        # This creates a natural tapering effect as we go deeper
        drawPhyloTree(Tree[1], branch_length * 0.8, angle)
        # Return to the previous position (backtrack)
        turtle.backward(branch_length)
        # Turn right to restore original orientation
        turtle.right(angle)
    
    # Draw the right subtree
    if Tree[2]:
        # Turn right by the specified angle to draw right branch
        turtle.right(angle)
        # Move forward by the branch length
        turtle.forward(branch_length)
        # Recursively draw the right subtree with slightly shorter branches
        drawPhyloTree(Tree[2], branch_length * 0.8, angle)
        # Return to the previous position (backtrack)
        turtle.backward(branch_length)
        # Turn left to restore original orientation
        turtle.left(angle)


def drawPhyloTree_with_labels(Tree, branch_length=50, angle=30, show_internal=True):
    """Draws a phylogenetic tree with optional internal node labels.
    
    Extended version that optionally shows internal node names as well.
    
    Args:
        Tree: A tuple representing a tree structure
        branch_length: Length of branches to draw (default: 50)
        angle: Angle for branch turns in degrees (default: 30)
        show_internal: If True, writes internal node names too (default: True)
    
    Examples:
        >>> import turtle
        >>> from draw_phylo_tree import drawPhyloTree_with_labels
        >>> from represent_trees import smallTree
        >>> 
        >>> turtle.speed(3)
        >>> drawPhyloTree_with_labels(smallTree, show_internal=True)
        >>> turtle.done()
    """
    if not Tree:
        return
    
    # Check if this is a leaf node
    is_leaf = len(Tree) == 1 or (not Tree[1] and not Tree[2])
    
    if is_leaf:
        # Write the leaf node name
        turtle.write(str(Tree[0]), font=("Arial", 12, "normal"))
        return
    
    # For internal nodes, optionally write the name
    if show_internal:
        turtle.write(str(Tree[0]), font=("Arial", 10, "italic"))
        # Move forward a bit after writing internal node name
        turtle.forward(10)
    
    # Draw the left subtree
    if Tree[1]:
        turtle.left(angle)
        turtle.forward(branch_length)
        drawPhyloTree_with_labels(Tree[1], branch_length * 0.8, angle, show_internal)
        turtle.backward(branch_length)
        turtle.right(angle)
    
    # Draw the right subtree
    if Tree[2]:
        turtle.right(angle)
        turtle.forward(branch_length)
        drawPhyloTree_with_labels(Tree[2], branch_length * 0.8, angle, show_internal)
        turtle.backward(branch_length)
        turtle.left(angle)
    
    # Move back after drawing internal node
    if show_internal:
        turtle.backward(10)


# Example usage and test function
if __name__ == "__main__":
    # Import example tree
    try:
        from represent_trees import smallTree
        
        print("Drawing phylogenetic tree (leaf nodes only)...")
        print("Close the turtle window when done viewing.")
        
        # Setup turtle
        turtle.speed(3)  # Moderate speed
        turtle.penup()
        turtle.goto(0, -200)  # Start near bottom of screen
        turtle.pendown()
        
        # Draw the tree
        drawPhyloTree(smallTree, branch_length=80, angle=45)
        
        # Keep window open
        turtle.done()
        
    except ImportError:
        print("Error: Could not import smallTree from represent_trees")
        print("Please ensure represent_trees.py is in the same directory")

