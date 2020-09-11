from django.shortcuts import render,redirect
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect)
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserDataForm
from django.contrib.auth.decorators import login_required
from .models import UserData
# Create your views here.
def registration(request):
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():  
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Successfully Registered' + user)                
                return redirect('login')

        context ={'form': form}
        return render(request, 'index.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)  
        
            if user is not None:
                login(request,user)
                return redirect('posts')    
            else:
                messages.info(request,'incorrect crendentials')
        context={}
        return render(request,'login.html',context)
def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def posts(request):
    newpost=UserData.objects.all()
    return render(request,'Posts.html',{'post':newpost})
    
@login_required(login_url='login')
def profile(request):
    #users = Users.objects.all()
    
    newpost=UserData.objects.all().filter(userid=request.user.id)
    user=request.user
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST,instance=user) 
        if form.is_valid():
            form.save()
            return redirect('posts')

    return render(request,"profile.html",{'post':newpost,'form':form})

def newpost(request):
    form = UserDataForm()
    return render(request,'newpost.html',{'form':form})

def postsubmit(request):
    # userid=request.POST['id']
    # newpost=request.POST['newpost']
    # email=request.POST['email']
    # username=request.POST['username']
    # p = UserData(userid=userid,post=newpost,email=email,username=username)
    # p.save()
    # newpost=UserData.objects.all().filter(userid=request.user.id)
    # print(newpost)
    # return render(request,"profile.html",{'post':newpost})
    if request.method == 'POST':
        form = UserDataForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserDataForm()
    return render(request,'newpost.html',{'form':form})

def update(request):
    return render(request,'update.html')

def updateData(request):
    # password=request.POST['password']
    # email=request.POST['email']
    # username=request.POST['username']
    # u=CreateUserForm(username=username,email=email)
    # u.save()
    return render(request,'profile.html')
def deleteData(request,image):
    obj =get_object_or_404(UserData,id=image)
    obj.delete()
    newpost=UserData.objects.all().filter(userid=request.user.id)
    print(newpost)
    return render(request,"profile.html",{'post':newpost})
    