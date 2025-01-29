from django.db import models

# Create your models here.
class Home(models.Model):
    email = models.EmailField()
    current_datetime = models.DateTimeField(auto_now_add=True)
    github_url = models.CharField(max_length=150)


    def __str__(self):
        return self.email + "  " + self.github_url