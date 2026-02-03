from typing import List

def topKFrequent( words: List[str], k: int) -> List[str]:
    hash_map = {}
    for word in words:
        hash_map[word] = hash_map.get(word, 0) + 1

    # Sort by frequency (descending), then lexicographically (ascending)
    sorted_words = sorted(hash_map.keys(), key=lambda x: (-hash_map[x], x))
    return sorted_words[:k]

words = ["love","leetcode","i","love","coding", "i"]
k = 2

print(topKFrequent(words, k))