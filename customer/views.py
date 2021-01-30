from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,UpdateView,CreateView
from customer.models import Booking, BookingItem, Rating
# Create your views here.


#! booking views 

class BookingList(ListView):
    model = Booking
    template = ''
    context_object_name = 'data'


class BookingDetail(DetailView):
    model = Booking
    template_name = ''
    context_object_name ='data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['item'] = BookingItem.objects.filter(order=self.object)
        except:
            pass
        return context



class BookingView(View):

    def get(self, request,*args, **kwargs):
        # ! need to complete the form

        context ={

        }
        return render(request, "", context)


    def post(self, request,*args, **kwargs):
        pass


class ratingList(ListView):
    model = Rating
    template = ""
    context_object_name = "data"