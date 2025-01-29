from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import *

def home_view(request):
    today = datetime.today()
    context = {
        'today': today,
    }
    return render(request, 'home.html', context)

def yonalishlar_view(request):
    yonalishlar = Yonalish.objects.all()
    context = {
        'yonalishlar': yonalishlar,
    }
    return render(request, 'yonalishlar.html', context)

def yonalish_details_view(request, yonalish_id):
    yonalish = Yonalish.objects.get(id = yonalish_id)
    context = {
        'yonalish': yonalish,
    }
    return render(request, 'yonalish_details.html', context)

def fanlar_view(request):
    fanlar = Fan.objects.all()
    context = {
        'fanlar': fanlar,
    }
    return render(request, 'fanlar.html', context)

def fan_details_view(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    context = {
        'fan':fan,
    }
    return render(request, 'fan_details.html', context)

def ustozlar_view(request):
    ustozlar = Ustoz.objects.all()
    context = {
        'ustozlar': ustozlar,
    }
    return render(request, 'ustozlar.html', context)

def ustoz_details_view(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    context = {
        'ustoz':ustoz,
    }
    return render(request, 'ustoz_details.html', context)

def fan_d_view(request, pk):
    fan = Fan.objects.filter(id = pk)
    fan.delete()
    return redirect('fanlar')

def yonalish_d_view(request, pk):
    yonalish = Yonalish.objects.filter(id = pk)
    yonalish.delete()
    return redirect('yonalishlar')

def ustoz_d_view(request, pk):
    ustoz = Ustoz.objects.filter(id = pk)
    ustoz.delete()
    return redirect('ustozlar')

def fan_update_view(request, pk):
    fan =  get_object_or_404(Fan, id = pk)
    context = {
        'fan': fan
    }
    return render(request, 'fan_update.html', context)

def fan_update_view(request, pk):
    fan = get_object_or_404(Fan, id=pk)
    if request.method == "POST":
        Fan.objects.filter(id=pk).update(
            yonalish = get_object_or_404(Yonalish, id=request.POST.get('yonalish_id')),
            nom = request.POST.get('nom'),
            asosiy = request.POST.get('asosiy'),
        )
        return redirect('fanlar')

    yonalishlar = Yonalish.objects.all()
    context = {
        'fan': fan,
        'yonalishlar': yonalishlar
    }
    return render(request, 'fan_update.html', context)

def yonalish_update_view(request, pk):
    yonalish = get_object_or_404(Yonalish, id=pk)
    if request.method == "POST":
        aktiv = request.POST.get('aktiv')
        if aktiv == 'on':
            aktiv = True
        else:
            aktiv = False

        Yonalish.objects.filter(id=pk).update(
            nom = request.POST.get('nom'),
            aktiv = aktiv,
        )
        return redirect('yonalishlar')

    context = {
        'yonalish': yonalish
    }
    return render(request, 'yonalish_update.html', context)

def ustoz_update_view(request, pk):
    ustoz = get_object_or_404(Ustoz, id = pk)
    fanlar = Fan.objects.all()
    if request.method == 'POST':
        Ustoz.objects.filter(id=pk).update(
            ism = request.POST.get('ism'),
            yosh = request.POST.get('yosh'),
            jins = request.POST.get('jins'),
            daraja = request.POST.get('daraja'),
            fan = request.POST.get('fan'),
        )
        return redirect('ustozlar')

    context = {
        'ustoz': ustoz,
        'fanlar': fanlar,
    }
    return render(request, 'ustoz_update.html', context)

