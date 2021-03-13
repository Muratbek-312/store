from django.test import TestCase

# Create your tests here.
# from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
#
#
#
#
# #TODO: CartProduct
# class CartProduct(models.Model):
#
#     user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
#     cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     qty = models.PositiveIntegerField(default=1)
#     final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
#
#     def __str__(self):
#         return "Продукт: {} (для корзины)".format(self.content_object.title)
#
#     def save(self, *args, **kwargs):
#         self.final_price = self.qty * self.content_object.price
#         super().save(*args, **kwargs)
#
#
# #TODO: Cart
# class Cart(models.Model):
#
#     owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
#     products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
#     total_products = models.PositiveIntegerField(default=0)
#     final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
#     in_order = models.BooleanField(default=False)
#     for_anonymous_user = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.id)