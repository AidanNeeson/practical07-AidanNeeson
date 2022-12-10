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

# TODO: Test the WordFrequencyManager
