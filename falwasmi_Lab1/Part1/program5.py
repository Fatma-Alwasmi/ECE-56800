class PairFinder:
    def find_indices(self, numbers, target):
        num_dict = {}
        for index, num in enumerate(numbers):
            complement = target - num
            if complement in num_dict:
                return (num_dict[complement], index)
            num_dict[num] = index
        return None

numbers = [10, 20, 10, 40, 50, 60, 70]
target = int(input("What is your target number? "))

finder = PairFinder()
result = finder.find_indices(numbers, target)

print(f"index1={result[0]}, index2={result[1]}")