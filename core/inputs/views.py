from django.shortcuts import render
from .models import Information
from django.http import JsonResponse


def inputs(request):
    add_number = 1
    number = list(range(add_number))
    return render(request, 'inputs.html', locals())


def add(request):
    param = int(request.POST['number'])
    add_number = param + 1
    number = list(range(add_number))
    return render(request, 'inputs.html', locals())


def send(request):
    data = request.POST
    slovar = {}
    for key in data:
        if not key == 'csrfmiddlewaretoken':
            slovar[key] = data[key]
    Information.objects.create(info=slovar)
    info = str(Information.objects.order_by('-id')[0])
    return JsonResponse(info, safe=False)
