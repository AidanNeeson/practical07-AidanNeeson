import pytest
import tf_objectoriented

@pytest.mark.parametrize(
    "input_file,expected_length",
    [("tests/inputs/cats.txt", 12), ("tests/inputs/dogs.txt", 13)]
)
def test_DataStorageManager_populates_data(input_file, expected_length):
    # Given the input file
    storage_manager = tf_objectoriented.DataStorageManager(input_file)

    # When, words are accessed
    word_list = storage_manager.words()

    # Then, words are populated
    assert word_list is not None
    assert len(word_list) == expected_length


@pytest.mark.parametrize(
    "word,expected_bool_result",
    [("a", True), ("apple", False)]
)
def test_StopWordManager_detects_stop_words(word, expected_bool_result):
    # Given some stop words
    stop_words_manager = tf_objectoriented.StopWordManager()

    # Check if its a stop word
    is_stop_word = stop_words_manager.is_stop_word(word)

    # Determine if its correct
    assert is_stop_word == expected_bool_result


@pytest.mark.parametrize(
    "word_list,expected_sorted_frequencies",
    [(["good", "good", "good", "hello", "bye", "bye", "bad"], [("good", 3), ("bye", 2), ("hello", 1), ("bad", 1)]),
    (["okay", "okay", "no", "no", "no", "no", "yes", "why", "why", "why"], [("no", 4), ("why", 3), ("okay", 2), ("yes", 1)])]
)
def test_WordFrequencyManager_returns_sorted_counts(word_list, expected_sorted_frequencies):
    # Given a list of words
    word_frequency_manager = tf_objectoriented.WordFrequencyManager()

    # Count their frequencies
    for word in word_list:
        word_frequency_manager.increment_count(word)
    
    # Sort the counts
    sorted_frequencies = word_frequency_manager.sorted()

    # Determine if its the same
    assert sorted_frequencies == expected_sorted_frequencies