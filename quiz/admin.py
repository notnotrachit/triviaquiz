from django.contrib import admin
"""
# Register your models here.
from import_export import resources
from quiz.models import questions

class QuestionsResources(resources.ModelResource):

    class Meta:
        model = questions

from import_export.admin import ImportExportModelAdmin

class QuestionsAdm(ImportExportModelAdmin):
    resource_class = QuestionsResources
admin.site.register(questions, QuestionsAdm)
"""
