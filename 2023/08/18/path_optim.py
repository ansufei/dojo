from collections import Counter

# Goal: remove loops but do not take a path not taken as we cannot presume on the absence of obstacles


# def optimize_path(path):
#     trajectory = [(0, 0)]
#     for step in path:
#         if step == "N":
#             trajectory.append((trajectory[-1][0] + 1, trajectory[-1][1]))
#     counter = Counter([x for x in path])
#     netNS = counter["N"] - counter["S"]
#     netWE = counter["W"] - counter["E"]
#     final_path = ""
#     if netWE < 0:
#         final_path += abs(netWE) * "E"
#     else:
#         final_path += netWE * "W"

#     if netNS < 0:
#         final_path += abs(netNS) * "S"
#     else:
#         final_path += netNS * "N"

#     return final_path
map_directions = {'N':[-1,0],
                    'S':[1,0],
                    'E':[0,1],
                    'W':[0,-1]}

def simplify_directions(pair):
    if pair in ['NS','SN','WE','EW']:
        return ""
    else:
        return pair
    
def check_for_loops(result, move):
        flag_erase_loop = False
        result[1] += move[1]
        result[0] += move[0]
        if result == [0,0]:
             flag_erase_loop =  True
        return flag_erase_loop, result
                 
def translate_from_path(path):
    return [map_directions[move] for move in path]

def optimize_path(path):
    # treat directly trivial cases
    if len(path) <= 2:
        return simplify_directions(path)
    
    # manage loops
    translated_path = translate_from_path(path)
    result = translated_path[0]
    for i, move in enumerate(translated_path[1:]):
        flag_erase_loop, result = check_for_loops(result, move)
        if flag_erase_loop == True:
            path = path[i+2:]
    
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
