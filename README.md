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

Thank you for your interest in improving **Phylogenetic Tree Utilities**! There are many ways to help:

- 🐛 **Report bugs**: Include your OS, Python version, steps to reproduce, and a minimal snippet/tree that triggers the issue.
- 💡 **Request features**: Describe the use‑case and, if possible, a small example tree or expected drawing.
- 🧪 **Add tests**: Increase coverage of tree utilities and drawing logic.
- 📝 **Improve docs**: Clarify function behavior, add examples, or fix typos.
- 🧩 **Contribute code**: Small, focused PRs are easiest to review.

### Development setup

1) Ensure **Python 3.10+** is available.
2) (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   python -m pip install --upgrade pip
   ```
3) *(Optional but encouraged)* Install developer tools:
   ```bash
   python -m pip install pytest black ruff mypy pre-commit
   pre-commit install  # enables auto-format/lint on commit, if you add a .pre-commit-config.yaml
   ```

### Running tests

We use **pytest**:
```bash
pytest -q
```

If you’re adding a new function (e.g., a new tree analysis helper), please include unit tests under a `tests/` directory. Example test shape:
```python
# tests/test_represent_trees.py
from represent_trees import leafCount

def test_leaf_count_simple():
    t = ('A', ('B', (), ()), ('C', (), ()))
    assert leafCount(t) == 2
```

### Coding style & quality

- Follow **PEP 8** and include **type hints** where reasonable.
- Keep functions **pure** where possible (no I/O in analysis utilities).
- Prefer **docstrings** that explain arguments, return values, and edge cases.
- Format with **black**, lint with **ruff**:
  ```bash
  ruff check .
  black .
  ```
- If you modify public behavior, update examples in the README.

### Pull request guidelines

- Create a topic branch from `main` (e.g., `feature/scale-negative-heights` or `fix/parent-for-root`).
- One logical change per PR. Keep diffs small and focused.
- Ensure:
  - [ ] `pytest` passes
  - [ ] new/changed behavior is documented
  - [ ] drawing demos still run (for `turtle` examples use `turtle.done()` to prevent premature close)
- Link related issues and describe the approach and trade‑offs in the PR body.

### Issue templates (suggested)

When filing an issue, consider this structure:

**Bug report**
- Environment (OS, Python)
- Steps to reproduce (code/tree)
- Expected vs. actual behavior
- Screenshots (for drawing issues)

**Feature request**
- Problem statement / motivation
- Proposed API (function name, signature, brief behavior)
- Minimal example



## License

This project is released under the **MIT License**. See the `LICENSE` file in this repository for the full text.

**Summary (not a substitute for the license):**
- You may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software.
- You must include the original copyright notice and the license in any substantial portions of the software.
- The software is provided **“as is”**, without warranty of any kind. The authors are **not liable** for any claim, damages, or other liability arising from its use.

If you distribute binaries or derivative works, please ensure a copy of the MIT license accompanies them. If you embed these utilities in academic work, a citation or link back to the repository is appreciated.


