from django.db import models


# Create your models here.

class Main_page(models.Model):
    title = models.CharField(max_length=150, null=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.content # отображает на сайте текст базы данных

    def get_absolute_url(self):
        return reverse('index_page', kwargs={'index_page_id': self.pk})