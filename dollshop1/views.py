from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from dollshop1.models import Category, Product, Commentary, Wishlist, Cart
from dollshop1.forms import CommentaryForm, CartQuantityForm



def homepage(request):

    category = Category.objects.all()
    product = Product.objects.all()

    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price += item.product.price * item.quantity

    context = {
        'product': product,
        'category': category,
        'cart': cart,
        'total_price': total_price,
        'cart_items': cart.count()
    }
    return render(request, 'dollshop1/shop.html', context)


def category_list(request, cate_pk):

    category = Category.objects.all()
    product = Product.objects.filter(category=cate_pk)
    context = {
        'category': category,
        'product': product,
        'now': Category.objects.get(pk=cate_pk)
    }

    return render(request, 'dollshop1/category_list.html', context)


def product_detail(request, get_pk):
    product = Product.objects.get(pk=get_pk)
    comment = Commentary.objects.filter(product=get_pk)


    if request.method == 'POST':
        comment_form = CommentaryForm(request.POST)
        if comment_form.is_valid():
            cf = comment_form.save(commit=False)
            cf.user = request.user
            cf.product = product
            cf.save()
            return redirect('dollshop:product_detail', get_pk)
    else:
        comment_form = CommentaryForm()

    context = {
        'product': product,
        'comment': comment,
        'comment_form': comment_form,
        'count': comment.count(),
    }
    return render(request, 'dollshop1/product_detail.html', context)


def wishlist(request):
    list_object = Wishlist.objects.filter(user=request.user)
    context = {
        'list_obj': list_object
    }
    return render(request, 'dollshop1/wishlist.html', context)


def wishlist_add(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    wishlist_obj = Wishlist.objects.filter(user=request.user, product=product)
    if not wishlist_obj:
        Wishlist.objects.create(user=request.user, product=product)
        return redirect('dollshop:homepage')
    else:
        return redirect('dollshop:homepage')


def wishlist_delete(request, product_pk):
    product = Wishlist.objects.get(pk=product_pk).delete()
    # product = get_object_or_404(Wishlist, pk=product_pk)
    return redirect('dollshop:wishlist')


# def cart_list(request):
#     cart = Cart.objects.filter(user=request.user).first()
#     product = cart.product.all()
#     total_price = 0
#     for item in product:
#         total_price += item.price
#
#     context = {
#         'product': product,
#         'total_price': total_price,
#
#     }
#     return render(request, 'dollshop1/cart.html', context)


def cart_list(request):
    cart = Cart.objects.filter(user=request.user)

    total_price = 0
    for item in cart:
        total_price += item.product.price * item.quantity

    if request.method == 'POST':
        print(request.POST.get('quantity'))
        cart.quantity = request.POST.get('quantity')
        cart.update()
        return redirect('dollshop:cart_list')
        # quantity_form = CartQuantityForm(request.POST)
        # if quantity_form.is_valid():
        #     qf = quantity_form.save(commit=False)
        #     qf.quantity = cart.quantity
        #     qf.update()
        #     return redirect('dollshop:cart_list')
    else:
        quantity_form = CartQuantityForm()


    context = {
        'cart': cart,
        'total_price': total_price,
        'quantity_form': quantity_form,

    }

    return render(request, 'dollshop1/cart.html', context)


def cart_delete(request, product_pk):
    cart = Cart.objects.get(pk=product_pk)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_add(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    cart = Cart.objects.filter(user=request.user, product=product)
    if not cart.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cart_item = cart.first()
        cart_item.quantity += 1
        cart_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
