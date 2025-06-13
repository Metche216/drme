from datetime import datetime, timedelta
from core.models import Appointment

def create_new_blank_appointments(interval):
    """ Create a new blank appointment """
    print("Creating new blank appointments..aaa.")
    start_time = datetime.now() + timedelta(days=5)
    start_hour = start_time.replace(hour=8, minute=0, second=0, microsecond=0)
    end_hour = start_time.replace(hour=11, minute=40, second=0, microsecond=0)
    delta = timedelta(minutes=interval)

    print('start_hour', start_hour)
    print('start_hour + delta', start_hour + delta)


    run_loop = True
    count = 10
    current = start_hour

    while run_loop:

        print('current', current)

        # if current >= end_hour:
        #     run_loop = False
        if count <= 1:
            run_loop = False
        count -= 1
        current += delta

        try:
            Appointment.objects.get(start=current)
            print(f"Appointment already exists from {current} to {current + timedelta(minutes=interval)}")

        except Appointment.DoesNotExist:
            Appointment.objects.create(
                start=current,
                end=current + timedelta(minutes=interval),
                patient="",
                cellphone="",
                email="",
            )
            print(f"Created appointment from {current} to {current + timedelta(minutes=interval)}")
