from django.db import models
from django.contrib import admin
# Create your models here.
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

from import_export import resources
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class questions(models.Model):
    number=models.IntegerField()
    question= models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    option1=models.CharField(max_length=50)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)
    answer=models.CharField(max_length=50)

    def __str__(self):
        return ': '.join([str(self.number), str(self.question)])

    class Meta:
        verbose_name_plural = "Question"

class QuestionResources(resources.ModelResource):
    class Meta:
        model = questions

class questionsAdmin(ImportExportModelAdmin):
    #readonly_fields = ('')
    list_filter = ('category',)
    list_display = ['number','question', 'category']
    resource_class = QuestionResources

class scores(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    correct=models.IntegerField(default=0)
    incorrect=models.IntegerField(default=0)
    unanswered=models.IntegerField(default=0)
    q_attempted=models.CharField(default="[]",max_length=99999)

    def __str__(self):
        return ': '.join([self.user.username, str(self.correct)])

    class Meta:
        verbose_name_plural = "Stats"

class scoresAdmin(admin.ModelAdmin):
    #readonly_fields = ('user',)
    list_filter = ('user',)
    list_display = ['user', 'correct', 'incorrect','unanswered']


@receiver(user_signed_up)
def create_user_profile(sender, user, **kwargs):
    scores.objects.create(user=user)



admin.site.register(questions,questionsAdmin)
admin.site.register(scores,scoresAdmin)
