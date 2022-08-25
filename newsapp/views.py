from django.shortcuts import render
import requests

# Create your views here.
def home(request):
	if request.POST.get("src") and request.POST.get("btn"):
		src = request.POST.get("src")
		try:
			a1 = "http://newsapi.org/v2/top-headlines"
			a2 = "?sources=" + src
			a3 = "&apiKey=" + "70888f4dd52a49349ca32c6fc7bc38b1"
			#print(src)
			wa = a1 + a2 + a3
			#print(wa)
			res = requests.get(wa)
			data = res.json()
			info = data["articles"]
			return render(request,"home.html",{"msg":info,"src":src})
		except Exception as e:
			return render(request,"home.html",{"msg":"issue" + str(e)})
	else:
		return render(request,"home.html")
