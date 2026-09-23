from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import StudentProfile
from hostel.models import Bed
from fees.models import Fee
from complaints.models import Complaint
from visitors.models import Visitor


@login_required
def home(request):
    total_students = StudentProfile.objects.count()
    total_beds = Bed.objects.count()
    occupied_beds = Bed.objects.filter(status=Bed.Status.OCCUPIED).count()
    available_beds = total_beds - occupied_beds
    occupancy_percent = round((occupied_beds / total_beds) * 100, 1) if total_beds > 0 else 0

    pending_fees = Fee.objects.filter(status__in=[Fee.Status.PENDING, Fee.Status.OVERDUE]).count()
    overdue_fees = Fee.objects.filter(status=Fee.Status.OVERDUE).count()
    open_complaints = Complaint.objects.exclude(status=Complaint.Status.RESOLVED).count()
    visitors_inside = Visitor.objects.filter(check_out__isnull=True).count()

    context = {
        'total_students': total_students,
        'total_beds': total_beds,
        'occupied_beds': occupied_beds,
        'available_beds': available_beds,
        'occupancy_percent': occupancy_percent,
        'pending_fees': pending_fees,
        'overdue_fees': overdue_fees,
        'open_complaints': open_complaints,
        'visitors_inside': visitors_inside,
    }
    return render(request, 'dashboard/home.html', context)