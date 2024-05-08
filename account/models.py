from __future__ import unicode_literals
# import datetime
from django.utils import timezone
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    # username 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(verbose_name='email address', unique=True)
    # email_confirmed = models.BooleanField(verbose_name='Email Confirmed', default=False)
    first_name = models.CharField(
        verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    dob = models.DateField(auto_now=True, blank=True)
    nrc = models.CharField(verbose_name='national registration number', max_length=300, blank=True)
    country = CountryField(blank_label='(select country)', blank=True)
    phone =  PhoneNumberField(blank=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    location = models.CharField(verbose_name='location', max_length=50, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_verified = models.BooleanField(verbose_name='verified', default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        print(subject, message, from_email,)
        # send_mail(subject, message, from_email, [self.email], **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse('account:edit', args=[self.pk])

class LawyerType(models.Model):
    name        = models.CharField( max_length=50)    
    updated     = models.DateField( auto_now=True )
    timestamp   = models.DateField( auto_now_add=True )
    slug        = models.SlugField( default=None )

    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'

class Lawywer(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    certification   = models.FileField(upload_to='lawyers/certificates/', max_length=100)
    experience      = models.IntegerField(default=0,verbose_name="years of experience")
    # cat             = models.ForeignKey(LawyerType, verbose_name="Category",related_name="category", on_delete=models.CASCADE)
    organisation    = models.CharField(max_length=50)
    fee             = models.DecimalField(max_digits=5, decimal_places=2,default=1.00)
    slug            = models.SlugField( default=None )
    updated         = models.DateField( auto_now=True )
    timestamp       = models.DateField( auto_now_add=True )
    # wins   
    
     
    def __str__(self):
        return f'{self.user}'

    def __unicode__(self):
        return f'{self.user}'
    
    def get_absolute_url(self):
        return reverse("account:lawyer-details", kwargs={"slug": self.slug})
    
    def get_rating(self):
        return 4.9    

    def get_wins(self):
        return 43 

class Apointment(models.Model):
    subject         = models.CharField( max_length=50)
    client          = models.ForeignKey(User, related_name="client", on_delete=models.CASCADE)
    lawyer          = models.ForeignKey(Lawywer, related_name="lawyer", on_delete=models.CASCADE)
    startTime       = models.DateTimeField(auto_now=False, auto_now_add=False)
    endtTime        = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated         = models.DateField( auto_now=True )
    timestamp       = models.DateField( auto_now_add=True )
     

    def __str__(self):
        return f'{self.subject}'

    def __unicode__(self):
        return f'{self.subject}'
    
    def get_meeting_deration(self):
        dur = self.endtTime - self.startTime
        return  dur
    
    def get_status(self):
        current_time =  timezone.now() 
        if current_time > self.startTime and current_time < self.endtTime:
            return 'Progress' 
        if current_time > self.startTime and current_time > self.endtTime:
            return 'Completed'
        if current_time < self.startTime and current_time < self.endtTime:
            return 'Pending'
        return 'Waiting'

class Rating(models.Model):
    lwyr          = models.ForeignKey(Lawywer, verbose_name="lawyer", related_name="lwyr", on_delete=models.CASCADE)
    usr          = models.ForeignKey(User,verbose_name="client",related_name="usr", on_delete=models.CASCADE)
    rate            = models.IntegerField(default=0)
    updated         = models.DateField( auto_now=True )
    timestamp       = models.DateField( auto_now_add=True )
  
    def __str__(self):
        return f'{self.usr} rating {self.lwyr}'

    def __unicode__(self):
        return f'{self.usr} rating {self.lwyr}'
