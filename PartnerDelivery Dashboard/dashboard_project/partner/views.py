from django.shortcuts import render


# Dashboard Page
def dashboard(request):

    orders = [
        {"id": 101, "customer": "Rahul", "status": "Delivered"},
        {"id": 102, "customer": "Ananya", "status": "Pending"},
        {"id": 103, "customer": "Kiran", "status": "Delivered"},
    ]

    context = {
        "total_orders": 120,
        "delivered_orders": 90,
        "pending_orders": 30,
        "total_partners": 15,
        "orders": orders
    }

    return render(request, 'partner/dashboard.html', context)


# Orders Page
def orders(request):

    orders_list = [
        {"id": 101, "customer": "Rahul", "address": "Bangalore", "status": "Delivered"},
        {"id": 102, "customer": "Ananya", "address": "Mysore", "status": "Pending"},
        {"id": 103, "customer": "Kiran", "address": "Mangalore", "status": "Delivered"},
    ]

    context = {
        "orders": orders_list
    }

    return render(request, 'partner/orders.html', context)


# Partners Page
def partners(request):

    partners_list = [
        {"id": 1, "name": "Ramesh", "phone": "9876543210", "status": "Active"},
        {"id": 2, "name": "Suresh", "phone": "9876541230", "status": "Active"},
        {"id": 3, "name": "Mahesh", "phone": "9123456780", "status": "Inactive"},
    ]

    context = {
        "partners": partners_list
    }

    return render(request, 'partner/partners.html', context)


# Payments Page
def payments(request):

    payments_list = [
        {"partner": "Ramesh", "amount": 500, "status": "Paid"},
        {"partner": "Suresh", "amount": 350, "status": "Pending"},
        {"partner": "Mahesh", "amount": 420, "status": "Paid"},
    ]

    context = {
        "payments": payments_list
    }

    return render(request, 'partner/payments.html', context)


# Deliveries Page
def deliveries(request):

    deliveries_list = [
        {"order_id": 101, "partner": "Ramesh", "status": "Delivered"},
        {"order_id": 102, "partner": "Suresh", "status": "Out for Delivery"},
        {"order_id": 103, "partner": "Mahesh", "status": "Pending"},
    ]

    context = {
        "deliveries": deliveries_list
    }

    return render(request, 'partner/deliveries.html', context)