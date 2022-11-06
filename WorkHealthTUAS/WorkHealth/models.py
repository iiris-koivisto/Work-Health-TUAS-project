from django.db import models

# Create your models here.

class Survey(models.Model):
    """A weekly survey for TUAS staff"""
    survey_id = models.BigAutoField(primary_key=True)       #auto matically creats an id for a survey, it is the primary key
    number_questions = models.TextChoices("one","two","three")      #creates a select box that allows admin to choose an option
    number_answers = models.IntegerField()      #potentially change to 'answer_type' and allows text answers
    upload_date = models.DateTimeField(auto_now_add=True)       #not too sure because the date it was created might not be the same as the date it will be uploaded
    #questions = models.ForeignKey(Question, on_delete=models.SET_NULL)     #creating an association between class survey and class Question, idk how it works if there are multiple questions
    def __str__(self):
         """Return a string representation of the model."""
         return self.survey_id

class Question(models.Model):
    """A question posed in a weekly survey"""
    question_id = models.BigAutoField(primary_key=True) 
    question = models.CharField(max_length=700)
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
         """Return a string representation of the model."""
         return self.question

class Options(models.Model):
    """The various options given per quesitons"""
    option_id = models.BigAutoField(primary_key=True) 
    option = models.CharField(max_length=150)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
         """Return a string representation of the model."""
         return self.option

class Result(models.Model):
    """The results of a survey"""
    result_id = models.BigAutoField(primary_key=True) 
    survey_id = models.ForeignKey(Survey, on_delete=models.PROTECT)

    def __str__(self):
         """Return a string representation of the model."""
         return self.result_id

class Admins(models.Model):
    """The admins who create the survey"""
    admin_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)

    def __str__(self):
         """Return a string representation of the model."""
         return self.username

class Staff(models.Model):
    """The staffs who answer the survey"""
    staff_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)

    def __str__(self):
         """Return a string representation of the model."""
         return self.username