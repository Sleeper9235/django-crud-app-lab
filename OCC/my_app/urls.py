from django.urls import path
from . import views 




urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('groups/', views.group_index, name='group-index'),
    path('groups/<int:group_id>', views.group_detail, name='group-detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='group-create'),
    path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='group-update'),
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='group-delete'),
    path('groups/<int:group_id>/add-thread/', views.add_thread, name="add-thread"),
    path('accounts/signup/', views.signup, name='signup'),
    path('thread/<int:id>/update/', views.thread_update, name='thread-update'),
    path('thread/<int:pk>/delete/', views.ThreadDelete.as_view(), name='thread-delete'),
]