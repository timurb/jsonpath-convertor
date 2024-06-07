def set_value(obj, key, value):
    """
    Set values for array indexes with no errors
    """

    if isinstance(obj, list):
        key = int(key)
        while len(obj) < key+1:
            obj.append(None)

    obj[key] = value


def has_tem(obj, key):
    """
    Check if obj has specified key -- both for lists and dicts
    """

    if isinstance(obj, dict):
        return key in obj
    elif isinstance(obj, list):
        return len(obj) > key
    else:
        # You should never hit this line
        raise TypeError("Only dicts and lists supported")


def normalize_key(key):
    """
    Convert stringified numbers to numbers
    """
    if key.isnumeric():
        return int(key)

    return key


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
    first_path = normalize_key(path[0])

    if len(path) == 1:  # We got to the end of the path, just set the value for the leaf of the tree
        set_value(tree, first_path, value)
        return

    # Now combination of (first_path + tail) hold the original sequence for the whole path
    tail = path[1:]

    # Grow a new branch if no branch present
    if not has_tem(tree, first_path):
        if tail[0].isnumeric():
            set_value(tree, first_path, [])
        else:
            set_value(tree, first_path, {})

    # Process that new branch in the same way as the current one
    build_tree(tree[first_path], tail, value)


def parse_jsonpath(strings):
    """
        Parses list of k/v into structured JSON
    """
    result = {}

    for key in strings:
        value = strings[key]
        build_tree(result, key.split("."), value)

    return result
