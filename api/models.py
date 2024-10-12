from django.db import models

# Create your models here.

class TodoModel(models.Model):
    todo_title = models.CharField(max_length=255)
    todo_description = models.CharField(max_length=255)

    def __str__(self):
        return self.todo_title
    
    
