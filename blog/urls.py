from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", main, name="main"),
    path("my-feed/", my_feed, name="my_feed"),
    path("<int:article_id>/", article, name="article"),
    path("<int:article_id>/comment/", add_comment, name="add_comment"),
    path("<int:article_id>/update/", update_article, name="update_article"),
    path("<int:article_id>/delete/", delete_article, name="delete_article"),
    path("create/", create_article, name="create_article"),
    path("topics/", all_topics, name="all_topics"),
    path("topics/<int:topic_id>/", articles_by_topic, name="articles_by_topic"),
    path("topics/<int:topic_id>/subscribe/", subscribe_topic, name="subscribe_topic"),
    path(
        "topics/<int:topic_id>/unsubscribe/",
        unsubscribe_topic,
        name="unsubscribe_topic",
    ),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path("set-password/", set_password, name="set_password"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    re_path(
        r"^(?P<year>\d{4})/(?P<month>\d{2})/$",
        articles_by_month,
        name="articles_by_month",
    ),
]
