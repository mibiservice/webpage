from django.urls import path
from . import views
urlpatterns = [
	path('recruiter/', views.register_recruiter, name="reg_recruiter"),
	path('partner/', views.register_partner, name="reg_partner"),
	path('worker/', views.register_worker, name="reg_worker"),
	path('pricing/', views.pricing, name = "pricing"),
	path('forms/', views.forms, name = 'forms'),
	path('price_worker/', views.price_worker, name = "price_worker"),
	path('about_us/', views.about_us, name = "about_us"),
	path('contact_us/', views.contact_us, name = "contact_us"),
	path('partners/', views.partners, name = "partners"),
	path('', views.index, name = "index"),
	path('join_us/', views.join_us, name = "join_us"),
]
