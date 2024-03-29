class Solution:
  def bestClosingTime(self, customers: str) -> int:
    ans = 0
    profit = 0
    maxProfit = 0

    for i, customer in enumerate(customers):
      profit += 1 if customer == 'Y' else -1
      if profit > maxProfit:
        maxProfit = profit
        ans = i + 1

    return ans