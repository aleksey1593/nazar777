from django.shortcuts import render
from .models import Information
from django.http import JsonResponse


def inputs(request):
    add_number = 1
    number = list(range(add_number))
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(session_key)
    return render(request, 'inputs.html', locals())


def add(request):
    param = int(request.POST['number'])
    add_number = param + 1
    number = list(range(add_number))
    return render(request, 'inputs.html', locals())


def send(request):
    data = request.POST
    print(data)
    slovar = {}
    for key in data:
        if not key == 'csrfmiddlewaretoken':
            slovar[key] = data[key]
    print(data)
    Information.objects.create(info=slovar)
    info = str(Information.objects.order_by('-id')[0])
    return JsonResponse(info, safe=False)