from django.urls import path

from productData.views import product_views as views


urlpatterns=[
    

     path('', views.GetProducts.as_view()),

     path('create/',views.CreateProducts.as_view()),
   
     path('<str:pk>/', views.GetProduct.as_view()),

     path('<int:pk>/update/', views.UpdateProduct.as_view(), name='update_product'),  # Optionally separate for update

     path('<int:pk>/delete/', views.DeleteProduct.as_view(), name='delete_product'),  # Optionally separate for delete

]