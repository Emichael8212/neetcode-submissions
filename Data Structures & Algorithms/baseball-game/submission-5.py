class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        sum_score = 0
        for i in range(len(operations)):
            if operations[i] == 'D':
                score.append(2 * int(score[-1]))
                sum_score += score[-1]
            elif operations[i] == '+':
                score.append((score[-1] + score[-2]))
                sum_score += score[-1]
            elif operations[i] == 'C':
                sum_score -= score[-1]
                score.pop()
            else:
                score.append(int(operations[i]))
                sum_score += score[-1]
        return sum(score)