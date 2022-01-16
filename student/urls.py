from django.contrib import admin  
from django.urls import path  
from . import views  
urlpatterns = [  
    #path('admin/', admin.site.urls),  
    path('',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('emp', views.emp,name='emp'),  
    path('show',views.show,name='home'),  
    path('edit/<int:id>', views.edit,name='edit'),  
    path('update/<int:id>', views.update,name='update'),  
    path('delete/<int:id>', views.destroy,name='delete'),  
]  