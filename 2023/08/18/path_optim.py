from collections import Counter

# Goal: remove loops but do not take a path not taken as we cannot presume on the absence of obstacles

def simplify_directions(pair):
    if pair in ['NS','SN','WE','EW']:
        return ""
    else:
        return pair
    
def check_for_loops(path_indices, memory, move):
    result = [memory[-1][i] + move[i] for i in range(2)]
    if result in memory:
        cursor = memory.index(result)
        memory = memory[ : cursor + 1] # back to the first occurence of this position in memory
        cursor_path_indices = cursor + path_indices.count(0)
        path_indices = [0 if i >= cursor_path_indices else path_indices[i] for i in range(len(path_indices)+1)]
        # if new cursor before previous cursor (i.e. new loop)
        if path_indices.index(0) > cursor:
            path_indices[cursor:path_indices.index(0)] = [0]
    else:
        memory.append(result)
        path_indices.append(1)
    return path_indices, memory
                 
def translate_from_path(path):
    map_directions = {  'N':[-1,0],
                        'S':[1,0],
                        'E':[0,1],
                        'W':[0,-1]
                    }
    return [map_directions[move] for move in path]

def optimize_path(path):
    # treat directly trivial cases
    if len(path) <= 2:
        return simplify_directions(path)
    
    # manage loops
    translated_path = translate_from_path(path)
    memory = [[0,0]]
    path_indices = []
    for i, move in enumerate(translated_path):
        path_indices, memory = check_for_loops(path_indices, memory, move)

    # translate back into letters
    path = ''.join([path[i] for i in range(len(path)) if path_indices[i]])
    return path

