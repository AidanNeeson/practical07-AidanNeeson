# Reflection on the Object-Oriented Programming Style

## Describe the high-level behavior of the Object-Oriented term frequency program

The Object-Oriented term frequency program counts the frequency of words in a given text, and displays the 25 most frequent words that are not "stop words".

## For each of the four constraints associated with the Object-Oriented programming style, provide an example from the Object-Oriented program where the constraint is reflected

Problem being broken down into "things":
```python
DataStorageManager(path_to_file)
StopWordManager()
WordFrequencyManager()
```

Data and procedures:
```python
self._word_freqs = {} # data

def increment_count(self, word): # procedure
```

Data only accessed through procedures:
```python
# method calls like, `words()`, use the data to accomplish a task, the data is never accessed directly outside of a method
for w in self._storage_manager.words():
            if not self._stop_word_manager.is_stop_word(w):
                self._word_freq_manager.increment_count(w)
```

Objects can reuse procedures defined elsewhere:
```python
# this is procdure is defined in a different class, but is used by each other class
super(WordFrequencyManager, self).info()
```

## Describe the overall purpose of each of the classes in the Object-Oriented program and the behaviors of the methods listed below

- `WordFrequencyController`
  - Overall purpose: TODO
  - Behavior of `run` method: TODO
- `DataStorageManager`
  - Overall purpose: TODO
  - Behavior of `words` method: TODO
- `StopWordManager`
  - Overall purpose: TODO
  - Behavior of `is_stop_word` method: TODO
- `WordFrequencyManager`
  - Overall purpose: TODO
  - Behavior of `increment_count` method: TODO
  - Behavior of `sorted` method: TODO

## Describe the general steps you took to parametrize the given test

TODO

## Analyze the complexity of the Object-Oriented program. Your response should include at least some of the words, "cognitive load", "change amplification", "unknown unknowns", and "dependencies". Please make sure to write three to five sentences *that contain examples from the program* to support your answer

TODO

## Describe your experience unit testing the Object-Oriented program. Was it easier or harder or about the same level of difficulty as unit testing the Cookbook and Pipeline programming styles? Please make sure to write three to five sentences *that contain examples from the tests* to support your answer

TODO
