from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reminder
from .forms import ReminderForm

# Create your views here.
@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminder/reminder_list.html', {'reminders':reminders})

@login_required
def reminder_detail(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    return render(request, 'reminder/reminder_detail.html', {'reminder': reminder})

@login_required
def reminder_create(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminders:reminder_details')
        else:
            form = ReminderForm()
            
        return render(request, 'reminder/create_reminder.html', {'form':form})
    
@login_required
def reminder_edit(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminders:reminder_detail', reminder_id=reminder.id)
        else:
            form = ReminderForm(instance=reminder)
        return render(request, 'reminder/create_reminder.html', {'form': form})
    
@login_required
def reminder_delete(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders:reminder_list')
    return render(request, 'reminder/reminder_confirm_delete.html', {'reminder':reminder})