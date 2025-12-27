# 📝 Additional Scripts Suggestions

This document outlines useful scripts that could be added to enhance the Phylogenetic Tree Builder project.

---

## 🎯 High Priority Scripts

### 1. **`draw_phylo_tree.py`** ⭐ *Complete Missing Function*
**Purpose:** Implement the `drawPhyloTree()` function mentioned in `draw_trees.py` comments.

**What it does:**
- Draws phylogenetic trees using turtle graphics
- Writes only leaf node names (not internal nodes)
- Draws branches between nodes

**Implementation:**
```python
"""Complete implementation of drawPhyloTree function."""

import turtle

def drawPhyloTree(Tree, branch_length=50, angle=30):
    """Draws a phylogenetic tree, writing leaf node names only.
    
    Args:
        Tree: A tuple representing a tree structure (node_name, left_subtree, right_subtree)
        branch_length: Length of branches to draw (default: 50)
        angle: Angle for branch turns in degrees (default: 30)
    """
    if not Tree:
        return
    
    # Base case: leaf node - write the name
    if len(Tree) == 1 or (not Tree[1] and not Tree[2]):
        turtle.write(str(Tree[0]), font=("Arial", 12, "normal"))
        return
    
    # Recursive case: internal node - draw branches
    # Draw left subtree
    if Tree[1]:
        turtle.left(angle)
        turtle.forward(branch_length)
        drawPhyloTree(Tree[1], branch_length * 0.8, angle)
        turtle.backward(branch_length)
        turtle.right(angle)
    
    # Draw right subtree
    if Tree[2]:
        turtle.right(angle)
        turtle.forward(branch_length)
        drawPhyloTree(Tree[2], branch_length * 0.8, angle)
        turtle.backward(branch_length)
        turtle.left(angle)
```

**Usage:**
```python
from draw_phylo_tree import drawPhyloTree
from represent_trees import smallTree
import turtle

turtle.speed(3)
drawPhyloTree(smallTree, branch_length=80, angle=45)
turtle.done()
```

---

### 2. **`tree_validator.py`** ✅ *Input Validation*
**Purpose:** Validate tree structures and provide helpful error messages.

**Functions:**
- `validate_tree(tree)` - Validates structure
- `is_valid_tree(tree)` - Boolean check
- `fix_tree_format(tree)` - Attempts to fix common issues

**Implementation:**
```python
"""Tree validation utilities."""

def validate_tree(tree, name="Tree"):
    """Validates that a tree has the correct structure.
    
    Args:
        tree: Tree structure to validate
        name: Name for error messages
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If tree structure is invalid
        TypeError: If tree is not a tuple
    """
    if not isinstance(tree, tuple):
        raise TypeError(f"{name} must be a tuple, got {type(tree).__name__}")
    
    if len(tree) == 0:
        raise ValueError(f"{name} cannot be empty")
    
    if len(tree) == 1:
        return True  # Leaf node is valid
    
    if len(tree) != 3:
        raise ValueError(
            f"{name} must have 1 (leaf) or 3 (internal) elements, "
            f"got {len(tree)}"
        )
    
    # Recursively validate subtrees
    validate_tree(tree[1], f"{name}.left")
    validate_tree(tree[2], f"{name}.right")
    
    return True


def is_valid_tree(tree):
    """Check if tree is valid without raising exceptions.
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        validate_tree(tree)
        return True
    except (ValueError, TypeError):
        return False


def get_tree_structure_info(tree):
    """Returns information about tree structure.
    
    Returns:
        dict: Information about the tree structure
    """
    from represent_trees import nodeCount, height, leafList
    
    if not is_valid_tree(tree):
        return {"valid": False, "error": "Invalid tree structure"}
    
    return {
        "valid": True,
        "nodes": nodeCount(tree),
        "height": height(tree),
        "leaves": len(leafList(tree)),
        "leaf_names": leafList(tree)
    }
```

---

### 3. **`tree_utils.py`** 🔧 *Extended Tree Operations*
**Purpose:** Additional useful tree operations not in current scripts.

**Functions:**
- Tree traversals (pre-order, in-order, post-order, level-order)
- Tree comparisons
- Tree copying
- Depth calculations
- Path finding

