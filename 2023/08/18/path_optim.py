from collections import Counter

# Goal: remove loops but do not take a path not taken as we cannot presume on the absence of obstacles

def simplify_directions(pair):
    if pair in ['NS','SN','WE','EW']:
        return ""
    else:
        return pair
    
def check_for_loops(memory, move):
        result = [memory[-1][i] + move[i] for i in range(2)]
        if result in memory:
            print(memory.index(result))
            memory = memory[:memory.index(result)]
        return memory
                 
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
    print('initial result', memory)
    for i, move in enumerate(translated_path):
        memory = check_for_loops(memory, move)
    print(memory)
    
    # remove side by side opposites
    split_path = [path[i] + path[i+1] for i in range(len(path) - 1)]
    simplify = []
    for i, pair in enumerate(split_path):
        cut_loops = simplify_directions(pair)
        if (cut_loops == pair):
            simplify.append(pair)
        else:
            if i == 0:
                simplify.append(pair)
            else:
                simplify[i-1] = simplify[i-1][0]
                simplify.append(cut_loops)
    return ''.join(simplify)
