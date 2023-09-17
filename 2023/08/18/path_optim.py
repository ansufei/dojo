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


def simplify_directions(pair):
    if pair in ['NS','SN','WE','EW']:
        return ""
    else:
        return pair

def optimize_path(path):
    if len(path) <= 2:
        return simplify_directions(path)
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
