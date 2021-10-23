import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class PedigreePerson(models.Model):
    pub_date = models.DateTimeField('Date Entered')
    person_choice = models.CharField(
        max_length = 200
        , choices = (
            ('0', "Grandmother on Parent #1 Side")
            , ('1', "Grandfather on Parent #1 Side")
            , ('3', "Sibling of Parent 1")
            , ('4', "Sibling 2 of Parent 1")
            , ('5', "Parent 1")
            , ('2', "Parent 2")
            , ('6', "Child of Parent 1 & Parent 2")
            , ('7', "Child 2 of Parent 1 & Parent 2")
            , ('8', "Child 3 of Parent 1 & Parent 2") )
        , default = '0'  )

    def __str__(self):
        return self.person_choice

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class PersonInput(models.Model):
    person = models.ForeignKey(PedigreePerson, on_delete=models.CASCADE)

    max_age = 110
    AGE_CHOICES = [tuple([x, x]) for x in range(1, 110)]

    MULTIPLE_OPTIONS = (
        (0, "Known and Undiagnosed"),
        (1, "Known and Confirmed Diagnosis"),
        (9, "Unkown")
    )

    patient_age = models.IntegerField(default = 0)
    patient_sex = models.CharField(
        max_length = 200,
        choices = (
            (0, "Male")
            , (1, "Female") )
        , default = 0 )

    patient_dna_dx = models.CharField(
        max_length = 200,
        choices = MULTIPLE_OPTIONS,
        default = 0)

    patient_ldlc = models.IntegerField(default = 0)

    patient_totc = models.IntegerField(default = 0)

    patient_tx = models.CharField(
        max_length = 200,
        choices = MULTIPLE_OPTIONS,
        default = 0 )

    patient_clincad_status = models.CharField(
        max_length = 200,
        choices = MULTIPLE_OPTIONS,
        default = 0 )

    patient_clincad_age = models.IntegerField(default = 0)

    def __str__(self):
        return self.person