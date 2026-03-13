"""
题意: 收银系统，每第 n 单打折。
思路1: 哈希表存价格，计数器记录订单数。
复杂度: 构造 O(m)，结算 O(p)。
思路2: 另一种实现，逻辑相同但接口更直观。
复杂度: 构造 O(m)，结算 O(p)。
"""

# Time:  ctor:    O(m), m is the number of all products
#        getBill: O(p), p is the number of products to bill
# Space: O(m)

class Cashier:

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.__n = n
        self.__discount = discount
        self.__curr = 0
        self.__lookup = {p: prices[i] for i, p in enumerate(products)}

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        self.__curr = (self.__curr + 1) % self.__n
        result = 0.0
        for i, p in enumerate(product):
            result += self.__lookup[p] * amount[i]
        return result * (1.0 - self.__discount / 100.0 if self.__curr == 0 else 1.0)


class Cashier2:
    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = discount
        self.count = 0
        self.price = {p: prices[i] for i, p in enumerate(products)}

    def getBill(self, product, amount):
        self.count += 1
        total = 0.0
        for i, p in enumerate(product):
            total += self.price[p] * amount[i]
        if self.count % self.n == 0:
            total *= (1.0 - self.discount / 100.0)
        return total
