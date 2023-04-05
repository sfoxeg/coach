from django.contrib import admin
from .models import Services, Mastermind_reg


class Services_list(admin.ModelAdmin):
    list_display = ('title', 'enable', 'price')


class Mm_reg_list(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email', 'request')


# Register your models here.
admin.site.register(Services, Services_list)
admin.site.register(Mastermind_reg, Mm_reg_list)
