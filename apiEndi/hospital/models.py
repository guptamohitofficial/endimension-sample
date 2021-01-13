from django.db import models
from django.contrib.auth.models import User
from django.utils.timesince import timesince


class Record(models.Model):
    hospital = models.ForeignKey(User, related_name='from_hospital', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='to_doctor', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True, null=True)
    image = models.FileField(upload_to="")
    status = models.CharField(max_length=50,null=True)

    def getTime(self):
        try:
            return timesince(self.time)+" ago"
        except:
            return ""


class Report(models.Model):
    patient = models.ForeignKey(Record, verbose_name=("record_report"), on_delete=models.CASCADE)
    report = models.TextField(null=True)







