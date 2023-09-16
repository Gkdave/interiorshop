from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm 
from django.utils.text import slugify 
from django.shortcuts import render, redirect,get_object_or_404 

from .models import Vendor
from shop.product.models import Product 

from .forms import ProductForm 

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
        
    return render(request,'vendor/become_vendor.html',{'form': form })


@login_required
def vendor_admin(request):
    vendor = request.user.vendor 
    products = vendor.products.all()
    
    return render(request,'vendor/vendor_admin.html',{'vendor':vendor, 'products': products})
    
        
@login_required 
def add_product(request):
    if request.method == 'POST':
        
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor 
            product.slug = slugify(product.title)
            product.save()
            
            return redirect('vendor_admin') 
    else:
        form = ProductForm()
        
    return render(request, 'vendor/add_product.html',{'form': form}) 
@login_required
def edit_product(request, pk):
    vendor = request.user.vendor 
    product = vendor.products.get(pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)
        
        if image_form.is_valid():
            productimage = image_form.save(commit=False)
            productimage.product = product
            productimage.save()
            
            return redirect('vendor_admin')
        
        if form.is_valid():
            form.save()
            
            return redirect('vendor_admin')
        
    else:
        form = ProductForm(instance=product)
        image_form = ProductForm()
        
    return render(request, 'vendor/edit_product.html',{'form':form, 'image_form':image_form, 'product':product})

@login_required
def edit_vendor(request):
    vendor = request.user.vendor
    
    if request.method == "POST":
        name = request.POST.get('name', '')
        emal = request.POST.get('email','')
        
        if name:
            vendor.created_by.email = email
            vendor.created_by.save()
            
            vendor.name = name
            vendor.save()
            
            return redirect('vendor_admin')
        
        
    return render(request, 'vendor/edit_vendor.html',{'vendor':vendor})

def vendors(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendors.html',{'vendors':vendors})
    
def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    
    return render(request, 'vendor/vendor.html',{'vendor':vendor})
    


            
    
            
        
    
