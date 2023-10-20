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
    path("view-share/<str:short_url>/", views.view_share_view, name="view_share"),
    path("share/<int:pk>/", views.share_file_view, name="share_file"),
    path("upload/", views.upload_view, name="upload"),
    path("delete/<int:pk>/", views.delete_file_view, name="delete_file"),
    path("search/", views.search_view, name="search"),
    path("my-urls/", views.my_urls_view, name="my_urls"),
    path("delete-my-url/<int:pk>/", views.delete_my_url_view, name="delete_my_url"),
    path("share-others/", views.share_others_view, name="share_others"),
]
