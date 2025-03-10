from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


def ogohlantirish_view(request):
    return render(request, 'ogohlantirish.html')


class SotuvlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(bolim=request.user.sotuvchi.bolim)
            mijozlar = Mijoz.objects.all()
            mahsulotlar = Mahsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
            context = {
                "sotuvlar": sotuvlar,
                "mahsulotlar": mahsulotlar,
                "mijozlar": mijozlar,
            }
            return render(request, "sotuvlar.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            qarz = None if request.POST.get('qarz') == "" else float(request.POST.get('qarz'))
            mijoz = Mijoz.objects.get(id=request.POST.get('mijoz_id'))
            jami_summa = (request.POST.get('jami_summa'))
            tolandi = (request.POST.get('tolandi'))

            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot_id'))
            miqdor = float(request.POST.get('miqdor'))

            if miqdor > mahsulot.miqdor:
                return render(request, "ogohlantirish.html", {'message': "Mahsulot yetarli emas!"})

            elif (request.POST.get('qarz') and request.POST.get('jami_summa') == '' and
                  request.POST.get('tolandi') == ''):
                jami_summa = miqdor * mahsulot.narx2
                tolandi = jami_summa - float(request.POST.get('qarz'))

            elif request.POST.get('jami_summa') == '' and request.POST.get('tolandi') == '':
                qarz = 0
                jami_summa = miqdor * mahsulot.narx2
                tolandi = miqdor * mahsulot.narx2
            elif request.POST.get('jami_summa') == '':
                jami_summa = miqdor * mahsulot.narx2
                tolandi = jami_summa
                qarz = 0
            elif request.POST.get('tolandi') == '':
                jami_summa = miqdor * mahsulot.narx2
                qarz = jami_summa - float(tolandi)
            elif qarz == None:
                qarz = float(jami_summa) - float(tolandi)
            Sotuv.objects.create(
                mahsulot=mahsulot,
                mijoz=mijoz,
                miqdor=miqdor,
                jami_summa=jami_summa,
                qarz=qarz,
                tolandi=tolandi,
                bolim=request.user.sotuvchi.bolim,
            )

            mijoz.qarz += qarz
            mijoz.save()

            mahsulot.miqdor -= miqdor
            mahsulot.save()
            return redirect('sotuvlar')
        return redirect('login')


class SotuvTahrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = get_object_or_404(Sotuv, id=pk)
            context = {
                'sotuv': sotuv,
            }
            return render(request, "sotuv-tahrirlash.html", context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            sotuv = get_object_or_404(Sotuv, id=pk)
            sotuv.miqdor = request.POST.get('miqdor')
            sotuv.jami_summa = request.POST.get('jami_summa')
            sotuv.tolandi = request.POST.get('tolandi')
            sotuv.qarz = request.POST.get('qarz')
            sotuv.save()
            return redirect('sotuvlar')


def sotuv_delete(request, pk):
    if request.user.is_authenticated:
        sotuv = get_object_or_404(Sotuv, id=pk)

        if request.method == 'POST':
            sotuv.delete()
            return redirect('sotuvlar')
        context = {
            'sotuv': sotuv,
        }

        return render(request, 'sotuv_delete.html', context)
    return redirect('login')
