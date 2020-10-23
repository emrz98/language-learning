from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, blank=True) 
    age = models.IntegerField()

    def __str__(self):
        return self.name

class FlashCard(models.Model):
    anverse = models.CharField(max_length=50)
    reverse = models.CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.anverse + " - " + self.reverse
