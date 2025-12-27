"""Tree validation utilities.

This module provides functions to validate tree structures and
provide helpful error messages when trees are invalid.

Functions:
    validate_tree: Validates tree structure and raises errors if invalid
    is_valid_tree: Returns boolean indicating if tree is valid
    get_tree_structure_info: Returns detailed information about tree structure
"""

from typing import Union, Tuple, Dict, Any, Optional

# Type alias for trees
Tree = Union[Tuple, None]


def validate_tree(tree: Tree, name: str = "Tree") -> bool:
    """Validates that a tree has the correct structure.
    
    This function checks:
    - Tree is a tuple (not None, not a list, etc.)
    - Tree is not empty
    - Tree has either 1 element (leaf) or 3 elements (internal node)
    - Subtrees are recursively valid
    
    Args:
        tree: Tree structure to validate
        name: Name for error messages (used recursively for nested errors)
        
    Returns:
        True if tree is valid
        
    Raises:
        ValueError: If tree structure is invalid
        TypeError: If tree is not a tuple
        
    Examples:
        >>> validate_tree(('A', (), ()))
        True
        >>> validate_tree(('A', ('B', (), ()), ('C', (), ())))
        True
        >>> validate_tree([])
        Traceback (most recent call last):
            ...
        TypeError: Tree must be a tuple, got list
        >>> validate_tree(('A', 'B', 'C', 'D'))
        Traceback (most recent call last):
            ...
        ValueError: Tree must have 1 (leaf) or 3 (internal) elements, got 4
    """
    # Check if tree is None or empty
    if tree is None:
        raise ValueError(f"{name} cannot be None")
    
    # Check if tree is a tuple
    if not isinstance(tree, tuple):
        raise TypeError(
            f"{name} must be a tuple, got {type(tree).__name__}"
        )
    
    # Check if tree is empty
    if len(tree) == 0:
        raise ValueError(f"{name} cannot be empty")
    
    # Leaf node: single element
    if len(tree) == 1:
        return True
    
    # Internal node: must have exactly 3 elements (value, left, right)
    if len(tree) != 3:
        raise ValueError(
            f"{name} must have 1 (leaf) or 3 (internal) elements, "
            f"got {len(tree)}. Tree structure: {tree}"
        )
    
    # Recursively validate left subtree
    if tree[1] is not None:
        validate_tree(tree[1], f"{name}.left")
    
    # Recursively validate right subtree
    if tree[2] is not None:
        validate_tree(tree[2], f"{name}.right")
    
    return True


def is_valid_tree(tree: Tree) -> bool:
    """Check if tree is valid without raising exceptions.
    
    This is a non-exception version of validate_tree() that simply
    returns True or False. Useful for conditional checks.
    
    Args:
        tree: Tree structure to check
        
    Returns:
        bool: True if tree is valid, False otherwise
        
    Examples:
        >>> is_valid_tree(('A', (), ()))
        True
        >>> is_valid_tree([])
        False
        >>> is_valid_tree(None)
        False
        >>> is_valid_tree(('A', 'B', 'C', 'D'))
        False
    """
    try:
        validate_tree(tree)
        return True
    except (ValueError, TypeError):
        return False


