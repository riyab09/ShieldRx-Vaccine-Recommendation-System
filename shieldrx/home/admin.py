from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import MyModel


class MyModelResource(resources.ModelResource):
    class Meta:
        model = MyModel

class MyModelAdmin(ImportExportModelAdmin):
    resource_class = MyModelResource

admin.site.register(MyModel, MyModelAdmin)

