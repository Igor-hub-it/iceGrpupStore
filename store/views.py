from django.shortcuts import render
from .models import *


def main(request):
    return render(request, 'store/main.html')


def contacts(request):
    return render(request, 'store/contacts.html')



def catalog(request):
    cooling_cabinets = CoolingCabinet.objects.all()
    refrigerators = Refrigerator.objects.all()
    freezer_chests = FreezerChest.objects.all()
    monoblocks = Monoblock.objects.all()
    showcases = Showcase.objects.all()
    conditioners = Conditioner.objects.all()
    mobile_air_conditioners = MobileConditioner.objects.all()
    bakery = Bakery.objects.all()
    thermal_equipment = ThermalEquipment.objects.all()
    combi_steamers = CombiSteamer.objects.all()
    convection_ovens = ConvectionOven.objects.all()
    mechanical_equipment = MechanicalEquipment.objects.all()
    context = {
        'coolingCabinets': cooling_cabinets,
        'refrigerators': refrigerators,
        'freezerChests': freezer_chests,
        'monoblocks': monoblocks,
        'showcases': showcases,
        'conditioners': conditioners,
        'mobileAirConditioners': mobile_air_conditioners,
        'bakery': bakery,
        'thermalEquipment': thermal_equipment,
        'combiSteamers': combi_steamers,
        'convectionOvens': convection_ovens,
        'mechanicalEquipment': mechanical_equipment,
    }
    return render(request, 'store/catalog.html', context)


def sortCatalog(request, product_type):
    if product_type == 'cooling_cabinet':
        products = CoolingCabinet.objects.all()
    elif product_type == 'refrigerator':
        products = Refrigerator.objects.all()
    elif product_type == 'freezer_chest':
        products = FreezerChest.objects.all()
    elif product_type == 'monoblock':
        products = Monoblock.objects.all()
    elif product_type == 'showcase':
        products = Showcase.objects.all()
    elif product_type == 'conditioners':
        products = Showcase.objects.all()
    elif product_type == 'mobileAirConditioners':
        products = Showcase.objects.all()
    elif product_type == 'bakery':
        products = Showcase.objects.all()
    elif product_type == 'thermalEquipment':
        products = Showcase.objects.all()
    elif product_type == 'combiSteamers':
        products = Showcase.objects.all()
    elif product_type == 'convectionOvens':
        products = Showcase.objects.all()
    elif product_type == 'mechanicalEquipment':
        products = Showcase.objects.all()
    else:
        # Обработка случая, когда передан некорректный тип продукта
        products = []

    context = {
        'products': products,
        'product_type': product_type,
    }
    return render(request, 'store/same_kind_products.html', context)
