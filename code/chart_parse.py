>>> import treebank-grammar as tg
>>> g = tg.extract_simple_pcfg(1000)
>>> import nltk.parse as np
>>> c = np.ChartParser(g)
>>> p = c.parse('The rates rise .'.split())
>>> len(list(p))       # prints number of parses
