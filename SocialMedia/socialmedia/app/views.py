from django.shortcuts import redirect, render

from .models import AddDay
from .forms import AddDayForm
# Create your views here.
def home(request):
  addDay= AddDay.objects.all()
  return render(request,'html/index.html',{'addDay':addDay})

def StoryForm(request):
  if request.method == 'POST':
    form = AddDayForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = AddDayForm()
  return render(request, 'html/modal.html',{'form':form})
