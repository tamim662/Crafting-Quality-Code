import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    ''' Since the function swap_k doesn't return value there's no point testing fot it,
        but we can check the result what  it supposed to be.For example the initial list will
        be changed after swap operation, we can look on it does it really changed according to 
        k items swap.'''

    def test_swap_k_exm_1(self):
        '''Test a1.swap_k with  k equal to zero'''
        nums = [4, 5, 6,7,8]
        a1.swap_k(nums,0) # where k=0
        expected=[4, 5, 6,7,8]
        self.assertEqual(expected, nums)

    def test_swap_k_exm_2(self):
        '''Test a1.swap_k with  k equal to 1'''
        nums = [4, 5, 6,7,8]
        a1.swap_k(nums,1) # where k=1 <= len(nums)=5
        expected=[8, 5, 6,7,4]
        self.assertEqual(expected, nums)

    def test_swap_k_exm_3(self):
        '''Test a1.swap_k with  k value more than 1'''
        nums = [4, 5, 6,7,8]
        a1.swap_k(nums,2) # where k=2 <= len(nums)=5
        expected=[7, 8, 6,4,5]
        self.assertEqual(expected, nums)
        


if __name__ == '__main__':
    unittest.main(exit=False)
