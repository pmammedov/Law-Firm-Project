from django.db import models
from django.db.models.fields import related
from django.urls import reverse

from account.models import User

class Article(models.Model):
    image  = models.ImageField( upload_to='post/image/',default="image.jpg" )
    title  = models.CharField( max_length=9000,default=None )
    body   = models.TextField( default=None,verbose_name="content",blank = True )
    author = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="author" )
    stamp  = models.DateField( auto_now_add=True )
    updated   = models.DateField( auto_now=True )
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('blog:post-details')

    def snip(self):
        return f'{self.body}'[:180]
    class Meta: 
        ordering = ('-stamp',) 


class Comment(models.Model): 
    post = models.ForeignKey(Article,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name    = models.CharField(max_length=80) 
    email   = models.EmailField() 
    body    = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active  = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('-created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 