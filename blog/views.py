from datetime import datetime
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpRequest

from .models import Topic, Article
from .forms import ArticleAddForm, LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    topics = Topic.objects.all()
    articles = Article.objects.all()
    context = {"title": "Main Page", "topics": topics, "articles": articles}
    return render(request, "index.html", context)


def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "Page that will only contain articles on topics that the user is subscribed to!"
    )


def article(request: HttpRequest, article_id: int) -> HttpResponse:
    article = Article.objects.get(pk=article_id)
    context = {"title": "Detail Page", "article": article}
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
    if request.method == "POST":
        form = ArticleAddForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            article.save()
            messages.success(request, "You have successfully created an article")
            return redirect("article", article.pk)
    else:
        form = ArticleAddForm()

    context = {"title": "Create Page", "form": form}
    return render(request, "add_news.html", context)


def all_topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is page for all topics")


def articles_by_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    articles = Article.objects.filter(topics_id=topic_id)
    topics = Topic.objects.all()
    context = {"title": articles[0].topics, "topics": topics, "articles": articles}
    return render(request, "index.html", context)


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
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered an account")
            return redirect("login_view")
    else:
        form = RegistrationForm()

    context = {"title": "Register Page", "form": form}
    return render(request, "register.html", context)


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The page with the password change")


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged into your account")
            return redirect("index")
    else:
        form = LoginForm()

    context = {"title": "Login Page", "form": form}
    return render(request, "login.html", context)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("index")


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
