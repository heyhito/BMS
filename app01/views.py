from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
#首页
def index(request):
    name = models.Book_Messages.objects.all()
    return render(request,'home.html',{'name':name})

#添加书籍
def add(request):
    if request.method == 'GET':
        return render(request,'add.html')
    else:
        name = request.POST.get('book_name')
        price = request.POST.get('book_price')
        data = request.POST.get('book_data')
        press = request.POST.get('book_press')
        models.Book_Messages.objects.create(
            name=name,
            price=price,
            data=data,
            press=press,
        )
        return redirect('home')

#编辑书籍信息
def edit(request,book_id):
    if request.method == 'GET':
        try:
            obj = models.Book_Messages.objects.get(id=book_id)
        except Exception:
            return HttpResponse('别瞎几把改!!')
        return render(request,'book_edit.html',{'obj':obj})
    else:
        name = request.POST.get('book_name')
        price = request.POST.get('book_price')
        data = request.POST.get('book_data')
        press = request.POST.get('book_press')
        models.Book_Messages.objects.filter(id=book_id).update(
            name = name,
            price = price,
            data = data,
            press = press,
        )
        return redirect('home')

#删除书籍
def delete(request,book_id):
    models.Book_Messages.objects.get(id=book_id).delete()
    return redirect('home')