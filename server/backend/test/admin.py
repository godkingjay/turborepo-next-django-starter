from django.contrib import admin

from .models import Test, TestReference


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "middle_name", "age")
    list_filter = ("first_name", "last_name", "age")
    search_fields = ("first_name", "last_name", "middle_name")


@admin.register(TestReference)
class TestReferenceAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "image", "author")
    list_filter = ("title", "author")
    search_fields = ("title", "author")
