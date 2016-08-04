from django.contrib import admin
from datetime import date
from tea.models import *


class ListOfOrderInline(admin.TabularInline):
    model = ListOfOrder
    extra = 1
    raw_id_fields = ("product",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (ListOfOrderInline,)
    list_display = ['id', 'user', 'sum', 'date_order']
    list_display_links = ('id', 'user')
    date_hierarchy = 'date_order'
    list_filter = ('date_order',)
    list_per_page = 10
    search_fields = ('user__name','user__surname', 'sum',)

    """
    fieldsets = (
        (None, {'fields': (('user', 'sum',), 'date_order')}),
        ('Advanced options', {
             'classes': ('collapse',),  # wide
             'fields': (('user', 'sum'), 'date_order'),
             'description': '<b>This is description</b>'})
        )
    """


class ProductAdmin(admin.ModelAdmin):
    inlines = (ListOfOrderInline,)
    list_display = ['id', 'name', 'category', 'price', 'quantity', 'photo',
                    'user']
    list_display_links = ('id', 'name')
    list_filter = ('category', 'user',)
    search_fields = ('name', 'price', 'quantity', 'category__name')
    list_per_page = 10


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email']
    list_display_links = ('id', 'name', 'surname')
    fields = (('name', 'surname'), 'email', 'phone', 'address')
    list_per_page = 10
    search_fields = ('name', 'surname', 'email', 'phone', 'address',)

"""
class DecadeBornListFilter(admin.SimpleListFilter):
    title = 'decade born'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        # return [('90s', 'in 90s'), ('80s', 'in 80s')]
        qs = model_admin.get_queryset(request)
        if qs.filter(date_order__gte == date(1980, 1, 1),
                     date_order__lte == date(1989, 12, 31)).exists():
            yield('80s', 'in 80')

    def queryset(self, request, queryset):
        if self.value == '80s':
            return queryset.filter(date_order__gte == date(1980, 1, 1),
                                   date_order__lte == date(1989, 12, 31))
"""


admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Buyer, BuyerAdmin)

