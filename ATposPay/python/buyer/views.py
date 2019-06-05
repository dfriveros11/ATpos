from rest_framework import serializers
from .models import Buyer
from django.shortcuts import render, redirect
from .forms import BuyerForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.http import JsonResponse
from django.forms.models import model_to_dict
from .serializers import BuyerSerializer
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')

def BuyerList(request):
    buyers = Buyer.objects.all()
    serializer = BuyerSerializer(buyers, many=True)
    return Response(serializer.data)
    #queryset = Buyer.objects.all()
    #context = {
    #    'buyer_list': queryset
    #}
    #return render(request, "estandar.html", context)

def BuyerCreate(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        print (request.body)
        buyer = form.save()
        buyer.save()
        messages.add_message(request, messages.SUCCESS, 'Buyer created successfully')
        return HttpResponseRedirect(reverse('buyerCreate'))
    else:
        form = BuyerForm()
    context = {
        'form': form,
    }

    return render(request, 'estandar.html', context)
