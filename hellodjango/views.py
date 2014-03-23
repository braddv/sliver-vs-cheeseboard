from django.http import HttpResponse

def home(request):
  html = "<html><body>Hello!</body></html>"
  return HttpResponse(html)
