from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Score(models.Model):
    math_score=models.PositiveIntegerField()
    eng_score=models.PositiveIntegerField()
    sci_score=models.PositiveIntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return 'maths', self.math_score,'english', self.eng_score, 'science', self.sci_score



