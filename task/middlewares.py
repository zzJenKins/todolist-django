from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render

class BrowserMiddleware(object):
    def process_request(self,request):
        user_agent = request.META['HTTP_USER_AGENT']
        print(user_agent)
        if "MSIE" in user_agent:
            return render(request,"browser.html")

        return None
