import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question='What language did u first learn to speak? ' 
        self.my_survey=AnonymousSurvey(question)
        self.my_survey.store_response(question)
        self.responses=['English','Spanish','German']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    
    def test_store_three_response(self):
        for res in self.responses:
            self.my_survey.store_response(res)
        for res in self.responses:
            self.assertIn(res, self.my_survey.response)
                                                                                                                            
if __name__=='__main__':
    unittest.main()

