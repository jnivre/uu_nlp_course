>>> nb_hard = wc.wsd_classifier(nltk.NaiveBayesClassifier.train, 'hard.pos', wc.wsd_word_features, distance=3, confusion_matrix=True, log=True)
Reading data...
 Senses: HARD1 HARD2 HARD3
Training classifier...
Testing classifier...
Accuracy: 0.8016
Writing errors to errors.txt
      |   H   H   H |
      |   A   A   A |
      |   R   R   R |
      |   D   D   D |
      |   1   2   3 |
------+-------------+
HARD1 |<692>  7   3 |
HARD2 |  84  <2>  2 |
HARD3 |  75   1  <1>|
------+-------------+
(row = reference; col = test)



