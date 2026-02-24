from django.shortcuts import render
import datetime

def home(request):
    return render(request, "home.html")

def tasks(request):
    return render(request, "tasks.html")

def time(request, offset):
    offset = int(offset)

    curr_time = datetime.datetime.now()

    past = curr_time - datetime.timedelta(hours=offset)
    future = curr_time + datetime.timedelta(hours=offset)

    return render(
        request,
        "time.html",
        context={
            "past_time": past,
            "future_time": future,
            "current_time": curr_time,
            "offset": offset,
        },
    )