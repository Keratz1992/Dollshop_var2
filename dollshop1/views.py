from django.shortcuts import render, redirect

from dollshop1.models import Category, Product, Commentary
from dollshop1.forms import CommentaryForm


def homepage(request):

    category = Category.objects.all()
    product = Product.objects.all()

    context = {
        'product': product,
        'category': category,
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
    }
    return render(request, 'dollshop1/product_detail.html', context)


def wishlist(request):
    return render(request, 'dollshop1/wishlist.html')