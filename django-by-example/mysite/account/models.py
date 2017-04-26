from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    date_of_brith = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)




class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)



# monkey-patch,动态的为User添加代码，需求始于需要给User添加一个ManyToMany关系字段。
User.add_to_class('following',
                models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
