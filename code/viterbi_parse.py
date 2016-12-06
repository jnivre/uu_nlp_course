>>> v = np.ViterbiParser(g)
>>> p = v.parse('The rates rise .'.split())
>>> print(p.__next__())    # prints best parse tree
