from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Result)
admin.site.register(Admin)
admin.site.register(Staff)