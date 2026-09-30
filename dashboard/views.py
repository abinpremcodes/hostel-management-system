from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import StudentProfile
from hostel.models import Bed
from fees.models import Fee
from complaints.models import Complaint
from visitors.models import Visitor


@login_required
def home(request):

    # ----------------------------------------
    # STUDENT DASHBOARD
    # ----------------------------------------
    if request.user.is_student:
        return student_dashboard(request)

    # ----------------------------------------
    # HOSTEL STATISTICS
    # ----------------------------------------

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

    # ----------------------------------------
    # FEE STATISTICS
    # ----------------------------------------

    paid_fees = Fee.objects.filter(
        status=Fee.Status.PAID
    ).count()

    pending_fees = Fee.objects.filter(
        status=Fee.Status.PENDING
    ).count()

    overdue_fees = Fee.objects.filter(
        status=Fee.Status.OVERDUE
    ).count()

    # ----------------------------------------
    # COMPLAINT STATISTICS
    # ----------------------------------------

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

    # ----------------------------------------
    # VISITOR STATISTICS
    # ----------------------------------------

    visitors_inside = Visitor.objects.filter(
        check_out__isnull=True
    ).count()

    # ----------------------------------------
    # CONTEXT
    # ----------------------------------------

    context = {
        # Students
        "total_students": total_students,

        # Beds
        "total_beds": total_beds,
        "occupied_beds": occupied_beds,
        "available_beds": available_beds,
        "occupancy_percent": occupancy_percent,

        # Fees
        "paid_fees": paid_fees,
        "pending_fees": pending_fees,
        "overdue_fees": overdue_fees,

        # Complaints
        "pending_complaints": pending_complaints,
        "in_progress_complaints": in_progress_complaints,
        "resolved_complaints": resolved_complaints,
        "open_complaints": open_complaints,

        # Visitors
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

    context = {
        "student": student,
        "active_allocation": active_allocation,
        "pending_fees": pending_fees,
        "open_complaints": open_complaints,
    }

    return render(
        request,
        "dashboard/student_home.html",
        context
    )