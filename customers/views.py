from django.shortcuts import render
from .models import Customers
from .serializers import CustomerSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def customers_list(request):
    if request.method =='GET':
        customers = Customers.objects.all()
        serializer=CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method =='POST':
        data = JSONParser().parse(request)
        serializer=CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=401)

@csrf_exempt
def customer_details(request,pk):
    try:
        customer =Customers.objects.get(pk=pk)
    except Customers.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)        
    
    if request.method =='PUT':
        data =JSONParser().parse(request)
        serializer=CustomerSerializer(customer,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=401)
    
    if request.method=='DELETE':
        customer.delete()
        return HttpResponse(status=204,safe=False)
        