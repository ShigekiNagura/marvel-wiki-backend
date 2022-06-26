from django.db import models

class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    published_at = models.DateField(blank=True, null=True)
    characters = models.ManyToManyField("Character")
    
    class Meta:
        db_table = "movie"