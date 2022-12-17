class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        freq = list(c.items())
        freq.sort(key=lambda x: x[1], reverse=True)
        
        return ''.join([k * v for k, v in freq])