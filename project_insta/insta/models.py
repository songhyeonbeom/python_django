from django.db import models
from django.urls import reverse
from insta.fields import ThumbnailImageField
from common.models import User



class Album(models.Model):
    #id 프라이머리키
    objects = None
    name = models.CharField('NAME', max_length=30)
    slug = models.SlugField(max_length=250, unique=True)
    owner = models.ForeignKey('common.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('insta:album_detail', args = [self.slug])

    def __str__(self) :
        return '{}'.format(self.name)


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = ThumbnailImageField('IMAGE', upload_to='insta/%Y/%m')
    description = models.TextField('Photo Description', blank=True)

    title = models.CharField('TITLE', max_length=30, null=True)
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)

    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='owner_photo')
    voter = models.ManyToManyField(User, related_name='voter_photo')
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return '{}'.format(self.image.name)

    def get_absolute_url(self):
        return reverse('insta:photo_detail', args = [self.id])


class Answer(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner_answer')
    voter = models.ManyToManyField(User, related_name='voter_answer')










