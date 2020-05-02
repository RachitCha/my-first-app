from django.urls import path
from src import views

urlpatterns=[
	path('', views.index, name='index'),
	path('contact/', views.contact, name='contact'),
	path('single_page/<int:nationalnew_id>/', views.single_page, name='single_page'),
	path('page/', views.page, name='page'),
	path('national/', views.national, name='national'),
	path('state/', views.state, name='state'),
	path('district/', views.district, name='district'),
	path('city/', views.city, name='city'),
	path('front/<int:frontnew_id>/', views.front, name='front'),
	path('single_page1/<int:statenew_id>/', views.single_page1, name='single_page1'),
	path('single_page2/<int:hoshangabadnew_id>/', views.single_page2, name='single_page2'),
	path('single_page3/<int:seoninew_id>/', views.single_page3, name='single_page3'),
	path('single_page4/<int:rochaknew_id>/', views.single_page4, name='single_page4'),
]