from django.contrib import admin
from .models import Feed   # 추가
from .models import Feed, Profile   # 추가

admin.site.register(Feed)   # 추가
admin.site.register(Profile)   # 추가