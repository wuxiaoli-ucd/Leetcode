class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_good = 0
        good = 0
        open_day = 0
        for i, v in enumerate(customers):

            if v == "Y":
                good += 1
                if good > max_good:
                    max_good = good
                    open_day = i + 1
            else:
                good -= 1

        return open_day