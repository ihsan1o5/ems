from django.shortcuts import render
from .models import Client, Vehicle, Shipment


def homeView(request):

    clients = Client.objects.all().order_by('-id')
    trucks = Vehicle.objects.all().order_by('-id')
    shipments = Shipment.objects.all().order_by('-id')
    print(shipments.count())
    total_balance = sum(shipment.balance for shipment in shipments)
    total_price = Shipment.total_price()
    total_paid_amount = Shipment.total_paid_amount()

    context = {
        'clients': clients,
        'trucks': trucks,
        'total_price': total_price,
        'total_paid_amount': total_paid_amount,
        'total_balance': total_balance,
        'total_shipments': shipments.count()
    }
    return render(request, 'dashboard/index.html', context)
