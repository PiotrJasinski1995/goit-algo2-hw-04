from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, suffix: str) -> int:
        """
        Count how many words stored in the Trie end with the given suffix.
        """
        if not isinstance(suffix, str):
            raise TypeError("Suffix must be a string.")
    
        result = 0
        if suffix:  # only run if suffix is not empty
            for word in self.keys():
                if word.endswith(suffix):
                    result += 1
        return result

    def has_prefix(self, prefix: str) -> bool:
        """
        Check whether there is at least one word that starts with the given prefix.
        """
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string.")

        result: bool = False
        if prefix:  # only check if prefix is not empty
            result = len(self.keys_with_prefix(prefix)) > 0

        return result


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Check for words that end with the given suffix
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Check for prefix existence
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("Task 1 - all tests passed")
