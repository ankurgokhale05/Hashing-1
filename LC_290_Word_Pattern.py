from typing import List

"""
Approach: Two hash maps for bidirectional mapping

Time Complexity: O(N + M), where N is the length of pattern and M is the length of the string (from splitting on whitespace and iterating once).
Space Complexity: O(N), for storing up to N entries in each hash map.
Did this code successfully run on Leetcode (Problem 290. Word Pattern) : Yes
Any problem you faced while coding this : None

Approach:
We split the input string into words and first check that the word count matches the pattern's length, since a mismatch immediately rules out a valid mapping.
We then maintain two hash maps, one mapping pattern characters to words and one mapping words back to pattern characters, enforcing a strict one-to-one correspondence in both directions.
At each index, if either side has been mapped before, we verify it's consistent with the current pair; any contradiction means the pattern doesn't match, otherwise we record the new mapping and continue.
"""
class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        word_dict = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = words[i]
            else:
                if pattern_dict[pattern[i]] != words[i]:
                    return False

            if words[i] not in word_dict:
                word_dict[words[i]] = pattern[i]
            else:
                if word_dict[words[i]] != pattern[i]:
                    return False
        return True


def run_tests():
    test_cases = [
        # (pattern, s, expected)
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
        ("a", "dog", True),
        ("ab", "dog dog", False),
        ("abc", "dog cat fish", True),
    ]

    solver = Solution()
    print("--- Testing HashMap ---")
    for pattern, s, expected in test_cases:
        result = solver.word_pattern(pattern, s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: pattern={pattern!r}, s={s!r}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()