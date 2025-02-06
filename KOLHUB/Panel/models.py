from django.db import models

class Pages(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField()
    user = models.CharField(max_length=20)
    
    def __str__(self):
        return self.id
