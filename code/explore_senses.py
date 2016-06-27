>>> import wsd_code as wc
>>> wc.senses('hard.pos')
['HARD3', 'HARD2', 'HARD1']
>>> hard = wc.senseval.instances('hard.pos')
>>> hard[0]
SensevalInstance(word='hard-a', position=20, context=[('``', '``'), ('he', 'PRP'),
('may', 'MD'), ('lose', 'VB'), ('all', 'DT'), ('popular', 'JJ'), ('support', 'NN'),
(',', ','), ('but', 'CC'), ('someone', 'NN'), ('has', 'VBZ'), ('to', 'TO'), 
('kill', 'VB'), ('him', 'PRP'), ('to', 'TO'), ('defeat', 'VB'), ('him', 'PRP'), 
('and', 'CC'), ('that', 'DT'), ("'s", 'VBZ'), ('hard', 'JJ'), ('to', 'TO'), 
('do', 'VB'), ('.', '.'), ("''", "''")], senses=('HARD1',))

