from typing import List

"""
Approach 1: Sort each string as key

Time Complexity: O(N*K*log(K)) where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K*log(K)) time.
Space Complexity: O(N*K), the total information content stored in the result
Did this code successfully run on Leetcode (Problem 49. Group Anagrams) : Yes
Any problem you faced while coding this : None

Approach:
We iterate through each string and compute a canonical key by sorting its characters, since two strings are anagrams if and only if their sorted forms are identical.
We use a hash map keyed on this sorted string to bucket all words that share the same sorted form together.
Finally, we return all the buckets (map values) as the grouped result.
"""
class SolutionSorting:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None or len(strs) == 0:
            return strs
        word_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in word_map:
                word_map[sorted_word] = [word]
            else:
                word_map[sorted_word].append(word)
        return list(word_map.values())


"""
Approach 2: Prime number multiplication as key

Time Complexity: O(N*K), where N is the length of strs and K is the maximum length of a string in strs — for each word we do a single linear pass to compute its product.
Space Complexity: O(N*K), the total information content stored in the result
Did this code successfully run on Leetcode (Problem 49. Group Anagrams) : Yes
Any problem you faced while coding this : None

Approach:
We assign each lowercase letter a unique prime number, then represent each word as the product of the primes corresponding to its characters.
By the fundamental theorem of arithmetic, this product is unique to a given multiset of characters regardless of their order, so anagrams always produce the same product.
We use a hash map keyed on this product to bucket all words sharing the same product together, avoiding the O(K*log(K)) sort per word from Approach 1.
"""
class SolutionPrimeProduct:
    def __init__(self):
        self.primes = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17,
            'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
            'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73,
            'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
        }

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None or len(strs) == 0:
            return strs
        word_map = {}
        for word in strs:
            product = 1
            for ch in word:
                product *= self.primes[ch]
            if product not in word_map:
                word_map[product] = [word]
            else:
                word_map[product].append(word)
        return list(word_map.values())


def run_tests():
    def normalize(result):
        # Order of groups and order within groups isn't guaranteed,
        # so normalize for comparison: sort each group, then sort the list of groups.
        return sorted(sorted(group) for group in result)

    test_cases = [
        # (strs, expected)
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["ab", "ba", "abc"], [["ab", "ba"], ["abc"]]),
        ([], []),
    ]

    solutions = {
        "Sorting": SolutionSorting(),
        "PrimeProduct": SolutionPrimeProduct(),
    }

    for name, solver in solutions.items():
        print(f"--- Testing {name} ---")
        for strs, expected in test_cases:
            result = solver.group_anagrams(strs)
            status = "PASS" if normalize(result) == normalize(expected) else "FAIL"
            print(f"{status}: strs={strs}, expected={expected}, got={result}")
        print()


if __name__ == "__main__":
    run_tests()