import pytest
import tf_objectoriented

# TODO: Parametrize this test
def test_DataStorageManager_populates_data():
    # Given the input file
    storage_manager = tf_objectoriented.DataStorageManager("tests/inputs/cats.txt")

    # When, words are accessed
    word_list = storage_manager.words()

    # Then, words are populated
    assert word_list is not None
    assert len(word_list) == 12


# TODO: Test the StopWordManager

# TODO: Test the WordFrequencyManager
