from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(verbose_name='优惠码', max_length=50)
    valid_from = models.DateTimeField(verbose_name='起始日期')
    valid_to = models.DateTimeField(verbose_name='截止日期')
    discount = models.IntegerField(verbose_name='优惠额度', validators=[MinValueValidator, MaxValueValidator])
    active = models.BooleanField(verbose_name='是否有效')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '优惠券'
        verbose_name_plural = verbose_name
