from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the "#" separating the length from the word
            while s[j] != "#":
                j += 1

            cur_len = int(s[i:j])

            word_start = j + 1
            word_end = word_start + cur_len

            res.append(s[word_start:word_end])

            i = word_end

        return res