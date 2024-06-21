from django.urls import path,include
from .views import *

urlpatterns = [
   path('register/',RegisterView.as_view(),name='register_view'),
   #path('login/', LoginView.as_view(), name='login'),
   path('spam_report/',SpamReportView.as_view(),name='report_spam'),
   path('registered_users/<int:user_id>/', RegisteredUserListView.as_view(), name='registered_users_list'),
   path('search_by_name/',SearchByNameView.as_view(),name="search_by_name"),
   path('search_by_phone_number/',SearchByPhoneNumberView.as_view(),name="search_by_phone_number")
]