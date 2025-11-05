import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question='What language did u first learn to speak? ' 
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.response)

    def test_store_three_response(self):
        question='What language did u first learn to speak? ' 
        my_survey=AnonymousSurvey(question)
        responses=['English','Spanish','German']
        for res in responses:
            my_survey.store_response(responses)
        for res in responses:
            self.assertIn(responses, my_survey.response)

#if __name__=='__main__':
#    unittest.main()