def get_tree_structure_info(tree: Tree) -> Dict[str, Any]:
    """Returns detailed information about tree structure.
    
    This function validates the tree and returns useful information
    about its structure, including metrics and validation status.
    
    Args:
        tree: Tree to analyze
        
    Returns:
        dict: Dictionary containing:
            - 'valid': bool indicating if tree is valid
            - 'error': str error message if invalid
            - 'nodes': int total number of nodes (if valid)
            - 'height': int tree height (if valid)
            - 'leaves': int number of leaf nodes (if valid)
            - 'leaf_names': list of leaf node names (if valid)
            
    Examples:
        >>> info = get_tree_structure_info(('A', ('B', (), ()), ('C', (), ())))
        >>> info['valid']
        True
        >>> info['nodes']
        3
        >>> info['height']
        1
        >>> info['leaves']
        2
    """
    # First check if tree is valid
    if not is_valid_tree(tree):
        try:
            validate_tree(tree)  # This will raise the actual error
        except (ValueError, TypeError) as e:
            return {
                "valid": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    # Import tree analysis functions
    try:
        from represent_trees import nodeCount, height, leafList
    except ImportError:
        return {
            "valid": True,
            "error": "Could not import analysis functions from represent_trees"
        }
    
    # Calculate tree metrics
    try:
        return {
            "valid": True,
            "nodes": nodeCount(tree),
            "height": height(tree),
            "leaves": len(leafList(tree)),
            "leaf_names": leafList(tree),
            "root": tree[0] if tree else None
        }
    except Exception as e:
        return {
            "valid": True,
            "error": f"Error calculating metrics: {str(e)}"
        }


def find_tree_issues(tree: Tree) -> list:
    """Find and return a list of all issues with the tree structure.
    
    This function performs a thorough check and returns a list of
    all problems found, rather than stopping at the first error.
    
    Args:
        tree: Tree to check
        
    Returns:
        list: List of error message strings (empty if tree is valid)
        
    Examples:
        >>> issues = find_tree_issues(('A', 'B', 'C', 'D'))
        >>> len(issues) > 0
        True
    """
    issues = []
    
    if tree is None:
        issues.append("Tree is None")
        return issues
    
    if not isinstance(tree, tuple):
        issues.append(f"Tree must be a tuple, got {type(tree).__name__}")
        return issues
    
    if len(tree) == 0:
        issues.append("Tree is empty")
        return issues
    
    if len(tree) not in (1, 3):
        issues.append(
            f"Tree must have 1 (leaf) or 3 (internal) elements, got {len(tree)}"
        )
        return issues
    
    # Recursively check subtrees
    if len(tree) == 3:
        if tree[1] is not None:
            left_issues = find_tree_issues(tree[1])
            issues.extend([f"left subtree: {issue}" for issue in left_issues])
        
        if tree[2] is not None:
            right_issues = find_tree_issues(tree[2])
            issues.extend([f"right subtree: {issue}" for issue in right_issues])
    
    return issues


def validate_tree_with_suggestions(tree: Tree) -> Dict[str, Any]:
    """Validates tree and provides suggestions for fixing issues.
    
    This function not only validates but also provides helpful
    suggestions on how to fix common problems.
    
    Args:
        tree: Tree to validate
        
    Returns:
        dict: Dictionary with validation results and suggestions
    """
    result = {
        "valid": False,
        "issues": [],
        "suggestions": []
    }
    
    issues = find_tree_issues(tree)
    
    if not issues:
        result["valid"] = True
        return result
    
    result["issues"] = issues
    
    # Provide suggestions based on issues found
    for issue in issues:
        suggestion = None
        
        if "must be a tuple" in issue:
            suggestion = f"Convert to tuple: tuple({tree})"
        elif "cannot be empty" in issue:
            suggestion = "Add at least one element to the tuple"
        elif "must have 1 (leaf) or 3 (internal) elements" in issue:
            suggestion = (
                "For a leaf node, use: (node_name,)\n"
                "For an internal node, use: (node_name, left_subtree, right_subtree)"
            )
        
        if suggestion:
            result["suggestions"].append({
                "issue": issue,
                "suggestion": suggestion
            })
    
    return result


# Example usage and test function
if __name__ == "__main__":
    print("=" * 60)
    print("Tree Validator - Example Usage")
    print("=" * 60)
    
    # Test valid trees
    print("\n1. Testing valid trees:")
    print("-" * 60)
    
    valid_trees = [
        ('A', (), ()),  # Leaf
        ('A', ('B', (), ()), ('C', (), ())),  # Simple tree
    ]
    
    for tree in valid_trees:
        is_valid = is_valid_tree(tree)
        print(f"Tree: {tree}")
        print(f"  Valid: {is_valid}")
        if is_valid:
            info = get_tree_structure_info(tree)
            print(f"  Nodes: {info.get('nodes', 'N/A')}")
            print(f"  Height: {info.get('height', 'N/A')}")
            print(f"  Leaves: {info.get('leaves', 'N/A')}")
        print()
    
    # Test invalid trees
    print("\n2. Testing invalid trees:")
    print("-" * 60)
    
    invalid_trees = [
        None,
        [],
        (),
        ('A', 'B', 'C', 'D'),
        ('A', ('B',), ('C',)),  # Left subtree has wrong structure
    ]
    
    for tree in invalid_trees:
        is_valid = is_valid_tree(tree)
        print(f"Tree: {tree}")
        print(f"  Valid: {is_valid}")
        if not is_valid:
            issues = find_tree_issues(tree)
            print(f"  Issues: {issues}")
            suggestions = validate_tree_with_suggestions(tree)
            if suggestions["suggestions"]:
                print("  Suggestions:")
                for sug in suggestions["suggestions"]:
                    print(f"    - {sug['suggestion']}")
        print()
    
    # Test with real tree from represent_trees
    print("\n3. Testing with example tree from represent_trees:")
    print("-" * 60)
    try:
        from represent_trees import smallTree
        
        info = get_tree_structure_info(smallTree)
        print(f"Tree: smallTree")
        print(f"  Valid: {info['valid']}")
        if info['valid']:
            print(f"  Nodes: {info['nodes']}")
            print(f"  Height: {info['height']}")
            print(f"  Leaves: {info['leaves']}")
            print(f"  Leaf names: {info['leaf_names']}")
    except ImportError:
        print("Could not import smallTree from represent_trees")
    
    print("\n" + "=" * 60)

