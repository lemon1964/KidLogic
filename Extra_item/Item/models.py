from django.db import models
from django.urls import reverse


class Grup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False, db_index=True, default='')

    def __str__(self):
        return f'{self.name}'

    def get_url(self):
        return reverse('one_grup', args=[self.slug])


class Objec(models.Model):
    name = models.CharField(max_length=40)
    picture = models.CharField(max_length=40)
    sound = models.CharField(max_length=40)
    ident = models.BooleanField(default=True)
    grup = models.ForeignKey(Grup, on_delete=models.CASCADE, null=True, related_name='objecs')

    def __str__(self):
        return f'{self.name} - {self.ident}'

