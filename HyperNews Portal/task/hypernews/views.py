from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


class HomePage(View):
    def main_page(self, request):
        return HttpResponse(f"<p>Coming soon</p>\n<a target='_blank' target='_blank' href='/news/>Back to news</a>")

    def redirect_view(self):
        return HttpResponseRedirect("news/")