**Implementation:**
```python
"""Extended tree utility functions."""

from collections import deque


def pre_order(Tree):
    """Pre-order traversal: root, left, right.
    
    Returns:
        list: Nodes in pre-order
    """
    if not Tree:
        return []
    if len(Tree) == 1:
        return [Tree[0]]
    return [Tree[0]] + pre_order(Tree[1]) + pre_order(Tree[2])


def in_order(Tree):
    """In-order traversal: left, root, right.
    
    Returns:
        list: Nodes in in-order
    """
    if not Tree:
        return []
    if len(Tree) == 1:
        return [Tree[0]]
    return in_order(Tree[1]) + [Tree[0]] + in_order(Tree[2])


def post_order(Tree):
    """Post-order traversal: left, right, root.
    
    Returns:
        list: Nodes in post-order
    """
    if not Tree:
        return []
    if len(Tree) == 1:
        return [Tree[0]]
    return post_order(Tree[1]) + post_order(Tree[2]) + [Tree[0]]


def level_order(Tree):
    """Level-order (breadth-first) traversal.
    
    Returns:
        list: Nodes in level-order
    """
    if not Tree:
        return []
    
    result = []
    queue = deque([Tree])
    
    while queue:
        current = queue.popleft()
        if current:
            result.append(current[0])
            if len(current) == 3:
                queue.append(current[1])
                queue.append(current[2])
    
    return result


def depth(node, Tree, current_depth=0):
    """Calculate depth of a node in the tree.
    
    Args:
        node: Node to find depth of
        Tree: Tree to search in
        current_depth: Current depth (used in recursion)
        
    Returns:
        int: Depth of node, or -1 if not found
    """
    if not Tree:
        return -1
    
    if Tree[0] == node:
        return current_depth
    
    if len(Tree) == 3:
        left_depth = depth(node, Tree[1], current_depth + 1)
        if left_depth != -1:
            return left_depth
        return depth(node, Tree[2], current_depth + 1)
    
    return -1


def copy_tree(Tree):
    """Create a deep copy of the tree.
    
    Returns:
        tuple: Deep copy of the tree
    """
    if not Tree:
        return Tree
    if len(Tree) == 1:
        return (Tree[0],)
    return (Tree[0], copy_tree(Tree[1]), copy_tree(Tree[2]))


def trees_equal(tree1, tree2):
    """Check if two trees are structurally and semantically equal.
    
    Returns:
        bool: True if trees are equal
    """
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if len(tree1) != len(tree2):
        return False
    if tree1[0] != tree2[0]:
        return False
    if len(tree1) == 1:
        return True
    return trees_equal(tree1[1], tree2[1]) and trees_equal(tree1[2], tree2[2])


def path_to_root(node, Tree):
    """Get path from a node to the root.
    
    Returns:
        list: Path from node to root (including both)
    """
    from Phylogenetic_Tree_Builder import parent
    
    if not Tree:
        return []
    
    path = [node]
    current_parent = parent(node, Tree)
    
    while current_parent is not None:
        path.append(current_parent)
        current_parent = parent(current_parent, Tree)
    
    return path[::-1]  # Reverse to get root -> node path
```

---

### 4. **`tree_generator.py`** 🌳 *Generate Example Trees*
**Purpose:** Generate example trees for testing and demonstrations.

**Functions:**
- Generate random trees
- Generate balanced trees
- Generate trees from list of leaves
- Generate specific tree patterns

**Implementation:**
```python
"""Tree generation utilities for testing and examples."""

import random


def generate_balanced_tree(leaves, prefix="Node"):
    """Generate a balanced binary tree from a list of leaf names.
    
    Args:
        leaves: List of leaf node names
        prefix: Prefix for internal nodes
        
    Returns:
        tuple: Generated tree
    """
    if len(leaves) == 0:
        return None
    if len(leaves) == 1:
        return (leaves[0], (), ())
    
    mid = len(leaves) // 2
    left_leaves = leaves[:mid]
    right_leaves = leaves[mid:]
    
    internal_name = f"{prefix}_{len(leaves)}"
    return (
        internal_name,
        generate_balanced_tree(left_leaves, prefix),
        generate_balanced_tree(right_leaves, prefix)
    )


def generate_random_tree(leaf_count, leaf_prefix="Leaf", node_prefix="Node"):
    """Generate a random binary tree structure.
    
    Args:
        leaf_count: Number of leaves to generate
        leaf_prefix: Prefix for leaf names
        node_prefix: Prefix for internal nodes
        
    Returns:
        tuple: Randomly generated tree
    """
    if leaf_count <= 0:
        return None
    if leaf_count == 1:
        return (f"{leaf_prefix}_1", (), ())
    
    # Randomly split leaves between left and right
    left_count = random.randint(1, leaf_count - 1)
    right_count = leaf_count - left_count
    
    left_tree = generate_random_tree(left_count, leaf_prefix, node_prefix)
    right_tree = generate_random_tree(right_count, leaf_prefix, node_prefix)
    
    node_name = f"{node_prefix}_{leaf_count}"
    return (node_name, left_tree, right_tree)


def generate_star_tree(leaves, root_name="Root"):
    """Generate a star tree (all leaves connected directly to root).
    
    Args:
        leaves: List of leaf names
        root_name: Name of root node
        
    Returns:
        tuple: Star tree structure
    """
    if len(leaves) == 0:
        return (root_name, (), ())
    if len(leaves) == 1:
        return (root_name, (leaves[0], (), ()), ())
    if len(leaves) == 2:
        return (root_name, (leaves[0], (), ()), (leaves[1], (), ()))
    
    # For more than 2 leaves, create left and right subtrees
    mid = len(leaves) // 2
    left_tree = generate_star_tree(leaves[:mid], f"{root_name}_L")
    right_tree = generate_star_tree(leaves[mid:], f"{root_name}_R")
    
    return (root_name, left_tree, right_tree)
```

