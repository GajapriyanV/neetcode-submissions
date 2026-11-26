class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjMap = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                wordMap = word[:i] + "*" + word[i + 1:]
                adjMap[wordMap].append(word)

        q = deque([beginWord])
        turns = 1
        visit = {beginWord}

        while q:
            for _ in range(len(q)):
                newWord = q.popleft()

                if newWord == endWord:
                    return turns

                for i in range(len(newWord)):
                    wordMap = newWord[:i] + "*" + newWord[i + 1:]

                    for word in adjMap[wordMap]:
                        if word not in visit:
                            q.append(word)
                            visit.add(word)

            turns += 1

        return 0