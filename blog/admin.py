from django.contrib import admin
from blog import models


admin.register(models.Article)
admin.register(models.Category)
admin.register(models.Tags)
