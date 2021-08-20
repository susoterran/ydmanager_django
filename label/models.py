from django.db import models
from django.urls import reverse

from label.fields import ThumbnailImageField

class Label(models.Model):
    number = models.CharField('품번', max_length=100, null=False)
    category_choice = (
        ('일반', '일반'),
        ('FC2', 'FC2'),
        ('아마추어', '아마추어'),
        ('노모', '노모'),
    )
    category = models.CharField('카테고리', max_length=100, choices=category_choice)
    info = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    image = ThumbnailImageField(upload_to='label')

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('label:label_detail', args=(self.id,))
