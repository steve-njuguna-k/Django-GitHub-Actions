from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=500, verbose_name='Post Title', null=False)
    content = models.TextField(verbose_name='Post Content', null=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Posts'