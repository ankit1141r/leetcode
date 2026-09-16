class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        numbers = set()

        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                numbers.add((a*100+b*10+c))

        return list(sorted(numbers))
        
        
        
