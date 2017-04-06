def find_max_min(array):
  min_num=max_num=array[0]
  for i in array[1:]:
    if i < min_num:
      min_num = i
    else:
      if i > max_num:
        max_num = i
    if min_num==max_num:
      return [i]
  return [min_num,max_num]

import unittest
class MaxMinTest(unittest.TestCase):
    """docstring for MaxMinTest"""

    def test_find_max_min_four(self):
        self.assertListEqual([1, 4],
                             find_max_min([1, 2, 3, 4]),
                             msg='should return [1,4] for [1, 2, 3, 4]')

    def test_find_max_min_one(self):
        self.assertListEqual([4, 6],
                             find_max_min([6, 4]),
                             msg='should return [4, 6] for [6, 4]')

    def test_find_max_min_two(self):
        self.assertListEqual([2, 78],
                             find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]),
                             msg='should return [2, 78] for [4, 66, 6, 44, 7, 78, 8, 68, 2]')

    def test_find_max_min_three(self):
        self.assertListEqual([1, 4],
                             find_max_min([1, 2, 3, 4]),
                             msg='should return [1,4] for [1, 2, 3, 4]')

    def test_find_max_min_identity(self):
        self.assertListEqual([4],
                             find_max_min([4, 4, 4, 4]),
                             msg='Return the number of elements in the list in a new list if the `min` and `max` are equal')

unittest.main(verbosity=2)   
