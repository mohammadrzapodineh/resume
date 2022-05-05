from django.db import models
from ckeditor.fields import RichTextField


class WorkHistory(models.Model):
    title = models.CharField(verbose_name="عنوان نمونه کار", max_length=120)
    company = models.CharField(max_length=120, verbose_name="شرکت")
    description = RichTextField(verbose_name="توضیحات سابقه کار")
    date = models.CharField(verbose_name="سال کار شما از سال ؟ تا سال؟", max_length=120)

    class Meta:
        verbose_name = 'سابقه کار'
        verbose_name_plural = 'سابقه کار ها '

    def __str__(self):
        return f"سابقه کار - {self.title}"


class EducationHistory(models.Model):
    title = models.CharField(verbose_name="عنوان تحصيلات", max_length=120)
    field_of_study = models.CharField(max_length=120, verbose_name="رشته تحصيلي")
    description = RichTextField(verbose_name="توضیحات تحصيلات")
    date = models.CharField(verbose_name="سال کار شما از سال ؟ تا سال؟", max_length=120)

    class Meta:
        verbose_name = 'سابقه تحصيل'
        verbose_name_plural = 'سابقه تحصيلات '

    def __str__(self):
        return f"سابقه تحصيل - {self.title}"


class Skill(models.Model):
    title = models.CharField(verbose_name='عنوان مهارت', max_length=120)
    percent = models.IntegerField(default=0, verbose_name='درصد فراگیری مهارت ')
    is_circle = models.BooleanField(verbose_name='کامپوننت آن دایره ای باشد؟', default=False)

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return f'مهارت:{self.title}'


class Portfolio(models.Model):
    title = models.CharField(verbose_name='عنوان نمونه کار', max_length=120)
    image = models.ImageField(verbose_name='تصویر نمونه کار', upload_to='images/portfolio/')
    link = models.URLField(verbose_name='لینک وبسایت', blank=True, null=True)

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کار ها'

    def __str__(self):
        return f"نمونه کار{self.title}"