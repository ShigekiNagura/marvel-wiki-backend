from django.db import models

class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    published_at = models.DateField(blank=True, null=True)
    characters = models.ManyToManyField("Character")
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    
    class Meta:
        db_table = "movie"