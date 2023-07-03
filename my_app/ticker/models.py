from django.db import models

class Ticker(models.Model):
    message=models.TextField()
    time_create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
