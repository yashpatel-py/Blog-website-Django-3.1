from django.contrib import admin
from home.models import Contact, Counselling, faq

# Register your models here.
admin.site.register((Contact, Counselling))

@admin.register(faq)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('faq.js',)