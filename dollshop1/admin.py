from django.contrib import admin

from dollshop1.models import Category, Product, Commentary, Wishlist, Cart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'category', 'price', 'date_create']
    list_filter = ['category', 'date_create']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']



@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):

    list_display = ['user', 'date_create']
    list_filter = ['user', 'date_create']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = ['user', 'product']
    list_filter = ['user']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_filter = ['user', 'product']