import random
import time


class Sorter:
    def __init__(self, param_list):
        self.param_list = param_list

    @staticmethod
    def sort(self, param_list):
        return sorted(param_list)

    @staticmethod
    def __bubble(self, param_list):
        for i in range(len(param_list)):
            bubble_sorted = True
            for j in range(len(param_list) - i - 1):
                if param_list[j] > param_list[j + 1]:
                    param_list[j], param_list[j + 1] = param_list[j + 1], param_list[j]
                    bubble_sorted = False
            if bubble_sorted:
                break
        return param_list

    @staticmethod
    def __insertion(self, param_list):
        for i in range(len(param_list)):
            k = param_list[i]
            j = i - 1
            while j >= 0 and param_list[j] > k:
                param_list[j + 1] = param_list[j]
                j -= 1
            param_list[j + 1] = k
        return param_list

    def custom_sort(self, param_list, criteria="default"):
        match criteria:
            case "default":
                return Sorter.sort(self, param_list)
            case "bubble":
                return Sorter.__bubble(self, param_list)
            case "insert":
                return Sorter.__insertion(self, param_list)


def main():
    arr = [8, 2, 6, 4, 5]
    arr1 = random.sample(range(10000), 5000)
    s = Sorter
    t1 = time.time()
    # print(s.sort(s, arr))
    s.sort(s, arr1)
    t2 = time.time()
    print(f"Default sorting: {round(t2 - t1, 3)}")
    s.custom_sort(s, arr1, criteria="bubble")
    t3 = time.time()
    print(f"bubble sorting: {round(t3 - t1, 3)}")
    s.custom_sort(s, arr1, criteria="insert")
    t4 = time.time()
    print(f"Insertion sorting: {round(t4 - t1, 3)}")


if __name__ == "__main__":
    main()
