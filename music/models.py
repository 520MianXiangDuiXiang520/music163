from django.db import models

# Create your models here.
# Create your models here.
class 华语男歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 华语女歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 华语组合(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 欧美男歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 欧美女歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 欧美组合(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 日本男歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 日本女歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 日本组合(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 韩国男歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 韩国女歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 韩国组合(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 其他男歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 其他女歌手(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名

class 其他歌手组合(models.Model):
    歌手姓名=models.CharField(max_length=100)
    歌手ID=models.CharField(max_length=100)

    def __str__(self):
        return self.歌手姓名