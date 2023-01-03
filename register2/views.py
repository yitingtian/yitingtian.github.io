from django.shortcuts import render

from .models import register
# Create your views here.

def Register(request):
    if 'Pnumber' in request.POST:
        Pnumber = request.POST['Pnumber']
        name = request.POST['name']
        birthday = request.POST['birthday']
        sex = request.POST['sex']
        reIdentity = request.POST['reIdentity']
        Identity = request.POST['Identity']
        tel = request.POST['tel']
        address = request.POST['address']

        #將資料新增到資料表中
        obj=register.objects.create(Pnumber=Pnumber,name=name,birthday=birthday,sex=sex,reIdentity=reIdentity,Identity=Identity,tel=tel,address=address)

        obj.save()

    return render(request,'register.html')

