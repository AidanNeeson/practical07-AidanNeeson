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
  - Overall purpose: To serve as the controller of the purpose of the program. It manages all other objects to, in the end, create a finished frequency counting process.
  - Behavior of `run` method: It counts the frequency of all words given to it and displays then on the command-line.
- `DataStorageManager`
  - Overall purpose: Reads in and stores the contents of a file in a fashion that it is easily parasable.
  - Behavior of `words` method: Returns the a list of all of the words in the file.
- `StopWordManager`
  - Overall purpose: Creates a filter for all "stop words" and manages that procedure.
  - Behavior of `is_stop_word` method: Checks if an input word is a "stop word" and then returns True or False.
- `WordFrequencyManager`
  - Overall purpose: Stores and manages the data about the frequency of the words.
  - Behavior of `increment_count` method: Either adds a word to the dictionary and sets the count to one, or it increases the count of a word by one.
  - Behavior of `sorted` method: Returns a a sorted list of tuples that are ordered by their frequency.

## Describe the general steps you took to parametrize the given test

TODO

## Analyze the complexity of the Object-Oriented program. Your response should include at least some of the words, "cognitive load", "change amplification", "unknown unknowns", and "dependencies". Please make sure to write three to five sentences *that contain examples from the program* to support your answer

TODO

## Describe your experience unit testing the Object-Oriented program. Was it easier or harder or about the same level of difficulty as unit testing the Cookbook and Pipeline programming styles? Please make sure to write three to five sentences *that contain examples from the tests* to support your answer

TODO
