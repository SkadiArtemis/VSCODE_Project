class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        place = sorted(score, reverse=True)

        medal = {
            1: 'Gold Medal',
            2: 'Silver Medal',
            3: 'Bronze Medal'
        }

        rank = {s: str(i + 1) if i >= 3 else medal[i + 1] for i, s in enumerate(place)}

        return [rank[s] for s in score]