import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_changes_exm_1(self):
        '''Test a1.stock_price_summary with empty list.'''

        list=[]
        actual=a1.stock_price_summary(list)
        expected=(0,0)
        self.assertEqual(expected, actual)

    def test_stock_price_changes_exm_2(self):
        '''Test a1.stock_price_summary with one positive value in list.'''

        list=[3]
        actual=a1.stock_price_summary(list)
        expected=(3,0)
        self.assertEqual(expected, actual)
    
    def test_stock_price_changes_exm_3(self):
        '''Test a1.stock_price_summary with one neg value in the list.'''

        list=[-2]
        actual=a1.stock_price_summary(list)
        expected=(0,-2)
        self.assertEqual(expected, actual)
    
    def test_stock_price_changes_exm_4(self):
        '''Test a1.stock_price_summary with 0 along with both pos & neg value in the list.'''

        list=[2,0,-4]
        actual=a1.stock_price_summary(list)
        expected=(2,-4)
        self.assertEqual(expected, actual)

    def test_stock_price_changes_exm_5(self):
        '''Test a1.stock_price_summary with multiple value in the list.'''

        list=[1.01,-2.00,0,3.15,-4.21,0.97,-0.54,0]
        actual=a1.stock_price_summary(list)
        expected=(5.13,-6.75)
        self.assertEqual(expected, actual)






if __name__ == '__main__':
    unittest.main(exit=False)


