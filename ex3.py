def join(*lists, sep='-'):
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i != len(lists)-1:
            result.append(sep)
    return result if result else None
