from django.db import models

# Create your models here.

class Survey(models.Model):
    """A weekly survey for TUAS staff"""
    survey_id = models.BigAutoField(primary_key=True)       #auto matically creats an id for a survey, it is the primary key
    survey_title = models.CharField(max_length=200)         #just a text that says 'Survey'
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)       #not too sure because the date it was created might not be the same as the date it will be uploaded
   
    # def __str__(self):
    #      """Return a string representation of the model."""
    #      return self.survey_id


class Question(models.Model):
    """A question posed in a weekly survey"""
    question_id = models.BigAutoField(primary_key=True) 
    question_text = models.CharField(max_length=700)
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
         """Return a string representation of the model."""
         return self.question_text

class Option(models.Model):
    """The various options given per quesitons"""
    option_id = models.BigAutoField(primary_key=True) 
    option_text = models.CharField(max_length=150)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
         """Return a string representation of the model."""
         return self.option_text


class Result(models.Model):
    """The results of a survey"""
    result_id = models.BigAutoField(primary_key=True) 
    survey_id = models.ForeignKey(Survey, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
         """Return a string representation of the model."""
         return self.result_id

class Admin(models.Model):
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

class UserAnswer(models.Model):
    """the option that the user taking hte survey chooses"""
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staff, self.survey_id, self.date_taken