from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import register,Getnumber
# Create your views here.
def Register(request):
    msg = ""
    if 'name' in request.POST:
        name = request.POST['name']
        Idnumber = request.POST['Idnumber']
        birthday = request.POST['birthday']
        sex = request.POST['sex']
        Identity = request.POST['Identity']
        tel = request.POST['tel']
        address = request.POST['address']

        countname = register.objects.filter(name=name).count()
        countIdnumber = register.objects.filter(Idnumber=Idnumber).count()

        if countname == 0 and countIdnumber == 0:  # 表示這個 病歷號 沒有註冊過
            # 新增會員資料
            # 將資料新增到資料表中
            obj = register.objects.create(name=name, Idnumber=Idnumber,birthday=birthday, sex=sex,Identity=Identity, tel=tel, address=address)
            obj.save()
            id = register.objects.all().order_by('-id')[:1]
            msg = "資料建立成功 "
        elif countname != 0:
            name = request.POST['name']
            msg = " 已存在，請重新填寫 "
            msg = name + msg
        else:
            # Idnumber = request.POST['Idnumber']
            msg = " 此身分證號碼已存在，請重新填寫 "

    return render(request,'register.html',locals())

def Patients(request):
    data = Getnumber.objects.all().order_by('id')
    content = {"patientsList": data}
    return render(request,'patients.html',content)

def Registermain(request):
    return render(request,'registermain.html')

def find(request):
    num = request.GET.get('findnumber', '')
    if num == '':
        nosearch = 1
    else:
        id = register.objects.filter(id=num).first()  # 抓第一筆資料
        if id == None:
            notfound = 1
        else:
            details = register.objects.filter(id=num)[:1]
    return render(request,'findmypatient.html',locals())

def getNumber(request):
    msg = ""
    if 'name' in request.POST:
        name = request.POST['name']
        Idnumber = request.POST['Idnumber']
        birthday = request.POST['birthday']
        sex = request.POST['sex']
        reIdentity = request.POST['reIdentity']

        confirmname = register.objects.filter(name=name).count()
        confirmId = register.objects.filter(name=name,Idnumber=Idnumber).count()

        if confirmname != 0 and confirmId != 0:

            countname = Getnumber.objects.filter(name=name).count()
            if countname == 0:  # 表示這個 名字沒有掛號過
                # 將資料新增到資料表中
                obj = Getnumber.objects.create(name=name,Idnumber=Idnumber, birthday=birthday, sex=sex, reIdentity=reIdentity,)
                obj.save()
                id = Getnumber.objects.all().order_by('-id')[:1]
                msg = "掛號成功 "

            else:
                name = request.POST['name']
                msg = " 重複掛號，請重新操作 "
                msg = name + msg
        elif confirmname != 0 and confirmId == 0 :
            msg = "身分證號碼輸入錯誤，請重新掛號"
        else:
            msg = "初診請至初診系統填寫資料"

    return render(request,'getnumber.html', locals())

def Login(request):
        msg = ""
        if "acc" in request.POST:
            acc = request.POST['acc']
            password = request.POST['password']

            if acc == '001' and password == '001':
                request.session['acc'] = acc  # 儲存session 資料
                request.session['isAlive'] = True

                response = HttpResponseRedirect('/registermain')
                return response
            else:
                msg = "帳密錯誤，請重新輸入"
                return render(request, 'login.html', locals())

        else:
            if 'acc' in request.session and 'isAlive' in request.session:
                return HttpResponseRedirect("/registermain")
            else:
                return render(request, 'login.html', locals())
        return render(request,'login.html')

def Logout(request):
    del request.session["isAlive"] #刪除SESSION內容
    del request.session["acc"]
    response = HttpResponseRedirect('/login')
    return response


def Consult(request):

    return render(request,'diagnose.html')