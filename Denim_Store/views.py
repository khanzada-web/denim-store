from django.http import HttpRequest
from django.shortcuts import render
from stock.models import item
from .form import Catagories


def index(request):
    # Stock_Data=item.objects.all()

    Catagories_Data=Catagories()
    data={
        "Website_Name":"Denim Vault",
        "hero1":"Welcome to Denim Vault",
        "hero2":"Unlock Your Perfect Fit",
        "hero3":"At Denim Vault, we bring you the finest selection of high-quality denim designed to elevate your style. From timeless classics to the latest trends, our collection offers something for every denim lover. Discover durable, stylish, and comfortable jeans made to fit your lifestyle.",
        "Head1":"Discover Our Premium Denim Collection",
        
        "Catagories":Catagories_Data
        
    }

    if request.method=="POST":
        try:
            Catagory=request.POST.get('Catagory')
            if Catagory == 'Male':
                Stock_Data = item.objects.filter(category='Male')
            elif Catagory == 'Female':
                Stock_Data = item.objects.filter(category='Female')
            else:
                Stock_Data = item.objects.all()
            data={
        "Website_Name":"Denim Vault",
        "hero1":"Welcome to Denim Vault",
        "hero2":"Unlock Your Perfect Fit",
        "hero3":"At Denim Vault, we bring you the finest selection of high-quality denim designed to elevate your style. From timeless classics to the latest trends, our collection offers something for every denim lover. Discover durable, stylish, and comfortable jeans made to fit your lifestyle.",
        "Head1":"Discover Our Premium Denim Collection",
        "Data":Stock_Data,
        "Catagories":Catagories_Data
        
    }


        except:
            pass
    
    
   
   
    return render(request,"index.html",data)