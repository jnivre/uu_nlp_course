>>> v = np.ViterbiParser(g)
>>> p = v.parse('The rates rise .'.split())
>>> print(p.next())    # prints best parse tree
