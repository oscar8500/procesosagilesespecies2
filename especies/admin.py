from django.contrib import admin
from .models import Comment
from .models import Specie
from .models import UserProfile
from .models import Category


# Register your models here.
admin.site.register(Comment)
admin.site.register(Specie)
admin.site.register(UserProfile)
admin.site.register(Category)
