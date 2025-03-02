from django.db import models

NULLABLE = {"null": True, "blank": True}


class Product(models.Model):
    """Продукты"""

    title = models.CharField(max_length=150, verbose_name="название")
    model = models.CharField(max_length=150, verbose_name="модель", **NULLABLE)
    release_date = models.DateField(verbose_name="дата выхода", **NULLABLE)

    def __str__(self):
        return f"{self.title} {self.model}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"



class TradeNode(models.Model):
    """Звено сети"""
    name = models.CharField(max_length=255,verbose_name="название")
    email = models.EmailField(**NULLABLE)
    country = models.CharField(max_length=100,default="Россия",verbose_name="страна")
    city = models.CharField(max_length=100, **NULLABLE,verbose_name="город")
    street = models.CharField(max_length=100, **NULLABLE,verbose_name="улица")
    house_number = models.CharField(max_length=10, **NULLABLE,verbose_name="номер дома")
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name="suppliers",verbose_name="поставщик")
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,verbose_name="задолженность")
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Product', blank=True,verbose_name="список продуктов")

    def level(self):
        level = 0
        if self.supplier is None:
            return level
        return self.supplier.level() + 1

    def __str__(self):
        return f"{self.name} (Level {self.level()})"

    class Meta:
        verbose_name = "звено сети"
        verbose_name_plural = "звенья сети"
