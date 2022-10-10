from django.db import models


class Account(models.Model):
    '''账户表'''
    username = models.CharField(max_length=64, unique=True)  #unique=True 唯一索引
    email = models.EmailField()
    password = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)
    signature = models.CharField('签名', max_length=64,
                                 null=True)  #签名 注释 null=True 可控


class Article(models.Model):
    '''文章表'''
    title = models.CharField(max_length=255)  #字符串
    content = models.TextField()  #长文本
    account = models.ForeignKey(
        'Account', on_delete=models.CASCADE, default=""
    )  #'Account' 外键关键表'Account' on_delete=models.CASCADE外键删除时的操作 default="" 默认值
    tags = models.ManyToManyField('Tag')  # 多对多
    pub_date = models.DateField()  #日期


class Tag(models.Model):
    '''标签表'''
    name = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField(auto_now_add=True)  #日期自动填写当前时间


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


# 新建一个对象的方法有以下几种：
Person.objects.create(name=name, age=age)
p = Person(name="WZ", age=23)
p.save()
p = Person(name="TWZ")
p.age = 23
p.save()
Person.objects.get_or_create(name="WZT", age=23)
# 这种方法是防止重复很好的方法，但是速度要相对慢些，返回一个元组，第一个为Person对象，第二个为True或False, 新建时返回的是True, 已经存在时返回False.













