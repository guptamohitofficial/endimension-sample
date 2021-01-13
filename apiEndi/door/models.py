from django.contrib.auth.models import User
from django.db import models

# Creating a public chatting group
class Chat(models.Model):
    fromUser = models.ForeignKey(User, verbose_name=("Sent By"), on_delete=models.CASCADE) 
    # toUser = models.ForeignKey(User, verbose_name=("Send to"), on_delete=models.CASCADE) 
    message = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

