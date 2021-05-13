# Sort Binary Tree By Levels
# https://www.codewars.com/kata/52bef5e3588c56132c0003bc

def tree_by_levels(node):
    nodes = [node]
    vals = []
    if node != None:
        while len(nodes) > 0:
            if nodes[0] != None:
                vals.append(nodes[0].value)
                if nodes[0].left:
                    nodes.append(nodes[0].left)
                if nodes[0].right:
                    nodes.append(nodes[0].right)
                nodes = nodes[1:]
    return vals