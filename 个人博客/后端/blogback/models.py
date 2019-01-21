from django.db import models


# Create your models here.
class User(models.Model):
    """ 用户表"""
    username = models.CharField(max_length=20, unique=True, blank=True, verbose_name="姓名")
    password = models.CharField(max_length=255, verbose_name="密码")

    class Meta:
        db_table = 'f_user'


class Category(models.Model):
    """栏目表"""
    cate_name = models.CharField(max_length=20, unique=True, verbose_name="栏目名称")
    cate_alias = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="栏目别名")
    cate_keywords = models.CharField(max_length=10, unique=True, verbose_name='关键字')
    cate_describe = models.CharField(max_length=255, unique=True, verbose_name='描述')
    cate_fid = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父节点")

    class Meta:
        db_table = 'f_category'


class Article(models.Model):
    """文章表"""
    art_title = models.CharField(max_length=20, unique=True, verbose_name="文章标题")
    art_content = models.TextField(verbose_name="文章内容")
    art_keywords = models.CharField(max_length=20, unique=True, verbose_name="关键字")
    art_describe = models.CharField(max_length=255, unique=True, verbose_name="描述")
    art_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    art_cid = models.ForeignKey(Category, null=True, on_delete=models.PROTECT, verbose_name="栏目")

    class Meta:
        db_table = 'f_article'
