from django.db import models
import datetime

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData, func):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 2:
            errors["len_title"] = "Show title should be at least 2 characters"
        
        if func == 'new':
            all_shows = Show.objects.all()
            for show_title in all_shows:
                if postData['title'] == show_title.title:
                    errors["len_network"] = "Show title must be unique."

        if len(postData['network']) < 3:
            errors["len_network"] = "Show network should be at least 3 characters"

        format =  "%Y-%m-%d"
        if datetime.datetime.strptime(postData['release_date'], format) > datetime.datetime.now():
            errors["len_network"] = "Release Date should be in the past."

        if ((len(postData['description']) != 0) and (len(postData['description']) < 10)):
            errors["len_description"] = "Show description should be at least 10 characters"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=False)
    description = models.TextField(blank=True, null = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 

    def __str__(self):
        return f'{self.title} ({self.network})'

    def __repr__(self) -> str:
        return f'{self.title} ({self.network})'

