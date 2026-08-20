class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = b = c = False

        for triplet in triplets:
            a1, b1, c1 = triplet

            if a1 == target[0] and b1 <= target[1] and c1 <= target[2]:
                a = True

            if a1 <= target[0] and b1 == target[1] and c1 <= target[2]:
                b = True

            if a1 <= target[0] and b1 <= target[1] and c1 == target[2]:
                c = True

            if a and b and c:
                return True

        return False