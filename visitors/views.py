from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Visitor
from .forms import VisitorForm
from django.utils import timezone


@login_required
def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors/visitor_list.html', {'visitors': visitors})


@login_required
def visitor_add(request):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors:visitor_list')
    else:
        form = VisitorForm()
    return render(request, 'visitors/visitor_form.html', {'form': form})


@login_required
def visitor_edit(request, pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    visitors = get_object_or_404(Visitor, pk=pk)

    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitors)
        if form.is_valid():
            form.save()
            return redirect('visitors:visitor_list')
    else:
        form = VisitorForm(instance=visitors)
    return render(request, 'visitors/visitor_form.html', {'form': form})


@login_required
def visitor_delete(request, pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    visitors = get_object_or_404(Visitor, pk=pk)

    if request.method == 'POST':
        visitors.delete()
        return redirect('visitors:visitor_list')
    return render(request, 'visitors/visitor_confirm_delete.html', {'visitors': visitors})


from django.utils import timezone


@login_required
def visitor_checkout(request, pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    visitor = get_object_or_404(Visitor, pk=pk)

    if request.method == 'POST':
        visitor.check_out = timezone.now()
        visitor.save()
        return redirect('visitors:visitor_list')

    return render(request, 'visitors/visitor_confirm_checkout.html', {'visitor': visitor})