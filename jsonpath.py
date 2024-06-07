def build_tree(tree, path, value):
    """
        Modify the leaf in the tree under target path

        Implementation Logic:
            1. If path consists of only a single element -- just modify the branch for that key
            2. Otherwise grown the branch by that element and recursively call the function
               with child branch and the rest of elements

        Parameters:
            - tree: Branch to modify
            - path: JSONPath notation processed into array
            - value: value to assign
    """
    first_path = path[0]

    if len(path) == 1:  # We got to the end of the path, just set the value for the leaf of the tree
        tree[first_path] = value
        return

    # Now combination of (first_path + tail) hold the original sequence for the whole path
    tail = path[1:]

    # Grow a new branch if no branch present
    if not first_path in tree:
        tree[first_path] = {}

    # Process that new branch in the same way as the current one
    build_tree(tree[first_path], tail, value)


def parse_jsonpath(input):
    """
        Parses list of k/v into structured JSON
    """
    result = {}

    for key in input:
        value = input[key]
        build_tree(result, key.split("."), value)

    return result
