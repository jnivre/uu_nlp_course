>>> import cfg_parser as cfg
>>> g = cfg.read_grammar('grammar.txt')
>>> cfg.parse_sentences(g)
Parse a sentence (Q to quit): He worked for the BBC for a decade.
(S
  (S
    (NP (Pronoun He))
    (VP
      (Verb worked)
      (PP (Prep for) (NP (Det the) (Noun BBC)))
      (PP (Prep for) (NP (Det a) (Noun decade)))))
  (Punct .))
Parse a sentence (Q to quit): Q
>>> 
