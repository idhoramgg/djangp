from django.shortcuts import render
# from django.http import HttpResponse
from appTwo.models import Topic,Webpage,AccessRecord, User
# from appTwo.models import User
from appTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')


def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'appTwo/users.html', {"form": form})
    # user_list = User.objects.order_by('name')
    # user_dict = {"user": user_list}
    # return render(request, 'appTwo/signup.html', context=user_dict)