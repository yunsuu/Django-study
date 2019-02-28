from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comments(models.Model):
    #blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    date = models.DateTimeField('date published',null=True)
    
    def __str__(self):
        return self.text
