from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from accounts.decorators import login_required_json
from .models import Todo
from .forms import TodoForm

# Create your views here.

@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'todo/index.html',{"todos": todos})


@login_required_json
def set_completed_todo(request, todo_id):
    
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=todo_id, user = request.user)
            todo.is_completed = not todo.is_completed
            todo.save()
            return JsonResponse({'status': 'success', 'completed': todo.is_completed})
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@login_required_json
def delete_todo(request, todo_id):
    
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=todo_id, user = request.user)
            todo.delete()
            return JsonResponse({'status': 'success'})
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
    
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@login_required_json
def create_todo(request):
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        
        
        if form.is_valid():
            form.instance.user = request.user
            todo = form.save()
            
            return JsonResponse({'status':'success','todo_id':todo.id})
        else:
            return JsonResponse({'status':'error', 'message': form.errors}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@login_required_json
def update_todo(request, todo_id):
    
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=todo_id, user = request.user)
            
            update_form = TodoForm(request.POST or None, instance=todo)
            
            if update_form.is_valid():
                update_form.save()

                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status':'error', 'message': update_form.errors}, status=400)
 
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)