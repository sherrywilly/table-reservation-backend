from django.shortcuts import render,get_object_or_404
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView
from customer.models import Booking, BookingItem, Rating
from django.http import *
from django.urls import reverse,reverse_lazy
from customer.forms import BookingUpdate
from django.forms import ValidationError
# Create your views here.


#! booking views

class OrderList(View):
    def get(self, request):
        if not request.user.is_superuser and request.user.is_staff:
            data = Booking.objects.filter(restaurant__user=request.user)
           
            context = {
                "data": data
            }
            return render(request, "booking/list.html", context)

        else:
            data = Booking.objects.all()
          
            context = {
                "data": data
            }

            return render(request, "booking/list.html", context)
    
   



class OrderDetailView(DetailView):
    model = Booking
    template_name="booking/detail.html"
    def get_object(self):
        _pk = self.kwargs.get('pk')
        # print(_pk)
        return get_object_or_404(Booking,id=_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        print(pk)

        
        return context
    
        



class OrderUpdate(View):
    def get(self,request,*args, **kwargs):
        pk = kwargs.get('pk')
        try:
            booking_object = get_object_or_404(Booking,id=pk)
        except ValidationError as e:
            print(e)
            return HttpResponseRedirect(reverse('orders'))
       
        x = BookingUpdate(instance = booking_object)
        
        
        context = {
            "form":x,
            "title":"Order Update"
        }
        return render(request,"form.html",context)

    def post(self,request,*args, **kwargs):
        b_obj = Booking.objects.get(id=kwargs.get('pk'))
        form = BookingUpdate(request.POST,instance=b_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('order-update',kwargs={"pk":kwargs.get('pk')}))

        


class BookingView(View):

    def get(self, request, *args, **kwargs):
        # ! need to complete the form

        context = {

        }
        return render(request, "", context)

    def post(self, request, *args, **kwargs):
        pass


class ratingList(ListView):
    model = Rating
    template = ""
    context_object_name = "data"
