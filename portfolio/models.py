from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True, max_length=200)

    from django.db import models

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
   
    def __str__(self):
     return 'Message from '+ self.name
    
