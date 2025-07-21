class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1 and not trust:
            return 1

        trust_scores = [0] * (n + 1)

        for a, b in trust:
            trust_scores[a] -= 1  # a trusts someone, can't be judge
            trust_scores[b] += 1  # b is trusted by someone

        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i

        return -1
