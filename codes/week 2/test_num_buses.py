import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_Num_Buses_exm_1(self):
        ''' test num_buses method for zero value '''
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_Num_Buses_exm_2(self):
        ''' test num_buses method for minimum non zero value '''
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_Num_Buses_exm_3(self):
        ''' test num_buses method for thresold point value '''
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)
    
    def test_Num_Buses_exm_4(self):
        ''' test num_buses method for break point value '''
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)
    
    def test_Num_Buses_exm_5(self):
        ''' test num_buses method for large value '''
        actual = a1.num_buses(160)
        expected = 4
        self.assertEqual(expected, actual)

    

if __name__ == '__main__':
    unittest.main(exit=False)
