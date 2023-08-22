from django.db import models


class BaseProduct(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    img = models.ImageField(upload_to='photos', blank=True)
    # Общие поля для всех товаров


class CoolingCabinet(BaseProduct):
    volume = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Шкафы холодильные'


class Refrigerator(BaseProduct):
    volume = models.IntegerField()
    # internal =
    power = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Холодильные камеры'


class FreezerChest(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Морозильные лари'


class Monoblock(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Моноблоки'


class Showcase(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Витрины'


class Conditioner(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Кондиционеры'


class MobileConditioner(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Мобильные Кондиционеры'


class Bakery(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Выпечка'


class ThermalEquipment(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Тепловое оборудование'


class CombiSteamer(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Пароконвектоматы'


class ConvectionOven(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Конвекционные печи'


class MechanicalEquipment(BaseProduct):
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Механическое оборудование'
