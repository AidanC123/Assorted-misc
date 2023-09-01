Note; this file contains both output, and noted changes
Additional note; unfinished
output: error: likely deals with issues of each words tag, likely needs to entire 2d array as present in the other two programs and just set the indexs that arent set by the slides to zero
[nltk_data] Downloading package treebank to
[nltk_data]     C:\Users\aconl\AppData\Roaming\nltk_data...
[nltk_data]   Package treebank is already up-to-date!
[nltk_data] Downloading package universal_tagset to
[nltk_data]     C:\Users\aconl\AppData\Roaming\nltk_data...
[nltk_data]   Package universal_tagset is already up-to-date!
<BracketParseCorpusReader in 'C:\\Users\\aconl\\AppData\\Roaming\\nltk_data\\corpora\\treebank\\combined'>
[[('Pierre', 'NOUN'), ('Vinken', 'NOUN'), (',', '.'), ('61', 'NUM'), ('years', 'NOUN'), ('old', 'ADJ'), (',', '.'), ('will', 'VERB'), ('join', 'VERB'), ('the', 'DET'), ('board', 'NOUN'), ('as', 'ADP'), ('a', 'DET'), ('nonexecutive', 'ADJ'), ('director', 'NOUN'), ('Nov.', 'NOUN'), ('29', 'NUM'), ('.', '.')], [('Mr.', 'NOUN'), ('Vinken', 'NOUN'), ('is', 'VERB'), ('chairman', 'NOUN'), ('of', 'ADP'), ('Elsevier', 'NOUN'), ('N.V.', 'NOUN'), (',', '.'), ('the', 'DET'), ('Dutch', 'NOUN'), ('publishing', 'VERB'), ('group', 'NOUN'), ('.', '.')]]
('Pierre', 'NOUN')
('Vinken', 'NOUN')
(',', '.')
('61', 'NUM')
('years', 'NOUN')
('old', 'ADJ')
(',', '.')
('will', 'VERB')
('join', 'VERB')
('the', 'DET')
('board', 'NOUN')
('as', 'ADP')
('a', 'DET')
('nonexecutive', 'ADJ')
('director', 'NOUN')
('Nov.', 'NOUN')
('29', 'NUM')
('.', '.')
('Mr.', 'NOUN')
('Vinken', 'NOUN')
('is', 'VERB')
('chairman', 'NOUN')
('of', 'ADP')
('Elsevier', 'NOUN')
('N.V.', 'NOUN')
(',', '.')
('the', 'DET')
('Dutch', 'NOUN')
('publishing', 'VERB')
('group', 'NOUN')
('.', '.')
80310
20366
[('Drink', 'NOUN'), ('Carrier', 'NOUN'), ('Competes', 'VERB'), ('With', 'ADP'), ('Cartons', 'NOUN')]
12
{'PRON', 'ADP', '.', 'VERB', 'DET', 'NUM', 'X', 'ADJ', 'CONJ', 'PRT', 'ADV', 'NOUN'}
[[0.019, 0.0043, 0.041, 0.067], [0.0038, 0.035, 0.047, 0.007], [0.83, 0, 0.00047, 0], [0.004, 0.016, 0.087, 0.0045], [0.23, 0.00079, 0.0012, 0.00014]]
['PRON', 'ADP', '.', 'VERB']
          VB       TO       NN     PPSS
NN    0.0190  0.00430  0.04100  0.06700
TO    0.0038  0.03500  0.04700  0.00700
<s>   0.8300  0.00000  0.00047  0.00000
PPSS  0.0040  0.01600  0.08700  0.00450
VB    0.2300  0.00079  0.00120  0.00014
Traceback (most recent call last):
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexes\base.py", line 3361, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 76, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'PRON'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\aconl\Desktop\spring2022\Assignment2\Homework_2_HMMs_and_POS_Tagging_part3.py", line 137, in <module>
    tagged_seq = Viterbi(test_tagged_words)
  File "C:\Users\aconl\Desktop\spring2022\Assignment2\Homework_2_HMMs_and_POS_Tagging_part3.py", line 104, in Viterbi
    transition_p = tags_df.loc['PPSS', tag]
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexing.py", line 925, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexing.py", line 1100, in _getitem_tuple
    return self._getitem_lowerdim(tup)
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexing.py", line 862, in _getitem_lowerdim
    return getattr(section, self.name)[new_key]
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexing.py", line 931, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexing.py", line 1164, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexing.py", line 1113, in _get_label
    return self.obj.xs(label, axis=axis)
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\generic.py", line 3776, in xs
    loc = index.get_loc(key)
  File "C:\Users\aconl\AppData\Local\Programs\Thonny\lib\site-packages\pandas\core\indexes\base.py", line 3363, in get_loc
    raise KeyError(key) from err
KeyError: 'PRON'

changes:
line 6: added: from IPython.display import display
line 38: changed: print(train_tagged_words[:5]) (print added)
lines 43-47: comment: explains some of result
#use_tags = ['NUM', 'PRT', 'CONJ', '.', 'DET', 'ADP', 'VERB', 'ADV', 'PRON', 'ADJ', 'X', 'NOUN']
#note; given matrices are slightly adjusted based on which tag is went thru first
#based on tags, the use_tags commented out is what the article writer uses by chance.
#doesn't change the final accuracy rating, the only thing that changes is that unknown words
#take whatever the first tag is (in articles case it is NUM)
lines 79-84: changed: 
#I realize that the others aren meant to be zeroed out, but that also held issues
tags_matrix = [[.019, .0043, .041, .067],
           [.0038, .035, .047, .0070],
           [.83, 0, .00047, 0],
           [.0040, .016, .087, .0045],
           [.23, .00079, .0012, .00014]]

lines 147-172: commented out: full code to test all sentences
lines 178-183: changed: patterns changed to better match new tokenization
    (r'.*ing$', 'VB'),               # gerunds
    (r'.*ed$', 'VB'),                # simple past
    (r'.*es$', 'VB'),                # 3rd singular present
    (r'.*\'s$', 'NN'),               # possessive nouns
    (r'.*s$', 'NN'),                 # plural nouns
    (r'.*', 'NN')                     # nouns (default)