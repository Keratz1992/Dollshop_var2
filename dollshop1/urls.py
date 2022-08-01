
from django.urls import path

from dollshop1.views import homepage, category_list, product_detail, wishlist, \
    wishlist_add, wishlist_delete, cart_list, cart_delete, cart_add


app_name = 'dollshop'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('product_detail/<int:get_pk>/', product_detail, name='product_detail'),
    path('wishlist/', wishlist, name='wishlist'),
    path('category/<int:cate_pk>/', category_list, name='category_list'),
    path('cart_list/', cart_list, name='cart_list'),
    path('wishlist_add/<int:product_pk>/', wishlist_add, name='wishlist_add'),
    path('wishlist_delete/<int:product_pk>/', wishlist_delete, name='wishlist_delete'),
    path('cart_delete/<int:product_pk>', cart_delete, name='cart_delete'),
    path('cart_add/<int:product_pk>', cart_add, name='cart_add')

    ]