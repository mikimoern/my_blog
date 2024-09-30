from datetime import datetime
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Main Page",
    }
    return render(request, "index.html", context)


def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "Page that will only contain articles on topics that the user is subscribed to!"
    )


def article(request: HttpRequest, article_id: int) -> HttpResponse:
    context = {
        "title": "Detail Page",
    }
    return render(request, "detail_page.html", context)


def add_comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is comment for article #{article_id}.")


def update_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is page for update this article #{article_id}.")


def delete_article(request: HttpRequest, article_id: int) -> HttpResponse:
    context = {
        "title": "Delete Page",
    }
    return render(request, "delete_news.html", context)


def create_article(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Create Page",
    }
    return render(request, "add_news.html", context)


def all_topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is page for all topics")


def articles_by_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("Page with all the articles on a particular topic")


def subscribe_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("Address for subscribing to a specific topic")


def unsubscribe_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("Address for unsubscribing from a specific topic")


def profile(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Profile Page",
    }
    return render(request, "profile.html", context)


def register(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Register Page",
    }
    return render(request, "register.html", context)


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page with the password change")


def login_view(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Login Page",
    }
    return render(request, "login.html", context)


def logout_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Address to exit the site")


def articles_by_month(request: HttpRequest, year: int, month: int) -> HttpResponse:
    try:
        year = int(year)
        month = int(month)
    except ValueError:
        raise Http404("Incorrect date format")

    if month < 1 or month > 12:
        raise Http404("Incorrect month")

    current_date = datetime.now()

    if year > current_date.year or (
        year == current_date.year and month > current_date.month
    ):
        return HttpResponse(f"No articles for {year}/{month}")

    return HttpResponse(f"Articles for {year}/{month}.")
