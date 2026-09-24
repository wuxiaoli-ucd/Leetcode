from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dict = {}
        invalid = set()

        # 逻辑关系是，我其实先去每一个交易，第一件事，先看是否大于1000块，再的话直接invalid, 同时字典里把他加进去。否则的话。我去扫字典里有没有他的兄弟，有兄弟的话就是也变成invalid，然后把他加进去字典里

        for i, v in enumerate(transactions):
            name, time, amount, city = v.split(",")
            time = int(time)
            amount = int(amount)
            if int(amount) > 1000:
                invalid.add(i)

            # 这里有一个很容易的错误点，就是如果我的金额是大于1000的我就不会去判断他之前的可能有关系的可以同伙了，这样就会miss数据
            if name in dict:
                for index, prev_time, prev_amount, prev_city in dict[name]:
                    if abs(time - prev_time) <= 60 and city != prev_city:
                        invalid.add(index)
                        invalid.add(i)

            if name not in dict:
                dict[name] = []
            dict[name].append([i, int(time), int(amount), city])

        return [transactions[i] for i in invalid]


if "__main__" == __name__:
    solution = Solution()
    transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
    res = solution.invalidTransactions(transactions)
    print(res)