from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Wishlist, User

# Create your views here.
def index(request):
    items = Wishlist.objects.all()
    for item in items:
        for user in item.wish.all():
            print item.item
            print user.id
    print request.session['user_id']
    context = {
    'items': Wishlist.objects.all(),
    'users': User.objects.get(id=request.session['user_id'])
    }
    if not 'user_id' in request.session:
        messages.error(request, 'Must be logged in to continue!')
        return redirect('users:index')
    return render(request, 'main/index.html', context)

def wishitems(request):

    return render(request, 'main/wishitems.html')

def newitem(request):
    user_id = request.session['user_id']
    response_from_models = Wishlist.objects.new(request.POST, user_id)
    if response_from_models['status']:
        return redirect('main:index')
    else:
        for error in response_from_models['errors']:
            messages.error(request, error)
        return redirect('main:wishitems')

def additem(request, id):
    user_id = request.session['user_id']
    item_id = id
    response_from_models = Wishlist.objects.editlist(user_id, item_id)


    return redirect('main:index')

def inspect(request, id):
    context = {
    'item': Wishlist.objects.get(id=id),
    }
    return render(request, 'main/inspect.html', context)


def delete(request, id):
    curr_item = Wishlist.objects.get(id=id)
    curr_item.delete()
    return redirect('main:index')

def remove(request, id):
    curr_user = request.session['user_id']
    curr_item = Wishlist.objects.get(id=id)
    curr_item.wish.remove(curr_user)
    return redirect('main:index')
