#
#  Constructs branch of dict of target structure from inputs
#
#  Implementation Logic:
#  1. Split array of ["a","b","c"] into head ["a"] and tail ["b","c"]
#  2. If there is no tail just use head to construct dict
#     Example: ["c"] -> {"c": value}
#  3. Otherwise recursively call the function for tail only  
#
#  Parameters:
#   - keys: JSONPath notation processed into array
#   - value: value to assign
#   - result: dict to modify with processed value
#             On the first iteration this is result for target dict.
#             On recursive iteration that is result for the branch of the dict 
# 
def build_dict(keys, value, result):
    current_key = keys[0]

    if len(keys) == 1:
        result[current_key] = value
        return

    tail = keys[1:]

    if not current_key in result:       # don't overwrite the branch in dict if there is one already
        result[current_key] = {}

    build_dict(tail, value, result[current_key])


#
# Parses list of k/v into structured JSON
def parse_jsonpath(input):
    result = {}

    for key in input:
        value = input[key]
        build_dict(key.split("."), value, result)

    return result