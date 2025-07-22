# Phylogenetic Tree Utilities

A collection of Python scripts for constructing, representing, drawing, and analyzing phylogenetic trees using recursive data structures and the `turtle` graphics library.

---

## Requirements

* **Python 3.x**
* Standard library modules:

  * `turtle`

## Installation

1. Clone or download the repository containing these scripts.
2. Ensure you have Python 3 installed and accessible via your command line.
3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   ```

---

## Scripts Overview

### 1. `draw_trees.py`

Provides basic drawing utilities for trees and shapes using the `turtle` module:

* `square(sideLength)`: Draws a square with the specified side length.
* `fractalTree(trunkLength)`: Recursively draws a fractal-style tree given an initial trunk length.
* Template and starter code for `drawPhyloTree(Tree)`, which accepts a tree represented as a tuple.

Usage example:

```python
import turtle
from draw_trees import square, fractalTree

turtle.left(90)
fractalTree(300)  # Draws a fractal tree with trunk length 300
```

### 2. `DrawTrees2.py`

An enhanced phylogenetic tree drawer with branch-length scaling and angle corrections:

* Defines constants `ANGLE` and `CORRECTION` for branch orientation.
* `drawPhyloTree2(Tree, scale)`: Draws a phylogenetic tree where internal node values represent heights; branch lengths are scaled accordingly.

Usage example:

```python
import turtle
from DrawTrees2 import drawPhyloTree2, myTree

# myTree is defined in the script, or supply your own\scale = 20
drawPhyloTree2(myTree, scale)
turtle.done()
```

### 3. `represent_trees.py`

Functions for analyzing and manipulating tree data structures represented as nested tuples:

* `leafCount(Tree)`: Returns the number of leaf nodes.
* `find(node, Tree)`: Checks whether a node name/value exists in the tree.
* `subtree(node, Tree)`: Returns the subtree rooted at the specified node.
* `nodeList(Tree)`: Flattens the tree into a list of all nodes (internal and leaves).
* `descendantNodes(node, Tree)`: Lists all descendant nodes of a given node.
* `parent(node, Tree)`: Finds the parent of a given node, or `None` if it is the root.
* `scale(Tree, scaleFactor)`: Multiplies internal node values by a scale factor, returning a new tree.

Usage example:

```python
from represent_trees import leafCount, find, subtree

my_tree = ('A', ('B', (), ()), ('C', (), ()))
print(leafCount(my_tree))  # Output: 2
```

### 4. `Phylogenetic_Tree_Builder.py`

Basic tree metrics for tuple-based phylogenetic trees:

* `nodeCount(Tree)`: Computes the total number of nodes.
* `height(Tree)`: Computes the height of the tree (longest path from root to leaf).
* `leafList(Tree)`: Returns a list of leaf node labels.

Usage example:

```python
from Phylogenetic_Tree_Builder import nodeCount, height

sample_tree = (
    'A',
    ('B', ('D', (), ()), ('E', (), ())),
    ('C', ('F', (), ()), ('G', (), ()))
)
print(nodeCount(sample_tree))  # Total nodes
print(height(sample_tree))     # Height of the tree
```

---

## Usage Tips

* **Interactive Mode**: Many of these scripts are designed to be used in the Python shell or a Jupyter notebook. Import the specific functions you need.
* **Turtle Graphics**: Ensure your environment supports a GUI display for `turtle`. On headless servers, use a local machine or configure a virtual display.
* **Tree Format**: Trees are represented as nested tuples of the form `(value, left_subtree, right_subtree)`, where leaf nodes have empty subtrees: e.g., `('Leaf', (), ())`.

---

## Contributing

Feel free to submit issues or pull requests to expand functionality, add unit tests, or improve performance.

---

## License

This project is released under the MIT License. Be sure to include a copy of the license if distributing.
