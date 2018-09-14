from django.db import models

# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=32)


class User(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    ut = models.ForeignKey(to='UserType', to_field='id', related_query_name='a')


# v = User.objects.all()
# for item in v:
#     item.user
#     item.pwd
#     item.ut.name

User.objects.all().values('user', 'ut__name') # 跨表取name

v = UserType.objects.all()
for item in v:
    item.name
    item.id
    item.user_set.all() # 当前用户类型对应所有的用户，一条或者多条


    当foreignkey中related_query_name='xxx'

    正向查找
    user_set 替换成 xxx
    item.xxx.all()
    反向查找
    models.UserType.objects.all().values('name','user__pwd') # 通过反向user表查找pwd字段
    当有related_query_name='xxx'时
    models.UserType.objects.all().values('name','xxx__pwd')

    总结, ut = models.ForeignKey(to='UserType', to_field='id', related_query_name='xxx')
    related_query_name='xxx'参数存在时
    正向查找中 user_set 替换成 'xxx'
    反向查找中 反向查找表名,替换成  'xxx'

