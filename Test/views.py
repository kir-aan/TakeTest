from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestForm
from .models import TestInfo
from django.contrib.auth.models import User


@login_required
def post(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            fulltest = form.save(commit=False)
            fulltest.user = request.user
            fulltest.Uploader_info = request.user
            TestName = form.cleaned_data.get('TestName')
            File = form.cleaned_data.get('InputTextFile')
            fulltest.save()
            messages.success(request, 'Test {} Posted successfully'.format(TestName))
            return redirect('TakeTest-Home')
        else:
            parameters = {
              'form': form,
              'error': form.errors.as_ul()
            }
            return render(request, 'Test/post.html', parameters)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()
        return render(request, 'Test/post.html', {'form': form})
