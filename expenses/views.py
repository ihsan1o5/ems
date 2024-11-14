from django.shortcuts import render
from django.db.models import Q
from .models import Client, Vehicle, Shipment


def homeView(request):

    client = request.GET.get('client', None)
    driver = request.GET.get('driver', None)
    date = request.GET.get('date', None)

    clients = Client.objects.all().order_by('-id')
    trucks = Vehicle.objects.all().order_by('-id')

    filters = Q()
    if client:
        filters &= Q(client_id=client)
    if driver:
        filters &= Q(vehicle_id=driver)
    if date:
        filters &= Q(time_departure__date=date)

    shipments = Shipment.objects.filter(filters).order_by('-id') if filters else Shipment.objects.all().order_by('-id')

    total_balance = sum(shipment.balance for shipment in shipments)
    total_price = Shipment.total_price(queryset=shipments)
    total_paid_amount = Shipment.total_paid_amount(queryset=shipments)

    context = {
        'clients': clients,
        'trucks': trucks,
        'total_price': total_price,
        'total_paid_amount': total_paid_amount,
        'total_balance': total_balance,
        'total_shipments': shipments.count(),
        'shipments': shipments,
    }
    return render(request, 'dashboard/index.html', context)
