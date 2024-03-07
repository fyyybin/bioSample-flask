def search_cell(tree, position, data):
    for tree1 in tree:
        if tree1['label'] == position[0]:
            for tree2 in tree1['children']:
                if tree2['label'] == position[1]:
                    for tree3 in tree2['children']:
                        if tree3['label'] == position[2]:
                            for tree4 in tree3['children']:
                                if tree4['label'] == position[3]:
                                    for tree5 in tree4['children']:
                                        if tree5['label'] == position[4]:
                                            for tree6 in tree5['children']:
                                                if tree6['label'] == position[5]:
                                                    tree6['cells'].append(data)
                                                else:
                                                    break
                                        else:
                                            break
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
    return tree