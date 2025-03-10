from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "bo'limlar.html")
        return redirect('login')


class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
            context = {
                'mahsulotlar': mahsulot,
            }
            return render(request, "mahsulotlar.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx1=request.POST.get('narx1'),
                narx2=None if request.POST.get('narx2') == "" else request.POST.get('narx2'),
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                oxirgi_sana=datetime.now() if request.POST.get('sana') == "" else request.POST.get('sana'),
                bolim=Bolim.objects.filter(bolim=request.user.sotuvchi.bolim)
            )
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotTahrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = get_object_or_404(Mahsulot, id=pk)
            context = {
                'mahsulot': mahsulot,
            }
            return render(request, "mahsulot-tahrirlash.html", context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = get_object_or_404(Mahsulot, id=pk)
            mahsulot.nom = request.POST.get('nom')
            mahsulot.brend = request.POST.get('brend')
            mahsulot.narx1 = request.POST.get('narx1')
            mahsulot.narx2 = None if request.POST.get('narx2') == "" else request.POST.get('narx2')
            mahsulot.miqdor = request.POST.get('miqdor')
            mahsulot.olchov = request.POST.get('olchov')
            mahsulot.save()
            return redirect('mahsulotlar')


def mahsulot_delete(request, pk):
    if request.user.is_authenticated:
        mahsulot = get_object_or_404(Mahsulot, id=pk)

        if request.method == 'POST':
            mahsulot.delete()
            return redirect('mahsulotlar')
        context = {
            'mahsulot': mahsulot,
        }

        return render(request, 'mahsulot_delete.html', context)
    return redirect('login')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.all()
            context = {
                'mijozlar': mijozlar,
            }
            return render(request, 'mijozlar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            ism = request.POST.get('mijoz-ism')
            dokon = request.POST.get('mijoz-dokon')
            telefon = request.POST.get('mijoz-tel')
            manzil = request.POST.get('mijoz-manzil')
            qarz = 0.0
            bolim = Bolim.objects.all()

            if ism and dokon and telefon:
                Mijoz.objects.create(
                    ism=ism,
                    dokon=dokon,
                    tel=telefon,
                    manzil=manzil,
                    qarz=qarz,
                    bolim=bolim
                )

            return redirect('mijozlar')
        return redirect('login')


def MijozTahrirlash(request, pk):
    if request.user.is_authenticated:
        mijoz = Mijoz.objects.get(pk=pk)
        if request.method == "POST":
            Mijoz.objects.filter(pk=pk).update(
                ism=request.POST.get('ism'),
                dokon=request.POST.get('dokon'),
                manzil=request.POST.get('manzil'),
                tel=request.POST.get('tel'),
                qarz=0 if request.POST.get('qarz') == '' else request.POST.get('qarz'),
            )
            return redirect("mijozlar")
        context = {
            "mijoz": mijoz,
        }

        return render(request, 'mijoz-tahrirlash.html', context)
    return redirect('login')


def mijoz_delete(request, pk):
    if request.user.is_authenticated:
        mijoz = get_object_or_404(Mijoz, id=pk)

        if request.method == 'POST':
            mijoz.delete()
            return redirect('mijozlar')
        context = {
            'mijoz': mijoz,
        }

        return render(request, 'mijoz_delete.html', context)
    return redirect('login')
