# zomato/views.py
#menu
from django.shortcuts import render,redirect
from .menu import get_menu

def display_menu(request):
    menu = get_menu()
    return render(request, 'menu.html', {'menu': menu})
# zomato/views.py

#Add

def add_dish(request):
    if request.method == 'GET':
        return render(request, 'add_dish.html')




def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        price = float(request.POST.get('price'))
        
        # Generate a new dish ID (for demonstration purposes)
        new_dish_id = max(get_menu().keys()) + 1
        
        new_dish = {
            'name': dish_name,
            'price': price,
            'available': True  # Assume new dishes are available by default
        }
        
        get_menu()[new_dish_id] = new_dish
        
        return redirect('menu')
    
    return render(request, 'add_dish.html')
#DElete



def remove_dish(request):
    if request.method == 'POST':
        dish_id = int(request.POST.get('dish_id'))
        if dish_id in get_menu():
            del get_menu()[dish_id]
        return redirect('menu')
    
    return render(request, 'remove_dish.html')

#Update _dish
def update_dish(request):
    if request.method == 'POST':
        dish_id = int(request.POST.get('dish_id'))
        if dish_id in get_menu():
            new_dish = request.POST.get('available') == 'on'
            new_price = float(request.POST.get('price'))
            
            dish = get_menu()[dish_id]
            dish['available'] = new_dish
            dish['price'] = new_price
            
        return redirect('menu')
    
    return render(request, 'update_dish.html')