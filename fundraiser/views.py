from django.shortcuts import render
from datetime import datetime
from fundraiser.models import Donate
from django.core.mail import send_mail
import razorpay
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_GOnqLMbHkrycAR", "rqymj3FqdXdqYoD4ttbCg0mG"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, "index.html")

def success(request):
    return render(request, "Sucess.html")
