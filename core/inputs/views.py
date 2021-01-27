from django.shortcuts import render


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
    print(request.POST)
    return render(request, 'send.html', locals())