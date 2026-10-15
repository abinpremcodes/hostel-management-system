from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm
from .models import Event


def is_admin_or_warden(user):
    return (
        user.is_authenticated
        and (user.is_admin or user.is_warden)
    )


@login_required
def event_list(request):
    events = Event.objects.all().order_by("date", "time")
    return render(
        request,
        "events/event_list.html",
        {"events": events},
    )


@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(
        request,
        "events/event_detail.html",
        {"event": event},
    )


@login_required
@user_passes_test(is_admin_or_warden)
def manage_events(request):
    events = Event.objects.all().order_by("-date", "-time")
    return render(
        request,
        "events/manage_events.html",
        {"events": events},
    )


@login_required
@user_passes_test(is_admin_or_warden)
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully.")
            return redirect("events:manage_events")
    else:
        form = EventForm()

    return render(
        request,
        "events/event_form.html",
        {"form": form, "page_title": "Add Event"},
    )


@login_required
@user_passes_test(is_admin_or_warden)
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect("events:manage_events")
    else:
        form = EventForm(instance=event)

    return render(
        request,
        "events/event_form.html",
        {
            "form": form,
            "page_title": "Edit Event",
            "event": event,
        },
    )


@login_required
@user_passes_test(is_admin_or_warden)
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect("events:manage_events")

    return render(
        request,
        "events/event_confirm_delete.html",
        {"event": event},
    )