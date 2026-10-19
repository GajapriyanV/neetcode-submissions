class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        wordMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                wordMap[pattern].append(word)
        
        q = deque([beginWord])
        steps = 1
        visit = set([beginWord])
        while q:
            for _ in range(len(q)):
                curWord = q.popleft()

                if curWord == endWord:
                    return steps
                
                for i in range(len(curWord)):
                    pattern = curWord[:i] + "*" + curWord[i + 1:]
                    for nei in wordMap[pattern]:
                        if nei not in visit:
                            q.append(nei)
            steps +=1
        
        return 0

        



        