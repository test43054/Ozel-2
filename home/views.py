import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile
from product.models import Product, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:10]
    category=Category.objects.all()
    dayproducts = Product.objects.all()[:7]
    lastproducts = Product.objects.all().order_by('-id')[:7]
    randomproducts = Product.objects.all().order_by('?')[:3]

    context = {'setting': setting,
               'page': 'home',
               'sliderdata':sliderdata,
               'sliderone':sliderdata[1].id,
               'category':category,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):

    if request.method == 'POST':  # FORM POST EDİLDİYSE
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kur
            data.name = form.cleaned_data['name']  # formsdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # veritabanına kaydet
            messages.success(request, "mesajınız kaydedilmiştir iyi günler dileriz")
            return HttpResponseRedirect ('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)



def category_products(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    #products = Product.objects.all()
    context = {'products': products, 'category': category,'categorydata':categorydata}
    return render(request,'products.html', context)


def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'product': product,
               'category': category,
               'images': images,
               'comments': comments,
               }
    return render(request,'product_detail.html',context)


def product_search(request):
    if request.method == 'POST': #Check Form post
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()

            query = form.cleaned_data['query'] #get form data
            catid = form.cleaned_data['catid']

            if catid == 0:
                products = Product.objects.filter(title__icontains=query) #select * from products where title like %query%
            else:
                products =Product.objects.filter(title__icontains=query,category_id=catid)
            context ={ 'products': products,
                       'category': category,

                     }
            return render(request, 'products_search.html', context)
    return HttpResponseRedirect('/')

def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            messages.warning(request,'Giriş başarılı olmadı, kontrol edin!!!!')
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category,

              }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request,user)
            #PROFİL TABLOSUNuDA OLUŞTUR
            current_user = request.user
            data = UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
           # messages.success(request, "üye oldunuz süpersiniz!!!!!!")
            return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    context ={ 'category' : category,
               'form': form,

    }
    return render(request, 'signup.html', context)