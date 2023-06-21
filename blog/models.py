
from django.db import models
from accounts.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Blogpost(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    content = models.TextField()
    blogImage = models.ImageField(upload_to="blogimg",null=True)
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)

        super(Blogpost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title +" by "+ self.author.first_name
    