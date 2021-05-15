from django.apps import AppConfig


class ShopCartConfig(AppConfig):
    name = 'shop_cart'

    def ready(self):
        import shop_cart.signals