from django.test import TestCase
from .models import Survey, Question, Admin, UserAnswer, Option, Result, Staff

# Create your tests here.

class TestSurvey(TestCase):
    def setUp(self):
        test_survey = Survey.objects.create(survey_title = "Survey")
        test_question = Question.objects.create(survey_id = test_survey, question_text = 'Are you feeling well?')
        test_option = Option.objects.create(question_id = test_question, option_text = "Yes")
        test_option2 = Option.objects.create(question_id = test_question, option_text = "No")
        test_result = Result.objects.create(survey_id = test_survey)
        test_admin = Admin.objects.create(username = "Maria")
        test_staff = Staff.objects.create(username = "Miri")
        UserAnswer.objects.create(staff = test_staff, survey_id = test_survey, option = test_option, result = test_result)

    def test_survey(self):
        test_survey = Survey.objects.create(survey_title = "Survey")
        test_question = Question.objects.create(survey_id = test_survey, question_text = 'Are you feeling well?')
        test_option = Option.objects.create(question_id = test_question, option_text = "Yes")
        test_option2 = Option.objects.create(question_id = test_question, option_text = "No")
        test_result = Result.objects.create(survey_id = test_survey)
        test_admin = Admin.objects.create(username = "Maria")
        test_staff = Staff.objects.create(username = "Miri")
        test_answer = UserAnswer.objects.create(staff = test_staff, survey_id = test_survey, option = test_option, result = test_result)
        self.assertEqual(str(test_question), 'Are you feeling well?')
        self.assertEqual(str(test_option), 'Yes')
        self.assertEqual(str(test_option2), 'No')
        self.assertEqual(test_question.survey_id, test_survey)
        self.assertEqual(test_option2.question_id, test_question)
        # self.assertEqual(str(test_result), 'hello')
        self.assertEqual(test_result.result_id, 2)
        self.assertEqual(test_result.survey_id, test_survey)
        self.assertEqual(test_result.is_complete, False)
        self.assertEqual(str(test_admin), 'Maria')
        self.assertEqual(str(test_staff), 'Miri')
        # self.assertEqual(str(test_answer), 'test')

