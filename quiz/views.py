from django.shortcuts import render,redirect
from quiz.models import questions,scores
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'base.html',{"content": "Hello World!"})


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
                return render(request,'result.html',{"ans":questions.objects.get(number=request.POST.get('id')).answer})
            elif request.POST.get('name')=="skipped":
                stats=scores.objects.get(user=request.user)
                stats.unanswered += 1
                stats.save()
                return HttpResponse("Skipped")
            else:
                stats=scores.objects.get(user=request.user)
                stats.incorrect += 1
                stats.save()
                return HttpResponse("Wrong")

        else:
            return redirect(play)
    
    else:
        return redirect(play)
    
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'account/profile.html')
