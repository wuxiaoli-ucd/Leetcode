class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = 0
        while income > 0:
            last_upper = 0
            for i,v in enumerate(brackets):
                upper,percent = v[0],v[1]
                if income >= upper-last_upper:
                    tax+=(upper-last_upper)*percent/100
                    income-=(upper-last_upper)
                else:
                    tax+=income*percent/100
                    income = 0
                    return tax
                last_upper = upper
        return tax