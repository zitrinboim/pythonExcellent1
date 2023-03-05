def interleave(*iterables):
    zipped = zip(*iterables)
    for tup in zipped:
        for item in tup:
            yield item
