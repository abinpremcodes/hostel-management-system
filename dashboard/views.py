
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.timezone import localdate

from accounts.models import StudentProfile
from hostel.models import Bed
from fees.models import Fee
from complaints.models import Complaint
from visitors.models import Visitor
from events.models import Event


@login_required
def home(request):

    # Student Dashboard
    if request.user.is_student:
        return student_dashboard(request)

    # Hostel Statistics
    total_students = StudentProfile.objects.count()

    total_beds = Bed.objects.count()

    occupied_beds = Bed.objects.filter(
        status=Bed.Status.OCCUPIED
    ).count()

    available_beds = total_beds - occupied_beds

    occupancy_percent = (
        round((occupied_beds / total_beds) * 100, 1)
        if total_beds > 0
        else 0
    )

    # Fee Statistics
    paid_fees = Fee.objects.filter(
        status=Fee.Status.PAID
    ).count()

    pending_fees = Fee.objects.filter(
        status=Fee.Status.PENDING
    ).count()

    overdue_fees = Fee.objects.filter(
        status=Fee.Status.OVERDUE
    ).count()

    # Complaint Statistics
    pending_complaints = Complaint.objects.filter(
        status=Complaint.Status.PENDING
    ).count()

    in_progress_complaints = Complaint.objects.filter(
        status=Complaint.Status.IN_PROGRESS
    ).count()

    resolved_complaints = Complaint.objects.filter(
        status=Complaint.Status.RESOLVED
    ).count()

    open_complaints = (
        pending_complaints +
        in_progress_complaints
    )

    # Visitor Statistics
    visitors_inside = Visitor.objects.filter(
        check_out__isnull=True
    ).count()

    # Dashboard Context
    context = {
        "total_students": total_students,

        "total_beds": total_beds,
        "occupied_beds": occupied_beds,
        "available_beds": available_beds,
        "occupancy_percent": occupancy_percent,

        "paid_fees": paid_fees,
        "pending_fees": pending_fees,
        "overdue_fees": overdue_fees,

        "pending_complaints": pending_complaints,
        "in_progress_complaints": in_progress_complaints,
        "resolved_complaints": resolved_complaints,
        "open_complaints": open_complaints,

        "visitors_inside": visitors_inside,
    }

    return render(
        request,
        "dashboard/home.html",
        context
    )


def student_dashboard(request):

    student = request.user.student_profile

    active_allocation = student.allocations.filter(
        status="ACTIVE"
    ).first()

    pending_fees = student.fees.exclude(
        status="PAID"
    ).count()

    open_complaints = student.complaints.exclude(
        status="RESOLVED"
    ).count()

    # Upcoming Events
    upcoming_events = Event.objects.filter(
        date__gte=localdate()
    ).order_by("date", "time")

    context = {
        "student": student,
        "active_allocation": active_allocation,
        "pending_fees": pending_fees,
        "open_complaints": open_complaints,
        "upcoming_events": upcoming_events,
    }

    return render(
        request,
        "dashboard/student_home.html",
        context
    )
