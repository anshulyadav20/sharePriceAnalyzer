from companySharesAnalyzer import CompanyShareAnalyzer
import unittest
class TestCompanyShareAnalyzer(unittest.TestCase):
    '''
    This is a test class to test CompanyShareAnalyzer class
    '''
    def setUp(self):
        print "Inside the Test case BEGIN "
        shareAnalyzer = CompanyShareAnalyzer("shareData.csv")
        self.result=shareAnalyzer.getResultSharePriceAnalysis()
        print "Inside the Test case END"
    def test_share_value(self):
        '''   Company 9 max price is 100      '''
        self.assertEquals(100, self.result[8].value)
    def test_share_month(self):
        '''   Company 1 max price month july  '''
        self.assertEquals('jul', self.result[0].month)
    def test_share_year(self):
        '''   Company 7 max price year is 1990  '''
        self.assertEquals(1990, self.result[6].year)
if __name__ == '__main__':
    unittest.main()
