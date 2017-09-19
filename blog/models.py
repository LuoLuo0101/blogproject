from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name="标题",max_length=70)
    body = models.TextField(verbose_name="正文")
    create_time = models.DateTimeField(verbose_name="发布时间",auto_created=True)
    modified_time = models.DateTimeField(verbose_name="修改时间")
    category = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tags")

    class Meta:
        verbose_name = verbose_name_plural = "文章表"


class Category(models.Model):
    name = models.CharField(verbose_name="分类名",max_length=50)

    class Meta:
        verbose_name = verbose_name_plural = "文章分类表"


class Tags(models.Model):
    name = models.CharField(verbose_name="标签分类名",max_length=50)

    class Meta:
        verbose_name = verbose_name_plural = "标签分类表"
