from django.db import models


class CoolingCabinet(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Шкафы холодильные'


class Refrigerator(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    # internal =
    power = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Холодильные камеры'


class FreezerChest(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Морозильные лари'


class Monoblock(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Моноблоки'


class Showcase(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Витрины'


class Conditioner(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Кондиционеры'


class MobileConditioner(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Мобильные Кондиционеры'


class Bakery(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Выпечка'


class ThermalEquipment(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Тепловое оборудование'


class CombiSteamer(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Пароконвектоматы'


class ConvectionOven(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Конвекционные печи'


class MechanicalEquipment(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    volume = models.IntegerField()
    temperatureRangeFrom = models.IntegerField()
    temperatureRangeTo = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Механическое оборудование'
