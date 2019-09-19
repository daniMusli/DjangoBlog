from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class post(models.Model):
    user = models.ForeignKey('auth.User',verbose_name = 'yazr')
    title = models.CharField(max_length=120)
    content= RichTextField()
    date = models.DateTimeField( auto_now_add = True )
    image = models.FileField(null=True,blank=True)
    slug = models.SlugField(unique=True,max_length=130,editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       # return "/poss/{}".format(self.id)
        return reverse('post:detail', kwargs={'postsSlug' : self.slug})

    def get_craete_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'postsSlug' : self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'postsSlug' : self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('i','i'))
        unique_slug = slug
        counter = 1
        while post.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
            counter += 1
        return unique_slug

    def save(self,*args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(post,self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date']


class comment(models.Model):
    yorum = models.ForeignKey('postApp.post',on_delete = models.CASCADE,related_name='comments')

    name = models.CharField(max_length=200,verbose_name= 'isim')
    content = models.TextField(verbose_name = 'yorum')

    created_date = models.DateTimeField(auto_now_add=True)
