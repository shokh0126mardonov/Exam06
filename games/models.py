from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self): 
        return self.title
    
    def to_dict(self):
        return {
        'id':self.pk,
        'title' : self.title,
        'location': self.location,
        'start_date' : self.start_date,
        'description' : self.description,
        'created_at' : self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }