from django.db import models

# Create your models here.
class UsersModel(models.Model):
    name=models.CharField(max_length=255, verbose_name='имя')
    created_at=models.DateTimeField(auto_now_add=True)
    age=models.CharField(verbose_name='возраст',max_length=255)
    email=models.EmailField(verbose_name='имэил')
    phone=models.CharField(verbose_name='возраст',max_length=255)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'UserModel'
        verbose_name_plural = 'UserModels'

class TaskModel(models.Model):
    user=models.ForeignKey(UsersModel,on_delete=models.CASCADE,related_name='tasks')
    title=models.CharField(max_length=255, verbose_name='заголовок')
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(verbose_name='статус')
    image=models.ImageField(upload_to='media/',null=True)
    description=models.TextField(verbose_name='описание')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'TaskModel'
        verbose_name_plural = 'TaskModels'