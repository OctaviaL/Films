from django.db import models

class Film(models.Model):

    GENRE_CHOICES = (
        ('comedy', 'Комедия'),
        ('drama', 'Драма'),
        ('horror', 'Ужасы'),
    )

    title = models.CharField(max_length=50)
    genre = models.CharField(choices=GENRE_CHOICES)
    year = models.IntegerField()
    description = models.TextField('Описание поста')
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='films'
    )
    tags = models.ManyToManyField('Tag')

    def __str__(self) -> str:
        return f'{self.title}'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)

    def __str__(self) -> str:
        return f'{self.title}'

class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='images')
