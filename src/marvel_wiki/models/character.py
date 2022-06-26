from django.db import models

class Character(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    
    class Meta:
        db_table = "character"