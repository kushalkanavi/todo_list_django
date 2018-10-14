from django.db import models

class task(models.Model):

    Title    	= models.CharField(max_length=120, null=True)
    Description = models.CharField(max_length=4800, null=True)
    Due_Date  	= models.DateField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.Title

class subtask(models.Model):

    Title    	= models.CharField(max_length=120, null=True)
    Description = models.CharField(max_length=4800, null=True)
    Due_Date  	= models.DateField(auto_now=False, auto_now_add=False, null=True)
    task 		= models.ForeignKey(task, on_delete=models.CASCADE, to_field='id', null=True)

    def __str__(self):
        return self.Title