from django.shortcuts import render
from src.models import NationalNew,StateNew,HoshangabadNew,SeoniNew,FrontNew,RochakNew,TopNew
from datetime import datetime

# Create your views here.
def index(request):
	topnews_all = TopNew.objects.all()
	frontnews_all = FrontNew.objects.all()
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	nationalfront = NationalNew.objects.get(want_this_news_as_front_news = True)
	nationalsection_all = NationalNew.objects.filter(want_this_news_in_national_news_section = True)
	statefront = StateNew.objects.get(want_this_news_as_front_news = True)
	statesection_all = StateNew.objects.filter(want_this_news_in_state_news_section = True)
	districtfront = HoshangabadNew.objects.get(want_this_news_as_front_news = True)
	districtsection_all = HoshangabadNew.objects.filter(want_this_news_in_hoshangabad_news_section = True)
	cityfront = SeoniNew.objects.get(want_this_news_as_front_news = True)
	citysection_all = SeoniNew.objects.filter(want_this_news_in_seoni_news_section = True)
	rochaknews_all = RochakNew.objects.all()
	mydate = datetime.now()
	return render(request, 'index.html',{'topnews_all':topnews_all,'frontnews_all':frontnews_all,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'nationalfront':nationalfront,'nationalsection_all':nationalsection_all,'statefront':statefront,'statesection_all':statesection_all,'districtfront':districtfront,'districtsection_all':districtsection_all,'cityfront':cityfront,'citysection_all':citysection_all,'rochaknews_all':rochaknews_all,'mydate':mydate})

def contact(request):
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	topnews_all = TopNew.objects.all()
	mydate = datetime.now()
	return render(request, 'contact.html',{'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'topnews_all':topnews_all,'mydate':mydate})

def single_page(request,nationalnew_id):
	topnews_all = TopNew.objects.all()
	national_news = NationalNew.objects.get(pk=nationalnew_id)
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	nationalsection_all = NationalNew.objects.filter(want_this_news_in_national_news_section = True)
	mydate = datetime.now()
	return render(request, 'single_page.html',{'topnews_all':topnews_all,'national_news':national_news,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'nationalsection_all':nationalsection_all,'mydate':mydate})

def page(request):
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	topnews_all = TopNew.objects.all()
	mydate = datetime.now()
	return render(request, 'page.html',{'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'topnews_all':topnews_all,'mydate':mydate})

def national(request):
	topnews_all = TopNew.objects.all()
	news_all = NationalNew.objects.all()
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'national.html',{'topnews_all':topnews_all,'news_all':news_all,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def state(request):
	topnews_all = TopNew.objects.all()
	news_all = StateNew.objects.all()
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'state.html',{'topnews_all':topnews_all,'news_all':news_all,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def district(request):
	topnews_all = TopNew.objects.all()
	news_all = HoshangabadNew.objects.all()
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'district.html',{'topnews_all':topnews_all,'news_all':news_all,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def city(request):
	topnews_all = TopNew.objects.all()
	news_all = SeoniNew.objects.all()
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'city.html',{'topnews_all':topnews_all,'news_all':news_all,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def front(request,frontnew_id):
	topnews_all = TopNew.objects.all()
	front_news = FrontNew.objects.get(pk=frontnew_id)
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'front.html',{'topnews_all':topnews_all,'front_news':front_news,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def single_page1(request,statenew_id):
	topnews_all = TopNew.objects.all()
	state_news = StateNew.objects.get(pk=statenew_id)
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'single_page1.html',{'topnews_all':topnews_all,'state_news':state_news,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def single_page2(request,hoshangabadnew_id):
	topnews_all = TopNew.objects.all()
	district_news = HoshangabadNew.objects.get(pk=hoshangabadnew_id)
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'single_page2.html',{'topnews_all':topnews_all,'district_news':district_news,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def single_page3(request,seoninew_id):
	topnews_all = TopNew.objects.all()
	city_news = SeoniNew.objects.get(pk=seoninew_id)
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'single_page3.html',{'topnews_all':topnews_all,'city_news':city_news,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})

def single_page4(request,rochaknew_id):
	topnews_all = TopNew.objects.all()
	rochak_news = RochakNew.objects.get(pk=rochaknew_id)
	nationalmain_all = NationalNew.objects.filter(want_this_news_as_main_news = True)
	statemain_all = StateNew.objects.filter(want_this_news_as_main_news = True)
	districtmain_all = HoshangabadNew.objects.filter(want_this_news_as_main_news = True)
	citymain_all = SeoniNew.objects.filter(want_this_news_as_main_news = True)
	mydate = datetime.now()
	return render(request, 'single_page4.html',{'topnews_all':topnews_all,'rochak_news':rochak_news,'nationalmain_all':nationalmain_all,'statemain_all':statemain_all,'districtmain_all':districtmain_all,'citymain_all':citymain_all,'mydate':mydate})
