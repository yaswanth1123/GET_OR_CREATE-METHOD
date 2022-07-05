from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    player_name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.player_name

class Access_Records(models.Model):
    player_name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()


