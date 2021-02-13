from django.db import models

# Create your models here.
class Item(models.Model):

    #item_name vai ser um field de chars com tamanho máximo de 512 caracteres
    item_name = models.CharField(max_length=512, verbose_name="name")

    #item_price vai ser um float
    item_price = models.FloatField(verbose_name="price")

    #verbose é opcional, apenas mexe com a maneira como estes fields são mostrados no Django Admin.


    #Esta função __str__ simplesmente define como o item vai ser mostrado no Django Admin.
    def __str__(self):
        return self.item_name