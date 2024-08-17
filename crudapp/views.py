from django.shortcuts import render,redirect
from crudapp.forms import CrudForm
from .models import CrudModel
# Create your views here.
def create(request):
    if request.method == "POST":
        fm = CrudForm(request.POST)
        if fm.is_valid():
            name= fm.cleaned_data['name']
            book=fm.cleaned_data['book']
            game=fm.cleaned_data['game']
            det = CrudModel(name=name,book=book,game=game)
            det.save()
            fm = CrudForm()
    else :
        fm = CrudForm()
    cd = CrudModel.objects.all()  
    return render(request,'create.html',{'form':fm,'cru':cd})
def delete(request,id):
    dlt = CrudModel.objects.get(id=id)
    dlt.delete()
    return redirect('create')

def update(request,id):
    if request.method == 'POST':
        up = CrudModel.objects.get(id=id)
        fm = CrudForm(request.POST,instance=up)
        if fm.is_valid():
           fm.save()
    else :
        up = CrudModel.objects.get(id=id)
        fm=CrudForm(instance=up)    
    return render(request,'update.html',{'form':fm})


def complete(request,id):
    cp = CrudModel.objects.get(id=id)
    cp.complete = True
    cp.save()
    return render(request,"create.html",{"com":cp})