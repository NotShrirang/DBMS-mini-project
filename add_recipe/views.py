from django.shortcuts import render, redirect
from pydbops import *

# Create your views here.
def add_page(request):
    return render(request, "add.html", {"add_" : False})

def create_recipe1(request):
    recipe_name = request.POST['recipe']
    author_name = request.POST['author_name']
    level = request.POST['level']
    time = request.POST['time']
    d = openDatabase("mydb.db")
    d.createTable("recipe_table", fields={"id" : "integer primary key", 
                                            "recipe_name" : "text",
                                            "author" : "text",
                                            "level" : "text",
                                            "time" : "text",
                                            "ing" : "text",
                                            "steps" : "text"})
    recipe_table = d.getTable(table="recipe_table")
    recipe_table.addEntry(values={"id" : recipe_table.length() + 1,
                                    "recipe_name" : recipe_name,
                                    "author" : author_name,
                                    "level" : level,
                                    "time" : time,
                                    "ing" : "BLANK",
                                    "steps" : "BLANK"})
    return render(request, "recipe_steps.html", {"add_" : False, 'recipe_name' : recipe_name})

def create_recipe2(request):
    ing = request.POST['ing']
    steps = request.POST['steps']
    d = openDatabase("mydb.db")
    recipe_table = d.getTable(table="recipe_table")
    recipe_table.updateEntry({"ing" : ing, "steps" : steps}, whereField="id", Is=recipe_table.length())
    return redirect("/")