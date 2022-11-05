from django.shortcuts import render, redirect
from django.http import HttpResponse
from pydbops import *

# Create your views here.
def home(request):
    try:
        d = openDatabase("mydb.db")
        recipe_table = d.getTable("recipe_table")
        table_data = recipe_table.values(list=True)
        # print(table_data)
        
        data_list: list[dict] = []
        for entry in table_data:
            dictionary = {}
            dictionary['id'] = entry[0]
            dictionary['recipe_name'] = entry[1]
            dictionary['author_name'] = entry[2]
            dictionary['level'] = entry[3]
            dictionary['time'] = entry[4]
            dictionary['ing'] = entry[5]
            dictionary['step'] = entry[6]
            
            data_list.append(dictionary)
    except:
        data_list = []

    return render(request, "main.html", {"add_" : True, "recipes" : data_list})

def load_edit_recipe(request):
    id = None
    for key in request.POST.keys():
        if key.startswith('id:'):
            id = key[3:]
            break
    # print(id)
    d = openDatabase("mydb.db")
    recipe_table = d.getTable("recipe_table")
    table_data = recipe_table.values(list=True)
    recipe_name = ""
    for entry in table_data:
        if int(entry[0]) == int(id):
            recipe_name = entry[1]
            break
    return render(request, "edit.html", {"add_" : True, "id" : id, "recipe_name" : recipe_name})

def update(request):
    id = None
    for key in request.POST.keys():
        if key.startswith('id:'):
            id = key[3:]
            break
    # print(id)
    recipe_name = request.POST['recipe']
    author_name = request.POST['author_name']
    level = request.POST['level']
    time = request.POST['time']
    ing = request.POST['ing']
    steps = request.POST['steps']

    d = openDatabase("mydb.db")
    recipe_table = d.getTable("recipe_table")
    dictionary = {}
    dictionary['recipe_name'] = recipe_name
    dictionary['author'] = author_name
    dictionary['level'] = level
    dictionary['time'] = time
    dictionary['ing'] = ing
    dictionary['steps'] = steps
    recipe_table.updateEntry(values=dictionary, whereField='id', Is=id)
    return redirect('/')

def remove(request):
    id = None
    for key in request.POST.keys():
        if key.startswith('rem:'):
            id = key[4:]
            break
    print(id)
    
    d = openDatabase("mydb.db")
    recipe_table = d.getTable("recipe_table")
    recipe_table.removeEntry(id=int(id))
    return redirect('/')