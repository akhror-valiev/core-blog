from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #OneToOneField means relationship exsting User model,  #CASCADE means if user delete profile it will also delete from darabase.
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')     
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)                                                       
       
       
    def __str__(self): #dunder method
        return f'{self.user.username} Profile'        


    #def save(self, *args, **kwargs):
        #super(Profile, self).save(*args, **kwargs)  
        
        #img = Image.open(self.image.path)
        #if img.height > 300 or img.width > 300:
            #output_size = (300,300)  
            #img.thumbnail(output_size)   
            #img.save(self.image.path)                                          

