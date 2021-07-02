from django.contrib import admin
from .models import Listing
from .models import User
# Register your models here.
admin.site.register(Listing)
admin.site.register(User)
