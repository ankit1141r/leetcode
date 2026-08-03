class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApples = 0
        for a in apple:
            totalApples+=a  
           
        capacity.sort(reverse=True)

        usedBoxes = 0
        currentCapacity = 0

        for  cap in capacity:
            currentCapacity += cap
            usedBoxes+=1
            if (currentCapacity >= totalApples):
                break

        return usedBoxes
           

    