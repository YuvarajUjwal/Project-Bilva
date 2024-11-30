from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

def Home(request):
    tags = Tags.objects.all()
    pictures = []
    count = 0
    for tag in tags:
        count += 1
        if count > 4:
            break
        picture = Galeries.objects.filter(tag=tag).order_by('?').first()
        if picture:
            pictures.append(picture)

    context = {'pictures':pictures}
    return render(request,'events/home.html',context)

def About(request):
    context = {}
    return render(request,'events/about.html',context)

def Gallery(request):
    tags = Tags.objects.all()
    pictures = []
    for tag in tags:
        picture = Galeries.objects.filter(tag=tag).order_by('?').first()
        if picture:
            print(picture.tag)
            pictures.append(picture)

    context = {'pictures':pictures}
    return render(request,'events/gallery.html',context)

def Services(request):
    context = {}
    return render(request,'events/services.html',context)

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        form = EnquireForm(request.POST)
        if form.is_valid():
            form.save()
    context = {}
    return render(request,'events/contact.html',context)

def category(request,slug):
    tag = Tags.objects.get(category=slug)
    photos = Galeries.objects.filter(tag=tag)
    context = {'photos':photos,'slug':slug}
    return render(request,'events/picturecategory.html',context)

def upload_image(request):
    if request.user.is_superuser == False:
        return redirect('login')
    
    tags = Tags.objects.all()
    form = ImageForm()

    if request.method == 'POST':
        tag = request.POST.get('tag')
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    return render(request, 'events/upload.html',{'tags':tags,'form':form})

def Enquire_db(request):
    if request.user.is_superuser == False:
        return redirect('login')
    
    enquire = Enquire.objects.all()
    return render(request,'events/enquire_db.html',{'enquire':enquire})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminpage')
        
    return render(request, 'events/login.html')

def Create_tag(request):
    tags = Tags.objects.all()
    if request.method == 'POST':
        form = TagForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = TagForm()

    return render(request, 'events/create_tag.html',{'form':form,'tags':tags})

def Logout(request):
    logout(request)
    return redirect('home')

def Options(request):
    if request.user.is_superuser == False:
        return redirect('login')
    
    if request.method == 'POST':
        option = request.POST.get('option')
        if option == '1':
            return redirect('upload')
        elif option == '2':
            return redirect('create_tag')
        elif option == '3':
            return redirect('image_check')
        elif option == '4':
            return redirect('db')

    return render(request, 'events/options.html')

def Update_tag(request,pk):
    tag = Tags.objects.get(id=pk)
    form = TagForm(instance=tag)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('create_tag')
    return render(request, 'events/update_tag.html',{'tag':tag,'form':form})

def Delete_content(request,pk):
    tag = Tags.objects.get(id=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('create_tag')
    return render(request, 'events/delete_content.html',{'tag':tag})

def Delete_image(request,pk):
    tag = Galeries.objects.get(id=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('image_check')
    return render(request, 'events/delete_image.html',{'tag':tag})

def ImageShow(request):
    tags = Tags.objects.all()
    images = {}
    category = ''
    if request.method == 'POST':
        tag = request.POST.get('category')
        images = Galeries.objects.filter(tag=tag)
        for i in images:
            category = i.tag
            break        

    context = {'tags':tags,'show':images,'images':images,'category':category}
    return render(request,"events/image_check.html",context)