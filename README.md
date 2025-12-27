<div align="center">

# 🌳 Phylogenetic Tree Utilities

**A powerful collection of Python scripts for constructing, representing, drawing, and analyzing phylogenetic trees**

*Recursive data structures meet turtle graphics* 🐢

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [📚 Scripts Overview](#-scripts-overview)
- [💡 Usage Tips](#-usage-tips)
- [🔮 Roadmap & Improvements](#-roadmap--improvements)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

- 🎨 **Visual Tree Drawing** - Draw phylogenetic trees with the `turtle` graphics library
- 🔄 **Recursive Structures** - Elegant tuple-based tree representations
- 📊 **Tree Analysis** - Comprehensive utilities for counting nodes, finding parents, and more
- 🌿 **Fractal Trees** - Create beautiful fractal-style tree visualizations
- ⚙️ **Scalable Drawing** - Support for scaled trees with configurable branch lengths
- 🧮 **Tree Metrics** - Calculate height, count leaves, and traverse trees recursively

---

## 🚀 Quick Start

```python
# Draw a beautiful fractal tree
import turtle
from draw_trees import fractalTree

turtle.left(90)
fractalTree(300)
turtle.done()
```

```python
# Analyze a phylogenetic tree
from represent_trees import nodeCount, height, leafList
from Phylogenetic_Tree_Builder import leafCount

tree = ('A', ('B', (), ()), ('C', (), ()))
print(f"Nodes: {nodeCount(tree)}")      # Output: 3
print(f"Leaves: {leafCount(tree)}")     # Output: 2
print(f"Height: {height(tree)}")        # Output: 1
print(f"Leaf names: {leafList(tree)}")  # Output: ['B', 'C']
```

---

## 📦 Installation

### Requirements

- **Python 3.7+** 🐍
- Standard library modules:
  - `turtle` 🐢

### Setup Steps

1. **Clone or download** this repository
   ```bash
   git clone <repository-url>
   cd Phylogenetic_Tree_Builder
   ```

2. **Verify Python installation**
   ```bash
   python --version  # Should be 3.7 or higher
   ```

3. **Create a virtual environment** (Recommended)
   ```bash
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

That's it! No external dependencies required. 🎉

---

## 📚 Scripts Overview

### 🎨 1. `draw_trees.py`
*Basic drawing utilities for trees and shapes*

Provides foundational drawing functions using the `turtle` module:

| Function | Description |
|----------|-------------|
| `square(sideLength)` | Draws a square with specified side length |
| `fractalTree(trunkLength)` | Recursively draws a fractal-style tree |

**Example:**
```python
import turtle
from draw_trees import square, fractalTree

# Draw a square
square(250)

# Draw an upright fractal tree
turtle.left(90)
fractalTree(300)
turtle.done()
```

**💡 Tip:** Restart your Python shell (`Ctrl+F6` in many IDEs) after each turtle drawing session.

---

### 🌿 2. `DrawTrees2.py`
*Enhanced phylogenetic tree drawer with scaling*

An advanced tree drawer that uses internal node values to determine branch lengths:

| Feature | Description |
|---------|-------------|
| `ANGLE` | Branch angle constant (default: 30°) |
| `CORRECTION` | Distance correction factor (default: 1.155) |
| `drawPhyloTree2(Tree, scale)` | Draws trees with scaled branch lengths |

**Example:**
```python
import turtle
from DrawTrees2 import drawPhyloTree2, myTree

scale = 20
drawPhyloTree2(myTree, scale)
turtle.done()
```

**Tree Format:**
```python
# Numeric values represent heights/distances
# Internal nodes have numeric values, leaves have string names
myTree = (5,                          # Root node with value 5
          (3,                         # Left child with value 3
           ("A", (), ()),             # Left leaf 'A'
           ("B", (), ())              # Right leaf 'B'
          ),
          ("C", (), ())               # Right child (leaf) 'C'
         )
```

**Note:** The `myTree` example is already defined in `DrawTrees2.py`, so you can import and use it directly!

---

### 🔍 3. `represent_trees.py`
*Tree analysis and manipulation functions*

Comprehensive utilities for working with tuple-based tree structures:

| Function | Returns | Description |
|----------|---------|-------------|
| `nodeCount(Tree)` | `int` | Total number of nodes in the tree |
| `height(Tree)` | `int` | Tree height (longest path from root to leaf) |
| `leafList(Tree)` | `list` | List of all leaf node labels |

**Example:**
```python
from represent_trees import nodeCount, height, leafList

tree = ('A',
        ('B', ('D', (), ()), ('E', (), ())),
        ('C', ('F', (), ()), ('G', (), ()))
       )

print(f"Nodes: {nodeCount(tree)}")      # Output: 7
print(f"Height: {height(tree)}")        # Output: 2
print(f"Leaves: {leafList(tree)}")      # Output: ['D', 'E', 'F', 'G']
```

---

### 🧮 4. `Phylogenetic_Tree_Builder.py`
*Advanced tree operations and utilities*

Extended functionality for tree manipulation and analysis:

| Function | Returns | Description |
|----------|---------|-------------|
| `leafCount(Tree)` | `int` | Count of leaf nodes |
| `find(node, Tree)` | `bool` | Checks if node exists in tree |
| `subtree(node, Tree)` | `tuple` | Subtree rooted at specified node |
| `nodeList(Tree)` | `list` | All nodes (internal + leaves) |
| `descendantNodes(node, Tree)` | `list` | All descendants of a node |
| `parent(node, Tree)` | `str` or `None` | Parent of a node |
| `scale(Tree, scaleFactor)` | `tuple` | New tree with scaled internal node values |

**Example:**
```python
from Phylogenetic_Tree_Builder import leafCount, find, subtree, parent, scale

tree = ('A',
        ('B', ('D', (), ()), ('E', (), ())),
        ('C', (), ())
       )

print(leafCount(tree))              # Output: 3
print(find('D', tree))              # Output: True
print(parent('D', tree))            # Output: 'B'
print(descendantNodes('B', tree))   # Output: ['D', 'E']

# Scale numeric tree values
numeric_tree = (10, (5, (), ()), (3, (), ()))
scaled = scale(numeric_tree, 2.0)   # Doubles internal node values
```

---

## 🔮 Roadmap & Improvements

We're continuously working to improve this project! Check out our [**SUGGESTIONS.md**](SUGGESTIONS.md) document for:

- 📋 **Comprehensive improvement suggestions** - 20+ detailed recommendations
- 🎯 **Priority-based roadmap** - What to tackle first
- 💡 **Implementation examples** - Code snippets for improvements
- 🚀 **Quick wins** - Things you can do today

### Current Focus Areas

- ⚡ **Type hints** - Adding type annotations for better IDE support
- 🛡️ **Error handling** - Robust input validation and clear error messages
- 🧪 **Testing** - Building a comprehensive test suite
- 📚 **Documentation** - Enhanced examples and API docs
- 🔧 **Code organization** - Better module structure

Have ideas? Feel free to [open an issue](https://github.com/yourusername/Phylogenetic_Tree_Builder/issues) or contribute!

---

## 💡 Usage Tips

### 🌐 Interactive Mode
These scripts work great in:
- Python shell / REPL
- Jupyter notebooks
- IPython interactive sessions

Just import the functions you need:
```python
from draw_trees import fractalTree
from represent_trees import leafCount, height
```

### 🖥️ Turtle Graphics Requirements
- Requires a **GUI display** for drawing
- On headless servers: use a local machine or configure a virtual display (Xvfb)
- Window stays open until you call `turtle.done()` or close it manually
- **Important:** Restart your Python shell after each turtle drawing session for best results

### 🔄 Function Naming Note
Note that `leafCount` is available in `Phylogenetic_Tree_Builder.py` (with additional tree operations), while `nodeCount` and `height` are in `represent_trees.py`. Both modules complement each other!

### 🌳 Tree Format Specification
Trees are represented as nested tuples:
```
Tree = (value, left_subtree, right_subtree)
```

**Leaf node:** `('LeafName', (), ())`  
**Internal node:** `('NodeName', left_tree, right_tree)`

**Example:**
```python
# A simple binary tree
simple_tree = ('Root',
               ('Left', (), ()),
               ('Right', (), ())
              )
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

> 💡 **New to contributing?** Check out our [SUGGESTIONS.md](SUGGESTIONS.md) for ideas on what to work on, including quick wins that can be done in just a few hours!

### 🐛 Report Bugs
Found an issue? Open a bug report with:
- 🖥️ **Environment** (OS, Python version)
- 📝 **Steps to reproduce** (code/tree examples)
- ✅ **Expected vs. actual behavior**
- 🖼️ **Screenshots** (for drawing issues)

### 💡 Request Features
Have an idea? Describe:
- 🎯 **Problem statement** / motivation
- 🔧 **Proposed API** (function signature, behavior)
- 📖 **Minimal example**

### 🧪 Add Tests
Help us improve test coverage:
```bash
# Install test dependencies
pip install pytest

# Run tests
pytest -q
```

### 📝 Improve Documentation
- Clarify function behavior
- Add usage examples
- Fix typos or improve explanations

### 🧩 Contribute Code
- Keep PRs **small and focused**
- Follow **PEP 8** style guide
- Include **docstrings** and **type hints** (see [SUGGESTIONS.md](SUGGESTIONS.md) for examples)
- Add **tests** for new functionality
- Check our [roadmap](#-roadmap--improvements) for high-priority items

### 🔧 Development Setup

```bash
# 1. Clone repository
git clone <repository-url>
cd Phylogenetic_Tree_Builder

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dev tools (optional)
pip install pytest black ruff mypy pre-commit
pre-commit install
```

### ✅ Pull Request Checklist

- [ ] Tests pass (`pytest -q`) - Add tests for new features!
- [ ] Code follows PEP 8 style guide
- [ ] Docstrings added/updated with clear descriptions
- [ ] Type hints added (if applicable)
- [ ] Examples work correctly
- [ ] Drawing demos run (`turtle.done()` included)
- [ ] README updated if needed
- [ ] No linter errors (run `ruff check .` if available)

---

## 📄 License

This project is licensed under the **MIT License**.

> ⚠️ **Note:** If a LICENSE file is not present in the repository, please create one with the MIT License text. See [SUGGESTIONS.md](SUGGESTIONS.md) for details.

### Summary
- ✅ Free to use, modify, and distribute
- ✅ Include original copyright notice
- ⚠️ Provided "as is" without warranty

**Academic Use:** If you use this in research or academic work, a citation or link back to the repository is appreciated! 📚

---

## 📚 Additional Resources

- 📖 **[SUGGESTIONS.md](SUGGESTIONS.md)** - Detailed improvement suggestions and roadmap
- 🐛 **[Report Issues](https://github.com/yourusername/Phylogenetic_Tree_Builder/issues)** - Found a bug? Let us know!
- 💬 **[Discussions](https://github.com/yourusername/Phylogenetic_Tree_Builder/discussions)** - Questions or ideas? Start a discussion!

---

<div align="center">

**Built with ❤️ for the computational biology community**

*Happy tree building! 🌳✨*

[⬆ Back to Top](#-phylogenetic-tree-utilities)

</div>
