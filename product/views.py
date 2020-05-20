from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render

# Create your views here.
from home.models import Setting
from product.models import CommentForm, Comment, Category
from user.models import AddProductForm


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = AddProductForm(request.POST, request.FILES)
    context = {'setting': setting,
               'category': category,
               'form': form,

               }
    return render(request, 'user_addproduct.html', context)

@login_required(login_url='/login') #check login
def addcomment(request,id):
     url = request.META.get('HTTP_REFERER')
     if request.method == 'POST': #POST EDİLDİYSE
         form = CommentForm(request.POST)
         if form.is_valid():
             current_user=request.user#access user session information

             data = Comment()
             data.user_id = current_user.id
             data.product_id = id
             data.subject = form.cleaned_data['subject']
             data.comment = form.cleaned_data['comment']
            #data.rate = form.cleaned_data['rate']
             data.ip = request.META.get('REMOTE_ADDR')
             data.save()#veritabanına kaydet

             messages.success(request, "yorum gönderildi saolun")


             return HttpResponseRedirect(url)

     messages.warning(request, "yorum gönderilemedi lan bişey bozuk")
     return HttpResponseRedirect(url)