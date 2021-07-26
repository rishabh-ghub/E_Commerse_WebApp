from django.contrib import admin
from .models import Products,Order

# Register your models here.

admin.site.site_header = "E-Commerse Site"
admin.site.site_title = "A2Z Shopping"
admin.site.index_title = "Manage A2Z Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discount_price','category','description','image')
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)
    #fields = ('title','price')  #This makes only selected fields visible from admin
    list_editable = ('price','category',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)