---

## 🎨 Medium Priority Scripts

### 5. **`tree_visualizer.py`** 📊 *ASCII Art Trees*
**Purpose:** Print trees as ASCII art in the terminal.

**Functions:**
- `print_tree_ascii(tree)` - Pretty-print tree
- `tree_to_string(tree)` - Convert to string
- `print_tree_horizontal(tree)` - Horizontal layout

**Implementation:**
```python
"""ASCII art tree visualization."""

def print_tree_ascii(tree, prefix="", is_last=True):
    """Print tree in ASCII art format.
    
    Args:
        tree: Tree to print
        prefix: Prefix for current line (used in recursion)
        is_last: Whether this is the last child (affects connector)
    """
    if not tree:
        return
    
    # Print current node
    connector = "└── " if is_last else "├── "
    print(prefix + connector + str(tree[0]))
    
    # Update prefix for children
    extension = "    " if is_last else "│   "
    new_prefix = prefix + extension
    
    # Print children
    if len(tree) == 3:
        left, right = tree[1], tree[2]
        if left:
            print_tree_ascii(left, new_prefix, right is None or not right)
        if right:
            print_tree_ascii(right, new_prefix, True)


def tree_to_string(tree, prefix="", is_last=True):
    """Convert tree to string representation.
    
    Returns:
        str: String representation of tree
    """
    if not tree:
        return ""
    
    lines = []
    connector = "└── " if is_last else "├── "
    lines.append(prefix + connector + str(tree[0]))
    
    extension = "    " if is_last else "│   "
    new_prefix = prefix + extension
    
    if len(tree) == 3:
        left, right = tree[1], tree[2]
        if left:
            lines.append(tree_to_string(left, new_prefix, right is None or not right))
        if right:
            lines.append(tree_to_string(right, new_prefix, True))
    
    return "\n".join(line for line in lines if line)
```

**Usage:**
```python
from tree_visualizer import print_tree_ascii
from represent_trees import smallTree

print_tree_ascii(smallTree)
# Output:
# └── A
#     ├── B
#     │   ├── D
#     │   └── E
#     └── C
#         ├── F
#         └── G
```

---

### 6. **`tree_io.py`** 💾 *File I/O Operations*
**Purpose:** Save and load trees to/from files.

**Functions:**
- `save_tree(tree, filename)` - Save tree to file
- `load_tree(filename)` - Load tree from file
- `tree_to_json(tree)` - Convert to JSON
- `tree_from_json(json_str)` - Parse from JSON

