from django.shortcuts import render
from .models import Parent, Kid, Icecream, Shop


def test(request):
    data = Shop.objects.all()
    print('\n', data, '\n')
    return render(request, 'main/index.html', {'data': data})
