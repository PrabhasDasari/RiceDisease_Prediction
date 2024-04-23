from django.urls import path

from . import views

urlpatterns = [
			path("", views.home, name="home"),
            path("index.html", views.index, name="index"),
            path("comparison.html", views.comparison, name="comparison"),
			path('Login.html', views.Login, name="Login"), 
			path('UserLogin', views.UserLogin, name="UserLogin"),
			path('Register.html', views.Register, name="Register"),
			path('Signup', views.Signup, name="Signup"),
			path("Upload.html", views.Upload, name="Upload"),
			path('UploadImage', views.UploadImage, name="UploadImage"),
			path('Train', views.Train, name="Train"),
            path('LineGraph', views.line, name="line"),
            path('BarGraph', views.bar, name="bar"),
            path('PieChart', views.pie, name="pie"),
            path("DandS.html", views.DandS, name="DandS"),
            path("DandS1.html", views.DandS1, name="DandS1"),   
            path("about.html", views.about, name="about")       
            ]