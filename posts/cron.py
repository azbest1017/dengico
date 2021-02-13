import requests, json
from .models import Post, Affiliate_Partner
from datetime import date

def api_call_leadSU():
	all_mfo = Post.objects.all()
	all_mfo = all_mfo.filter(offer_want=True)
	today = date.today()
	for i in all_mfo:
	    offer_id = str(i.offer_id)
	    account = i.partner.all()
	    api_key = ""
	    for z in account:
        	api_key = z.api_key
	    url = "https://api.leads.su/webmaster/offers/" + offer_id + "/?token=" + api_key
	    r = requests.get(url)
	    data = r.json()
	    status = data["count"]
	    if status == "1":
	        i.offer_status = True
	        i.save()
	    elif status == "0":
	        i.offer_status = False
	        i.save()
	    else:
	        i.offer_status = False
	        i.name = "Ошибка API" + i.name
	        i.save()
	print("--------------")
	print(today)

def api_call_leadGid():
	all_mfo = Post.objects.all()
	all_mfo = all_mfo.filter(offer_want=True)
	today = date.today()
	for i in all_mfo:
	    offer_id = str(i.offer_id)
	    account = i.partner.all()
	    api_key = ""
	    for z in account:
        	api_key = z.api_key
	    url = "https://api.leads.su/webmaster/offers/" + offer_id + "/?token=" + api_key
	    r = requests.get(url)
	    data = r.json()
	    status = data["count"]
	    if status == "1":
	        i.offer_status = True
	        i.save()
	    elif status == "0":
	        i.offer_status = False
	        i.save()
	    else:
	        i.offer_status = False
	        i.name = "Ошибка API" + i.name
	        i.save()
	print("--------------")
	print(today)
