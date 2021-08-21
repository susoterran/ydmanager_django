import os
from django.db import models
from django.urls import reverse

from django.conf import settings
from taggit.managers import TaggableManager

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
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('label:label_detail', args=(self.id,))

    ### label/fields.py 안의 ThumbnailImageFieldFile 클래스의 delete 메소드가 정상 동작안해서 모델에 추가
    def delete(self):
        os.remove(str(settings.BASE_DIR)+str(self.image.url))
        os.remove(str(settings.BASE_DIR)+str(self.image.thumb_url))
        super().delete()

