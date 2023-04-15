from django.db import models

class Film(models.Model):

    title = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField('Описание поста')
    image = models.ImageField(upload_to='films/')
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='films'
    )

    def __str__(self) -> str:
        return f'{self.title}'
    

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)

    def __str__(self) -> str:
        return f'{self.title}'
