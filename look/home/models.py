# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# from mptt.models import MPTTModel, TreeForeignKey


class Districts(models.Model):
    '''Районы'''
    image = models.ImageField(upload_to='districts/')
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    places_nearbly = models.TextField(null=True)
    url = models.SlugField(unique=True)
    metro = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

class DistrictsNews(models.Model):
    title = models.CharField(max_length=100)
    anons = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='districts_news/', null=True, blank=True)
    date = models.DateField(null=True)
    districts = models.ForeignKey('Districts',
                                  verbose_name='Район',
                                  on_delete=models.CASCADE,
                                  null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Apartment(models.Model):
    apart_name = models.CharField(max_length=50, null=True)
    apart_image = models.ImageField(upload_to='districts_apart/', null=True)
    apart_price = models.CharField(max_length=50, null=True)
    districts = models.ForeignKey('Districts',
                                  verbose_name='Район',
                                  on_delete=models.CASCADE,
                                  null=True)

    def __str__(self):
        return self.apart_name

    class Meta:
        verbose_name = 'Планировка'
        verbose_name_plural = 'Планировки'

class DistrictsImage(models.Model):
    '''Фотографии районов'''
    name = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', upload_to='districts_image/')
    description = models.TextField('Описание', null=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    districts = models.ForeignKey('Districts',
                                  verbose_name='Район',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотографии района'
        verbose_name_plural = 'Фотографии района'


class Category(models.Model):
    '''Категории'''
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Reviews(models.Model):
    '''Отзывы'''
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    date = models.DateField('Дата', null=True)
    # parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    districts = models.ForeignKey('Districts',
                                  verbose_name='район',
                                  on_delete=models.CASCADE,
                                  null=True)

    def __str__(self):
        return f'{self.name} - {self.districts}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'