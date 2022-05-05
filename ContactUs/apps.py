from django.apps import AppConfig


class ContactusConfig(AppConfig):
    name = 'ContactUs'
    verbose_name = 'تماس با ما '

    def ready(self):
        from . import signals