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




# views.py

# ... your existing imports ...

# views.py

# ... your existing imports ...

def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST['dish_name']
        price = float(request.POST['price'])
        available = 'available' in request.POST
        description = request.POST['description']

        # Get the menu data from the function and calculate the next dish_id
        menu_data = get_menu()  # Call the function to get the menu data
        dish_id = len(menu_data) + 1

        # Save the new dish to the menu data
        menu_data[dish_id] = {
            'name': dish_name,
            'price': price,
            'available': available,
            'description': description
        }
        return redirect('menu')  # Redirect to the menu page

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