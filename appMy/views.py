from django.shortcuts import render,redirect
from .models import*

def indexPage(request):
    content1=Card.objects.get(id=1)
    news=Card.objects.filter(new=True)
    cards=Card.objects.all()
    category=Category.objects.all()
    news2=news.order_by("?")[:2]
    context={
        "content1":content1,
        "newsCard":news2,
        "newsCard4":news[:4],
        "cards":cards,
        "category":category
    }
    return render(request, 'index.html',context)

def detailPage(request,idcard):
    detailCard=Card.objects.get(id=idcard)
    comments=Comment.objects.filter(card=detailCard)
    
    if request.method=="POST":
        fname=request.POST.get("fname")
        text=request.POST.get("text")
        comment=Comment(fname=fname, text=text, card=detailCard,)
        comment.save()
        return redirect('/detail/'+ idcard)
        
         
    context={
        "detailCard":detailCard,
        "comments":comments,
    }
    return render(request, 'detail.html', context)




def categoryPage(request,categorytitle=None):
    if Card.objects.filter(category__title=categorytitle).exists():
        cards=Card.objects.filter(category__title = categorytitle)
    else:
        cards=Card.objects.all()
        
    category=Category.objects.all()
    context={
       
        "cards":cards,
        "category":category,
        
    }
    return render (request, "category.html", context)





def formPage(request):
    
    if request.method == "POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        email=request.POST.get("email")
        message=request.POST.get("message")
        
        print(fname,lname,phone,address,email,message)
    
    return render(request,"form.html")
