from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from rangefilter.filter import DateRangeFilter
from .models import *


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerProfile._meta.fields]  # Все поля модели
    search_fields = ['surname', 'name', 'patronymic']
    list_filter = (
        ('create_date', DateRangeFilter),
        ('modify_date', DateRangeFilter),
    )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Offer._meta.fields]  # Все поля модели
    search_fields = ['name']
    list_filter = (
        ('create_date', DateRangeFilter),
        ('modify_date', DateRangeFilter),
    )


@admin.register(Request2co)
class Request2coAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Request2co._meta.fields]  # Все поля модели
    search_fields = []
    list_filter = ('status', ('create_date', DateRangeFilter),)


class UserAdmin(UserAdmin):
    """
    Переопределенный класс UserAdmin
    """
    def save_model(self, request, obj, form, change):
        """
        После создания пользователя, генерируем для него токен
        """
        super(UserAdmin, self).save_model(request, obj, form, change)
        Token.objects.get_or_create(user=obj)

    def token(self, user):
        return Token.objects.get(user=user)

    def group(self, user):
        return user.groups.get()

    def get_list_display(self, request):
        """ Расширяем список отоброжаемых полей в аминке еще двумя полями """
        list_display = list(super(UserAdmin, self).get_list_display(request))
        list_display.insert(1, 'token')
        list_display.insert(2, 'group')
        return list_display

admin.site.unregister(User)
admin.site.unregister(Token)
admin.site.register(User, UserAdmin)