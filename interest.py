def loan_calc(amount,rate,time):
    intrest=amount*(rate/100)*(time/12)
    total_val=intrest+amount
    return(total_val)


import unittest

class MyTest (unittest.TestCase):
    def test_loan_calc(self):
        self.assertEqual(loan_calc(1000,10,10),1083.3333333333333)

    def test_loan_calc2(self):
        self.assertEqual(loan_calc(1000,0,0),1000)    

   
        
unittest.main(verbosity=2)
