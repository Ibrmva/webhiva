#from rest_framework import generics
# from django.shortcuts import render, redirect
# from .models import Task
# from .serializer import TaskSerializer
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Task


# class MainAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


class MainAPIView(APIView):
    def get(self, request):
        lst = Task.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Task.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'post': model_to_dict(post_new)})




#def login(request):
    #tasks = Task.objects.all()
    #tasks = Task.objects.order_by('-id')[:5]
    #return render(request, 'main/index.html', {'title':'Home ', 'tasks': tasks})

# def index(request):
#
#     #tasks = Task.objects.all()
#
#     tasks = Task.objects.order_by('-id')[:5]
#     # return render(request, 'main/index.html', {'title': 'Home ', 'tasks': tasks})
#     return render(request, 'main/index.html', {'title': 'Home ', 'tasks': tasks})
#
#
#
# def about(request):
#     return render(request, 'main/about.html')
#
#
# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = "could "
#
#     form = TaskForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/create.html')
#
#
#
#
