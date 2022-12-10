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

The steps I took to parametrize the given test was to first add the parametrize decorator at the top of the function. This allows pytest to see that it is supposed to be a parametrized test. I then looked through the class in question as well as the test provided to find out what variables I would need to include as parameters, and then I added them into the decorator. I then put the specified variable names included in the decorator inside of the function definition as parameters as well. Lastly, I went into the test and removed the hard coded instances of parameters and replaced them with the created variables.

## Analyze the complexity of the Object-Oriented program. Your response should include at least some of the words, "cognitive load", "change amplification", "unknown unknowns", and "dependencies". Please make sure to write three to five sentences *that contain examples from the program* to support your answer

The complexity of the Object-Oriented program is, on the surface, a lot more complex than the other methods, but in terms of its actual comlpexity, it is a lot less complex. This is because the cognitive load is even furhter minimized in this program by the use of abstractions at the method and class level like `WordFrequencyController` and `is_stop_word()`. These offer fairly broad, but easy to understand functionality at the interface level that seem to hide much of the complex work that is happening behind the scenes. The only thing increasing cognitive load in this program is the need for understanding dependencies like `re`, `sys`, `string`, and `abc`. In terms of change amplification, it is merely contained to the object within a class. The only time this could ever be affected negatively is if the public interface itself was edited. Unknown unknowns here are increased, however, due to the shared state. 

## Describe your experience unit testing the Object-Oriented program. Was it easier or harder or about the same level of difficulty as unit testing the Cookbook and Pipeline programming styles? Please make sure to write three to five sentences *that contain examples from the tests* to support your answer

Overall, it was a lot easier to unit test the Object-Oriented program compared to the Cookbook and Pipeline programs. This is because the shared state in this program did not affect the tests inputs in the same way it did before. It allowed for inputs to be a lot easier to determine, which also made parametrization significantly easier. 
```python
@pytest.mark.parametrize(
    "input_file,expected_length",
    [("tests/inputs/cats.txt", 12), ("tests/inputs/dogs.txt", 13)]
)
```
As seen above, the process is fairly simple compared to the other tests. The only drawback is needing to create objects in every test by doing something similar to `stop_words_manager = tf_objectoriented.StopWordManager()`, but this ends up being intuitive and not obstructive in the long run, unlike some of the setup for previous tests. The abstractions also helped to determine which processes to test, and which methods should be used to test the processes, which was harder to pick out in the previous programs.
