from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Food,Consume
# Create your views here.
def index(request):

    if request.method == "POST":
        food_consumed = request.POST["food_consumed"]
        consume = Food.objects.get(name=food_consumed)
        ## get the current user, inbuild
        user = request.user
        consume_obj = Consume(user=user,food_consumed=consume)
        consume_obj.save()
        # Redirect to the same page to prevent duplicate form submissions
        return HttpResponseRedirect(reverse('index'))

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request,"myapp/index.html",{"foods":foods,"consumed_food":consumed_food})

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect("/")
    return render(request,"myapp/delete.html")