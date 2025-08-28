from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, words: list[str]) -> str:
        """
        Find the longest common prefix among all the given words.
        """
        if not isinstance(words, list) or any(not isinstance(w, str) for w in words):
            raise TypeError("Input must be a list of strings.")
        if not words:
            return ""

        # The longest common prefix cannot be longer than the shortest word
        shortest_word = min(words, key=len)

        prefix_chars = []
        for idx, char in enumerate(shortest_word):
            # Check if this character is present in the same position in all words
            if all(word[idx] == char for word in words):
                prefix_chars.append(char)
            else:
                break
        return "".join(prefix_chars)


if __name__ == "__main__":
    # Test 1
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["flower", "flow", "flight"]) == "fl"

    # Test 2
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(
        ["interspecies", "interstellar", "interstate"]) == "inters"

    # Test 3
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["dog", "racecar", "car"]) == ""

    print("Task 2 - all tests passed")
    