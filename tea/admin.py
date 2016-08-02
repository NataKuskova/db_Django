from django.contrib import admin
from tea.models import *

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'sum', 'date_order', 'user']
    date_hierarchy = 'date_order'
    list_display_links = ('id', 'date_order')
    list_editable = ('user',)
    list_filter = ('date_order',)
    # empty_value_display = 'Empty'
    # actions_on_top = True  # bottom
    # actions = ['show_data', ]

    # def show_data(self, obj):
    #     return '%s - %s' % (obj.d1, obj.d2)

    # show_data.short_description = 'Simple show field'
    # show_data.admin_order_field = 'date_order'
    fieldsets = (
        (None, {'fields': (('user', 'sum',), 'date_order')}),
        ('Advanced options', {
             'classes': ('collapse',),  # wide
             'fields': (('user', 'sum'), 'date_order'),
             'description': '<b>This is description</b>'})
        )


class ListOfOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity', 'sum']
    # date_hierarchy = 'date_order'
    list_display_links = ('id', 'order')
    # list_editable = ('user',)
    # list_filter = ('date_order',)
    # empty_value_display = 'Empty'
    # actions_on_top = True  # bottom
    # actions = ['name_method', ]

    def show_data(self, obj):
        return '%s - %s' % (obj.d1, obj.d2)
    show_data.short_description = 'Simple show field'
    show_data.admin_order_field = 'date'
    fieldsets = (
        (None, {'fields': (('order', 'product',), 'price', 'quantity', 'sum')}),
        ('Advanced options', {
             'classes': ('collapse',),  # wide
             'fields': (('order', 'product'), 'price', 'quantity', 'sum'),
             'description': '<b>This is description</b>'})
        )


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(ListOfOrder, ListOfOrderAdmin)

