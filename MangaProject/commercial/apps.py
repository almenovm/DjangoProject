from django.apps import AppConfig


class CommercialConfig(AppConfig):
    name = 'commercial'

    def ready(self):
        import commercial.signals