from typing import List

"""
Approach 1: Two hash maps for bidirectional mapping

Time Complexity: O(N), where N is the length of s (and t), since we make a single pass through both strings.
Space Complexity: O(1), since the number of distinct characters is bounded by the fixed character set size (not the input length).
Did this code successfully run on Leetcode (Problem 205. Isomorphic Strings) : Yes
Any problem you faced while coding this : None

Approach:
We maintain two hash maps, one mapping characters of s to t and one mapping characters of t back to s, to enforce a strict one-to-one correspondence in both directions.
At each index, if a character has been mapped before, we check that it still maps to the same character on the other side; if it contradicts the existing mapping, the strings aren't isomorphic.
If no contradiction is found by the end, we record the new mapping and continue, returning True once the full pass completes cleanly.
"""
class SolutionHashMap:
    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_mapping = {}
        t_mapping = {}
        for i in range(len(s)):
            if s[i] in s_mapping and s_mapping[s[i]] != t[i]:
                return False
            if t[i] in t_mapping and t_mapping[t[i]] != s[i]:
                return False
            s_mapping[s[i]] = t[i]
            t_mapping[t[i]] = s[i]
        return True


"""
Approach 2: Fixed-size arrays storing last-seen index

Time Complexity: O(N), where N is the length of s (and t), since we make a single pass through both strings.
Space Complexity: O(1), since the arrays are fixed at size 256 regardless of input length.
Did this code successfully run on Leetcode (Problem 205. Isomorphic Strings) : Yes
Any problem you faced while coding this : None

Approach:
Instead of hash maps, we use two fixed-size arrays indexed by character code, where each slot stores the last index (1-based, so 0 means unseen) at which that character appeared.
At each position, if the recorded index for s[i] doesn't match the recorded index for t[i], the two characters have been mapped inconsistently, so the strings aren't isomorphic.
Otherwise we update both arrays with the current index (i + 1) and continue, returning True once the full pass completes cleanly.
"""
class SolutionArray:
    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_mapping = [0 for _ in range(256)]
        t_mapping = [0 for _ in range(256)]
        for i in range(len(s)):
            if s_mapping[ord(s[i])] != t_mapping[ord(t[i])]:
                return False
            s_mapping[ord(s[i])] = i + 1
            t_mapping[ord(t[i])] = i + 1
        return True


def run_tests():
    test_cases = [
        # (s, t, expected)
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "aa", False),
    ]

    solutions = {
        "HashMap": SolutionHashMap(),
        "Array": SolutionArray(),
    }

    for name, solver in solutions.items():
        print(f"--- Testing {name} ---")
        for s, t, expected in test_cases:
            result = solver.is_isomorphic(s, t)
            status = "PASS" if result == expected else "FAIL"
            print(f"{status}: s={s!r}, t={t!r}, expected={expected}, got={result}")
        print()


if __name__ == "__main__":
    run_tests()