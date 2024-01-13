"""购物清单案例"""

class ShoppingList:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    # 返回清单的商品个数
    def get_item_count(self):
        return len(self.shopping_list)

    # 返回清单商品的总价值
    def get_total_price(self):
        i = 0
        for price in self.shopping_list.values():
            i += price
        return i

