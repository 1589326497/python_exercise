import unittest  # 单元测试库头文件
from shopping_list import ShoppingList  # 将需要测试的类导入


class testShoppingList(unittest.TestCase):
    def setUp(self):  # setUp函数名不能改 类似于init函数用来存放属性
        self.shopping_list = ShoppingList({"洗衣机": 7, "手机": 8})

    def test_get_item_count(self):  # 定义测试用例 必须用text_开头
        self.assertEqual(3, self.shopping_list.get_item_count())  # 等价于 assert shopping_list.get_item_count()==2

    def test_get_total_price(self):
        self.assertEqual( 15,self.shopping_list.get_total_price())


