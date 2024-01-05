from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

def home(request,c_slug=None):
    current_category  = None
    filtered_products = None
    paginated_products = None

    if current_category!=None:
        current_category =get_object_or_404(categ,slug=c_slug)
        filtered_products=products.objects.filter(category=current_category ,available=True)
    else:
         filtered_products=products.objects.all().filter(available=True)
         paginator=Paginator(filtered_products,4)
         try:
             page=int(request.GET.get('page','1'))
         except:
             page=1
         try:
             paginated_products=paginator.page(page)
         except (EmptyPage,InvalidPage):
             paginated_products=paginator.page(paginator.num_pages)
    all_categories=categ.objects.all()
    return render(request,'home.html',{'pr':filtered_products,'categories': all_categories,'products':paginated_products})


def details(request,c_slug,product_slug):
    try:
        prd=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
       raise e
    return render(request,'details.html',{'pr':prd})


def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'qr':query,'p':prod})