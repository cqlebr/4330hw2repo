import unittest
from typing import List

class BubbleSort:
    def sort(self, arr: List[int]) -> List[int]:
        
        if arr is None:
            raise TypeError("Array is Empty")
        
        if not isinstance(arr, list):
            raise TypeError("Not a List")
        
        if not all(isinstance(x, (int, float)) for x in arr):
            raise TypeError("Not all elements are numeric")
        
        if len(arr) == 0:
            return []
        

        n = len(arr)
        for k in range(n):
            swapped = False
            for j in range(0, n - k - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr                

class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.bubble_sort = BubbleSort()

    def printMsg(self, fst, snd, msg):
        if not self.assertEqual(fst,snd):
            print(f"\nTest Passed for {msg}")
            print(f"Expected: {snd}")
            print(f"Result: {fst}")
        else:
            print(f"\nTest Failed for {msg}")
            print(f"Expected: {snd}")
            print(f"Result: {fst}")

    def testSorting(self):
        input = [43, 12, 76, 123, 87, 9]
        result = [9, 12, 43, 76, 87, 123]
        answer = self.bubble_sort.sort(input)
        self.printMsg(answer, result, "Regular Sorting Array")
    
    def testDupValues(self):
        input = [12, 53, 34, 12, 54]
        result = [12, 12, 34, 53, 54]
        answer = self.bubble_sort.sort(input)
        self.printMsg(answer, result, "Duplicate Values Array")
    
    def testSingleElem(self):
        input = [1]
        result = [1]
        answer = self.bubble_sort.sort(input)
        self.printMsg(answer, result, "Single Element Array")
    
    def testEmptyArr(self): 
        input = []
        result = []
        answer = self.bubble_sort.sort(input)
        self.printMsg(answer, result, "Empty Array")

    def testAlreadySorted(self):
        input = [1, 2, 3, 4]
        result = [1, 2, 3, 4]
        answer = self.bubble_sort.sort(input)
        self.printMsg(answer, result, "Already Sorted Array")
    
    def testReverseSorted(self):
        input = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]
        answer = self.bubble_sort.sort(input)
        self.printMsg(answer, result, "Reverse Sorted Array")
    
    def testIdempotency(self):
        input = [43, 65, 1, 76, 98, 123, 542, 12]
        result = [1, 12, 43, 65, 76, 98, 123, 542]
        answer = self.bubble_sort.sort(input)
        self.printMsg(answer, result, "First Idempotency Test")

        secondanswer = self.bubble_sort.sort(answer)
        self.printMsg(answer, result, "Second Idempotency Test")

    def testInvalidElem(self):
        print(f"\nTesting Invalid Elements")
        try:
            self.bubble_sort.sort([32, 54, "2", 3])
            print(f"\tTest Failed for Invalid Elements")
        except TypeError as e:
            print(f"\tTest Passed for Invalid Elements")
    

if __name__ == '__main__':
    unittest.main()