from django.db import models
from django.contrib import admin
# Create your models here.
from django.contrib.auth.models import User

class questions(models.Model):
    number=models.IntegerField()
    question= models.CharField(max_length=50)
    option1=models.CharField(max_length=50)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)

    def __str__(self):
        return ': '.join([str(self.number), str(self.question)])

    class Meta:
        verbose_name_plural = "Question"

class questionsAdmin(admin.ModelAdmin):
    #readonly_fields = ('')
    list_filter = ('number',)

class scores(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    correct=models.IntegerField(default=0)
    incorrect=models.IntegerField(default=0)
    unanswered=models.IntegerField(default=0)

    def __str__(self):
        return ': '.join([self.user.username, str(self.correct)])

    class Meta:
        verbose_name_plural = "Score"

class scoresAdmin(admin.ModelAdmin):
    #readonly_fields = ('')
    list_filter = ('user',)
    list_display = ['user', 'correct', 'incorrect','unanswered']

admin.site.register(questions,questionsAdmin)
admin.site.register(scores,scoresAdmin)
