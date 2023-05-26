from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    verbose_name = 'account_customuser'
    label = 'account'

    def ready(self):
        import account.signals # noqa

