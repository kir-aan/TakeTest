from django.shortcuts import render, redirect
from Test.models import TestInfo


def MakeTest(request):
    if "startbtn" in request.POST:
        # currentStudent = request.user
        currentTestObj = TestInfo.objects.get(InputTextFile=request.POST['f_name'])
        path = 'media/'+request.POST['f_name']
        file1 = open(path, 'r')
        lines = file1.readlines()
        file1.close()
        ques = []
        options = []
        ans = []
        for line in lines:
            if "Q:" in line:
                ques.append(line)
            if "opt" in line:
                options.append(line.replace('*', ''))
            if "*" in line:
                ans.append(line.replace('*', '')[:-1])
        i = 0
        quesBank = {}
        for qu in ques:
            quesBank[qu] = [options[x] for x in range(i, i + 4)]
            i = i + 4
        return render(request, 'TestMaking/maketest.html', {'qlength':len(quesBank),'testName':currentTestObj.TestName,'quesBank': quesBank,'ans':ans,'pMarks':currentTestObj.PosMarks,'nMarks':currentTestObj.NegMarks})

def TestSubmit(request):
    if "submitbtn" in request.POST:
        selectedAnswers = []
        print(request.POST['qlength'])
        print(request.POST.get('chosenAnswers',True))
    return render(request,'TestMaking/completed.html')
