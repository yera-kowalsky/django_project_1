from django.urls import path
from myapp.views import index,indexItem

app_name = "myapp"

urlpatterns = [
   # http://localhost:8000/myapp/
    path('', index),
    # http://localhost:8000/myapp/hello/
     path('<int:my_id>/', indexItem, name="detail")
]
  
