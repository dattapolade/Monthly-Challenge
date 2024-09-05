from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Start the year strong: Try a to learn new thing each day",
    "february": "Boost your fitness: Walk or run for at least 30 minutes every day!",
    "march": "Sharpen your skills: learn any skills that give you money",
    "april": "Spring into action: Try a new outdoor activity every weekend!",
    "may": "Mindful moments: Practice meditation for 10 minutes daily!",
    "june": "Expand your knowledge: Explore a new tech framework or language weekly!",
    "july": "Embrace the summer: Go on a nature hike or spend time in the sun daily!",
    "august": "Stay active: Try a new form of exercise like yoga, swimming, or cycling!",
    "september": "Tech growth: Work on a side project or learn advanced Django topics!",
    "october": "Challenge yourself: Participate in a local event or community project!",
    "november": "Gratitude month: Write down one thing you're thankful for each day!",
    "december": "Finish strong: Set weekly goals to complete any unfinished projects!"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

