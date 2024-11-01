from django.urls import path
from myapp.views import index,indexItem,add_item, update_item, delete_item

app_name = "myapp"

urlpatterns = [
   # http://localhost:8000/myapp/
   path('', index,name="index"),
    # http://localhost:8000/myapp/hello/
   path('<int:my_id>/', indexItem, name="detail"),
   path('additem/', add_item, name="add_item"),
   path('updateitem/<int:my_id>', update_item, name="update_item"),
   path('deleteitem/<int:my_id>', delete_item, name="delete_item"),
]
  
