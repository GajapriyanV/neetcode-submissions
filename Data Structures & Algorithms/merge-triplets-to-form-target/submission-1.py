class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = b = c = False

        for triplet in triplets:
            a1, b1, c1 = triplet

            if a1 == target[0] and b1 <= target[1] and c1 <= target[2]:
                a1 = True
            if a1 <= target[0] and b1 == target[1] and c1 <= target[2]:
                b1 = True
            if a1 <= target[0] and b1 <= target[1] and c1 == target[2]:
                c1 = True
        
            if a1 and b1 and c1:
                return True
        return False

        