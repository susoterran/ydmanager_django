from django.db import models
from django.urls import reverse

from actor.fields import ThumbnailImageField

class Actor(models.Model):
    name = models.CharField('NAME', max_length=100, null=False)
    name_eng = models.CharField('NAME_ENG', max_length=100, blank=True, null=True)
    name_jpn = models.CharField('NAME_JPN', max_length=100, blank=True, null=True, )
    info = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    image = ThumbnailImageField(upload_to='actor', default='actor/no_image.jpg')
   
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor:actor_detail', args=(self.id,))