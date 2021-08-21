from django.db import models
from django.urls import reverse

class Company(models.Model):
    name = models.CharField('회사명', max_length=50, null=False)
    url = models.CharField('URL', max_length=100, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company:company_detail', args=(self.id,))