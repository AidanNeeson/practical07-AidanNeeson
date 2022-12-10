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


# TODO: Test the StopWordManager

# TODO: Test the WordFrequencyManager
