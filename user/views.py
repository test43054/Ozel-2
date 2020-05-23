from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from home.models import UserProfile
from product.models import Category, Comment, Product
from user.forms import UserUpdateForm, ProfileUpdateForm, UserUpdateForm1
from user.models import AddProductForm


def index(request):
    category = Category.objects.all()
    current_user = request.user #Access user session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    #return HttpResponse(profile)
    context ={'category' : category,
              'profile' : profile,
              }
    return render(request, 'user_profile.html',context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request , 'Your account has been updated!')
            return redirect('/user')

    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user) #Important!
            messages.success(request, 'Your password was successfully update!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form' : form,
            'category' : category
        })

@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    # return HttpResponse("yorumlar")
    context = {'category': category,
               'comments': comments,
               }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login')
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'silindi')
    return HttpResponseRedirect('/user/comments')


########################################################################################################
@login_required(login_url='/login')
def myhomes(request):
    category = Category.objects.all()
    current_user = request.user
    products = Product.objects.filter(user_id=current_user.id)
    # return HttpResponse("yorumlar")
    context = {'category': category,
               'products': products,
               }
    return render(request, 'myhomes.html', context)
    #return HttpResponse("myhomesdeneme ")

@login_required(login_url='/login')
def deletemyhomes(request,id):
    current_user = request.user
    Product.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'silindi')
    return HttpResponseRedirect('/user/myhomes')



def userhome_update(request,id):#burda id yi alıyoruz product user id sine atıyoruz eşitlensin boş kalmsın diye
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        userhomeupdate_form = UserUpdateForm1(request.POST, request.FILES, instance=product)
        #profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if userhomeupdate_form.is_valid():
            userhomeupdate_form.save()
            messages.success(request , 'Your has been updated!')
            return redirect('/user/myhomes')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(userhomeupdate_form.errors))
            return HttpResponseRedirect('/user/myhomes')
    else:
        category = Category.objects.all()
        userhomeupdate_form = UserUpdateForm1(instance=product)
        context = {
            'category': category,
            'userhomeupdate_form': userhomeupdate_form,
            'product': product,
        }
        return render(request, 'userhome_update.html', context)
