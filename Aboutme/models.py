from django.db import models
from ckeditor.fields import RichTextField


class AboutMe(models.Model):
    avatar = models.ImageField(verbose_name='آواتار', upload_to='avatar/')
    name = models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')
    location = models.CharField(max_length=120, verbose_name="محل سکونت")
    biography = RichTextField(verbose_name='بیوگرافی')
    success_projects = models.IntegerField(verbose_name='تعداد پروژه های موفق', default=0)
    work_experience = models.IntegerField(verbose_name='سابقه کار', default=0)
    page_title = models.CharField(max_length=60, verbose_name='عنوان ضفحه در مرورگر', blank=True, null=True)
    meta_description = models.CharField(max_length=160, verbose_name='توضیحات تگ متا برای سئو', blank=True, null=True)
    meta_keywords = models.CharField(max_length=400, verbose_name='کلمات کلیدی تگ متا برای سئو', blank=True, null=True)

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره های من'

    def __str__(self):
        return f"درباره ی "


class SocialMedia(models.Model):
    title = models.CharField(verbose_name='عنوان لینک ', max_length=50)
    link = models.URLField(verbose_name='لینک ')
    icons = (
        ('facebook-f', 'آیکون فیسبوک'),
        ('instagram', 'آیکون اینستاگرام'),
        ('twitter', 'آیکون توییتر'),
        ('telegram', 'آیکون تلگرام'),
    )
    icon = models.CharField(max_length=20, verbose_name='آیکون', choices=icons)

    class Meta:
        ordering = ('title',)
        verbose_name = 'لینک شبکه اجتماعی'
        verbose_name_plural = 'لینک های شبکه های اجتماعی'

    def __str__(self):
        return f"{self.title}"
