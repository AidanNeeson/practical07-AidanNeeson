# Object-Oriented Programming Style

## Due Date: Friday, December 9th, 2022 by midnight

## Introduction

In this practical assignment, you will familiarize yourself with the Object-Oriented programming style by writing tests for an Object-Oriented program. Through this exercise, you will put into practice the following learning objective(s):

- The constraints associated with the Object-Oriented programming style and how to implement it in Python
- The complexity associated with the Object-Oriented programming style
- Whether the Object-Oriented programming style support unit testing
- How to write parametrized tests

## Instructions

Please perform each of the following steps in order.

### Install Dependencies

Install the dependencies listed in `pyproject.toml` by running `poetry install`.

### Run and Analyze the Object-Oriented Term Frequency Program

Run the Object-Oriented term frequency program by running `poetry run python tf_objectoriented.py pride_and_prejudice.txt`. You should see the following output.

```python
mr - 786
elizabeth - 635
very - 488
darcy - 418
such - 395
mrs - 343
much - 329
more - 327
bennet - 323
bingley - 306
jane - 295
miss - 283
one - 275
know - 239
before - 229
herself - 227
though - 226
well - 224
never - 220
sister - 218
soon - 216
think - 211
now - 209
time - 203
good - 201
```

Read through the Object-Oriented program, line-by-line, making sure that you understand how the program produces its output. Then, in `writing/reflection.md`, describe the overall purpose of each of the classes in the Object-Oriented program and the behaviors of the methods listed in the reflection question.

### Parametrize a Given Test

Look at the given test in `tests/test_tf_objectoriented.py`. Notice that it tests the behavior of the `DataStorageManager` and its input is an input file and its expected output is a list of words that contains all of the words in the input file. Also, notice that this expected output is tested by checking the length of the list of words. Run this test by running `poetry run task test`. You will see that the test passes! However, you will also see that the overall test suite fails due to a test coverage requirement. You should ignore this for now; in later steps, you will write more tests that will increase the test coverage.

While this test is correctly written, you can increase your confidence in the behavior of the `DataStorageManager` by adding test cases for additional inputs and expected outputs using parametrization. Modify the given test so that it has at least two test cases; this may involve adding an additional input file to the `tests/inputs` folder. Make sure you have correctly parametrized the test by running `poetry run task test`; you should see that you have at least two tests that have all passed.

In `writing/reflection.md`, describe the general steps you took to parametrize this given test.

### Write Parametrized Tests

Now, you should write at least two additional tests to increase the test coverage and your confidence in the behavior of the rest of the Object-Oriented term frequency program. Specifically, you should test the following behaviors.

First, test the public behavior of the `StopWordManager`. You can determine its public behavior by analyzing how it is used by other classes. For example, if you look at the `WordFrequencyController`, which uses the `StopWordManager`, you will notice that the `StopWordManager` has a method called `is_stop_word` that is used by the `WordFrequencyController` to determine whether a word is a stop word. You should write a test that checks that `is_stop_word` detects only stop words. This test should be parametrized and have at least two test cases--one that checks that `is_stop_word` returns `True` when given a stop word and one that checks that `is_stop_word` returns `False` when given a non-stop word.

Secondly, test the behavior of the `WordFrequencyManager`. Looking at the `WordFrequencyController`, you will see that the `WordFrequencyManager` is used to keep track of a word's frequency with its `increment_count` method and also used to get the sorted frequencies of all words with its `sorted` method. You should write a test that checks that when `increment_count` is used, then `sorted` returns the correct frequencies of each word in sorted order. This test should be parametrized and have at least two test cases--each test case should run `increment_count` on the words in a word list and check that `sorted` returns the expected sorted frequencies of each word. To increase your confidence that `WordFrequencyManager` can handle any list of words, each parametrized test case should use a different list of words.

As you write these tests, verify that they work by regularly running `poetry run task test`. In the end, you should have at least three tests that each has at least two test cases through parametrization. You can check your progress by running GatorGrader.

### Reflect on Your Work

Answer all questions in `writing/reflection.md`. As you do, commit your changes using best commit practices. Instead of creating a commit at the end with the message, "Answer reflection questions", you should commit after answering each question and describe your changes in the commit messages.

### Run GatorGrader

You can gain an approximation of your progress on this assignment by running [GatorGrader](https://github.com/GatorEducator/gatorgrader) locally. You do need to have `gatorgrade` and Python installed to be able to run this command.

`gatorgrade --config config/gatorgrade.yml`

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk with either the course instructor or a student technical leader during the class session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Practical Assessment

The grade that a student receives on this practical assignment is a checkmark grade (0 or 1) and is based on:

- **GitHub Actions CI Build Status**: Students are encouraged to repeatedly try to complete the assignment until it passes all GitHub Actions jobs. Students will receive a checkmark grade if their last before-the-deadline build passes and a green ✔ appears in their GitHub commit log instead of a red ✗.

Students will receive 1 if their solution passes all GatorGrader checks and receives a green ✔ in their last commit.

All grades for this project will be reported through a student's GitHub gradebook repository.
