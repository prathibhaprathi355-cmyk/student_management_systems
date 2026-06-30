from django.urls import path
from . import views
urlpatterns = [
    # read
    path('',views.displayDetails , name='home'),
    path('detail/<int:id>/' , views.one_student_details , name='detail'
    ),

    # create 
    path('create/', views.create_student, name='create'),
    path('update/<int:id>' ,views.update_student_view, name='update'),
    path('student-delete/<int:id>',views.delete_student , name='delete'
         ),

]