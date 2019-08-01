from django.shortcuts import render, redirect
from Test.models import TestInfo


def MakeTest(request,organisationName,testName,pMarks,nMarks):
    p = 'media/Tests/' + organisationName + '/' + testName + '/' + testName + '.txt'
    file1 = open(p, 'r')
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
    return render(request, 'TestMaking/maketest.html', {'testName':testName,'quesBank': quesBank,'ans':ans,'pMarks':pMarks,'nMarks':nMarks})
    # if request.method == 'POST':
    #     messages.success(request, 'Dear student, your test is submited successfully')
    #     return redirect('TakeTest-Home')
