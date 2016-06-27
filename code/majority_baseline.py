>>> import wsd_code as wc
>>> import nltk
>>> hard_dist = nltk.FreqDist([i.senses[0] for i in wc.senseval.instances('hard.pos')])
>>> hard_dist
FreqDist({'HARD1': 3455, 'HARD2': 502, 'HARD3': 376})
>>> hard_baseline = hard_dist.freq('HARD1')
>>> hard_baseline
0.797369028386799