**Implementation:**
```python
"""Tree file I/O operations."""

import json
import ast


def save_tree(tree, filename, format='python'):
    """Save tree to a file.
    
    Args:
        tree: Tree to save
        filename: Output filename
        format: Format to use ('python' or 'json')
    """
    if format == 'python':
        with open(filename, 'w') as f:
            f.write(repr(tree))
    elif format == 'json':
        with open(filename, 'w') as f:
            json.dump(tree, f, indent=2)
    else:
        raise ValueError(f"Unknown format: {format}")


def load_tree(filename, format='auto'):
    """Load tree from a file.
    
    Args:
        filename: Input filename
        format: Format to use ('auto', 'python', or 'json')
        
    Returns:
        tuple: Loaded tree
    """
    with open(filename, 'r') as f:
        content = f.read()
    
    if format == 'auto':
        format = 'json' if filename.endswith('.json') else 'python'
    
    if format == 'python':
        return ast.literal_eval(content)
    elif format == 'json':
        return tuple(json.loads(content))
    else:
        raise ValueError(f"Unknown format: {format}")


def tree_to_json(tree):
    """Convert tree to JSON string.
    
    Returns:
        str: JSON representation of tree
    """
    def tree_to_list(t):
        if not t:
            return None
        if len(t) == 1:
            return [t[0]]
        return [t[0], tree_to_list(t[1]), tree_to_list(t[2])]
    
    return json.dumps(tree_to_list(tree), indent=2)


def tree_from_json(json_str):
    """Parse tree from JSON string.
    
    Args:
        json_str: JSON string representation
        
    Returns:
        tuple: Parsed tree
    """
    def list_to_tree(lst):
        if lst is None:
            return None
        if isinstance(lst, list) and len(lst) == 1:
            return (lst[0],)
        if isinstance(lst, list) and len(lst) == 3:
            return (lst[0], list_to_tree(lst[1]), list_to_tree(lst[2]))
        return lst
    
    data = json.loads(json_str)
    return list_to_tree(data)
```

---

### 7. **`demo.py`** 🎬 *Comprehensive Demo*
**Purpose:** Showcase all features with examples.

**Implementation:**
```python
"""Comprehensive demo script showcasing all features."""

def run_demo():
    """Run a comprehensive demo of all tree utilities."""
    
    print("=" * 60)
    print("Phylogenetic Tree Builder - Comprehensive Demo")
    print("=" * 60)
    
    # Import all modules
    from represent_trees import smallTree, nodeCount, height, leafList
    from Phylogenetic_Tree_Builder import (
        leafCount, find, subtree, parent, descendantNodes, scale
    )
    
    print("\n1. Basic Tree Structure")
    print("-" * 60)
    print(f"Example tree: {smallTree}")
    
    print("\n2. Tree Metrics")
    print("-" * 60)
    print(f"Total nodes: {nodeCount(smallTree)}")
    print(f"Leaf count: {leafCount(smallTree)}")
    print(f"Height: {height(smallTree)}")
    print(f"Leaf names: {leafList(smallTree)}")
    
    print("\n3. Tree Search Operations")
    print("-" * 60)
    print(f"Find 'D': {find('D', smallTree)}")
    print(f"Find 'X': {find('X', smallTree)}")
    print(f"Parent of 'D': {parent('D', smallTree)}")
    print(f"Parent of 'A' (root): {parent('A', smallTree)}")
    
    print("\n4. Subtree Operations")
    print("-" * 60)
    subtree_B = subtree('B', smallTree)
    print(f"Subtree rooted at 'B': {subtree_B}")
    print(f"Descendants of 'B': {descendantNodes('B', smallTree)}")
    
    print("\n5. Tree Modification")
    print("-" * 60)
    numeric_tree = (10, (5, (), ()), (3, (), ()))
    scaled = scale(numeric_tree, 2.0)
    print(f"Original: {numeric_tree}")
    print(f"Scaled x2: {scaled}")
    
    print("\n6. ASCII Visualization")
    print("-" * 60)
    try:
        from tree_visualizer import print_tree_ascii
        print_tree_ascii(smallTree)
    except ImportError:
        print("tree_visualizer module not available")
    
    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
```

---

## 🔧 Lower Priority Scripts

### 8. **`tree_comparator.py`** 🔍 *Tree Comparison*
Compare trees, find differences, calculate similarity.

### 9. **`tree_exporter.py`** 📤 *Export to Formats*
Export trees to Newick format, DOT format (Graphviz), etc.

### 10. **`tree_statistics.py`** 📈 *Statistical Analysis*
Calculate various statistics about trees (branching factor, balance, etc.).

---

## 📋 Implementation Priority

1. **High Priority (Do First):**
   - `draw_phylo_tree.py` - Complete missing function
   - `tree_validator.py` - Essential for robustness
   - `tree_utils.py` - Useful extended operations

2. **Medium Priority (Nice to Have):**
   - `tree_generator.py` - Useful for testing
   - `tree_visualizer.py` - Better UX
   - `tree_io.py` - Practical file operations
   - `demo.py` - Showcase features

3. **Low Priority (Future Enhancement):**
   - `tree_comparator.py`
   - `tree_exporter.py`
   - `tree_statistics.py`

---

## 💡 Quick Implementation Guide

For each script:
1. Create the `.py` file
2. Add proper docstrings
3. Include usage examples in docstrings
4. Add to README.md documentation
5. Write basic tests (when test suite is set up)

Would you like me to implement any of these scripts? 🚀

