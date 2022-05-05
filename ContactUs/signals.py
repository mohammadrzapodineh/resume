from django.db.models.signals import pre_save
from .models import ContactUs
from django.dispatch import receiver
from Resume.utils import EmailThread
from django.template.loader import get_template


@receiver(signal=pre_save, sender=ContactUs)
def send_answer(sender, instance, **kwargs):
    if instance.is_answered and instance.answer:
        template = get_template('ContactUs/email_replay_component.html').render({'name': instance.name, 'answer': instance.answer})
        EmailThread('پاسخ به تماس شما در وبسایت شخصی محمد رضا پودینه تنیده ', template, recipient_list=[instance.email]).start()




