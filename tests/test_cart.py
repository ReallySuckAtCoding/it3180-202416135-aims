import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCartLimit(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa đầu tiên phải thành công (True)
        for i in range(20):
            dvd = DigitalVideoDisc(f"Title {i}", "Category", 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        
        # Thêm đĩa thứ 21 phải bị từ chối và trả về False
        dvd_extra = DigitalVideoDisc("Extra Title", "Category", 10.0)
        self.assertFalse(cart.add_dvd(dvd_extra))

if __name__ == '__main__':
    unittest.main()