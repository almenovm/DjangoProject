from django.apps import AppConfig


class ReviewConfig(AppConfig):
    name = 'review'
    def ready(self):
        import commercial.signals