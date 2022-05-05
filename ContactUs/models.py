from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ContactUs(models.Model):
    name = models.CharField(max_length=110, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل کاربر ')
    text = models.TextField(verbose_name='متن پیام ')
    date = models.DateTimeField(auto_now=True, verbose_name='تاریخ')
    is_observed = models.BooleanField(default=False, verbose_name='مشاهده شده است ؟')
    is_answered = models.BooleanField(default=False, verbose_name='پاسخ داده شده است ؟')
    answer = RichTextUploadingField(verbose_name='متن پاسخ', blank=True, null=True)

    class Meta:
        verbose_name = 'پیام کاربر'
        verbose_name_plural = 'پیام های کاربران '

    def __str__(self):
        return f'پیام از طرف {self.name}- {self.email}'

