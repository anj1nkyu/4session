from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    introduce = models.TextField() 
    content = models.TextField()
    category = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    

    

    def __str__(self):
        return self.title