# from django.contrib.auth import views as auth_views
# from django.urls import path
# from .import views


# app_name='accounts'

# urlpatterns = [

#     path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
#     path('students/',views.student_list,name='student_list'),
#     path('students/add',views.student_add,name='student_add'),
#     path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
#     path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
#     path('my-fees/', views.my_fees, name='my_fees'),
#      path('my-complaints/', views.my_complaints, name='my_complaints'),
    


# ]

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [

    # Login / Logout
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="accounts:login"
        ),
        name="logout"
    ),

    # Password Reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt",
            success_url="/accounts/password-reset/done/"
        ),
        name="password_reset"
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done"
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/accounts/reset/done/"
        ),
        name="password_reset_confirm"
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),


    # Student Management
    path(
        "students/",
        views.student_list,
        name="student_list"
    ),

    path(
        "students/add/",
        views.student_add,
        name="student_add"
    ),

    path(
        "students/<int:pk>/edit/",
        views.student_edit,
        name="student_edit"
    ),

    path(
        "students/<int:pk>/delete/",
        views.student_delete,
        name="student_delete"
    ),


    # Student Dashboard
    path(
        "my-fees/",
        views.my_fees,
        name="my_fees"
    ),

    path(
        "my-complaints/",
        views.my_complaints,
        name="my_complaints"
    ),
]