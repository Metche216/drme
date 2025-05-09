from django.shortcuts import render

def list_appointments(request):

    appointments = [
        {"id": 1, "date": "2023-10-01", "time": "10:00 AM", "patient": "John Doe"},
        {"id": 2, "date": "2023-10-02", "time": "11:00 AM", "patient": "Jane Smith"},
    ]

    return render(request, 'appointments/appointments.html', {'appointments': appointments})