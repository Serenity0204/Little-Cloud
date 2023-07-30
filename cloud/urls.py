from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("files/", views.files_view, name="all_files"),  # For all files
    path(
        "files/imgs/", views.files_view, {"file_type": "img"}, name="img_files"
    ),  # For image files
    path(
        "files/docs/", views.files_view, {"file_type": "doc"}, name="doc_files"
    ),  # For doc files
    path(
        "files/pdfs/", views.files_view, {"file_type": "pdf"}, name="pdf_files"
    ),  # For pdf files
    path(
        "files/txts/", views.files_view, {"file_type": "txt"}, name="txt_files"
    ),  # For txt files
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
]