from django.shortcuts import render
from django import views
from app01.models import Taizhang
# Create your views here.
class TaizhangTable(views.View):
    def get(self,request):
        shuju = Taizhang.objects.all()
        print(shuju[0].calibration_time)
        return render(request, 'index.html',{'shuju':shuju})