from django.shortcuts import render,redirect
from quiz.models import questions,scores
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.views.generic.edit import FormView

from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
import hashlib





def index(request):
    return render(request,'home.html')


@login_required(login_url='/accounts/login/')
def play(request):
    stats=scores.objects.get(user=request.user)
    qa_list=json.loads(stats.q_attempted)
    if len(questions.objects.exclude(number__in=qa_list).order_by('?'))>0:
        x = questions.objects.exclude(number__in=qa_list).order_by('?')[0]
        #context={"content"=x.question}
        
        return render(request,'question.html',{"question":x.question ,"category":x.category, "option1":x.option1,"option2":x.option2,"option3":x.option3,"option4":x.option4,'id':x.number})
    else:
        return render(request,'question.html',{"question":"You have played all questions"})

@login_required(login_url='/accounts/login/')
def check(request):
    if request.method=="POST":
        stats=scores.objects.get(user=request.user)
        qa_list=json.loads(stats.q_attempted)
        #print (qa_list)
        if int(request.POST.get('id')) not in qa_list:

            stats=scores.objects.get(user=request.user)
            qa_list=json.loads(stats.q_attempted)

            qa_list.append(int(request.POST.get('id')))

            stats.q_attempted=json.dumps(qa_list)
            stats.save()
            if request.POST.get('name') == questions.objects.get(number=request.POST.get('id')).answer:
                stats=scores.objects.get(user=request.user)
                stats.correct += 1
                stats.save()
                return render(request,'result.html',{ "correct":'True',"ans":questions.objects.get(number=request.POST.get('id')).answer})
            elif request.POST.get('name')=="Skip":
                stats=scores.objects.get(user=request.user)
                stats.unanswered += 1
                stats.save()
                return render(request,'result.html',{"skip":"True","ans":questions.objects.get(number=request.POST.get('id')).answer})
            else:
                stats=scores.objects.get(user=request.user)
                stats.incorrect += 1
                stats.save()
                return render(request,'result.html',{"incorrect":"True","ans":questions.objects.get(number=request.POST.get('id')).answer})

        else:
            return redirect(play)
    
    else:
        return redirect(play)
    
@login_required(login_url='/accounts/login/')
def profile(request):
    k=SocialAccount.objects.filter(user=request.user)
    disc=False
    ggl=False
    for i in k:
        if i.provider == "discord":
            disc=True
        elif i.provider == "google":
            ggl=True

    h=hashlib.md5(request.user.email.encode('utf-8')).hexdigest()
    if len(k)>0:
        g_url=k[0].get_avatar_url()
    else:
        g_url=f"http://www.gravatar.com/avatar/{h}?d=https://i.imgur.com/Srg5ywH.jpg"
    
    stats=scores.objects.get(user=request.user)
    return render(request,'account/profile.html',{"url":g_url,"USERNAME":request.user.username,"cor_ans":stats.correct,"incor_ans":stats.incorrect,"unans":stats.unanswered,"sa":k,"disc":disc,"ggl":ggl})


@login_required(login_url='/accounts/login/')
def accounts(request):
    return render(request,'account/base.html')

@login_required(login_url='/accounts/login/')
def conredirect(request):
    return redirect(profile)

def category(request):
    return render(request,'comingsoon.html')

def about(request):
    return render(request,'about.html')
