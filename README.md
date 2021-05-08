# Pizza App Project C3

 
The Homepage:
It displays the option to create a new pizza, the names of all the pizzas available in the database, and the individual option to update and delete those pizzas. 

http://127.0.0.1:8000/create_pizza/
This endpoint is for creating a new pizza by filling in the 4 fields and clicking on submit button. The Pizza Type field will accept only 2 inputs - Regular and Square. The Pizza Size field will accept only 3 inputs - Large, Medium, and Small. No error will be shown if anything except these inputs is entered. 

http://127.0.0.1:8000/update_pizza/pk
Here pk is the primary key of each individual pizza. When the update button is clicked, this endpoint will open with the help of the primary key of that specific pizza. The fields are pre-filled with the information of the pizza that needs to be updated. The user can make the necessary allowed changes to the information of the pizza in the database. The restrictions on the type and size of the pizza are the same as that of create_pizza endpoint. 

http://127.0.0.1:8000/delete/pk
Here pk is the primary key of each individual pizza. When the delete button is clicked, this endpoint will open with the help of the primary key of that specific pizza. A confirmation question will be asked with the name of the pizza. Two options are available: cancel (which will redirect the user to the homepage) and delete(which will delete the selected pizza from the database and then redirect the user to the homepage).

http://127.0.0.1:8000/info_pizza/
This endpoint is self-explanatory. It will show all the information of all the pizzas available in the database in a tabular form for easy viewing.
There are two filtering options available:
1) Sort by Type of Pizza
   http://127.0.0.1:8000/sortType/
   This will sort the info displayed on the info_pizza page by the type of pizza.

2) Sort by Size of Pizza
   http://127.0.0.1:8000/sortSize/
   This will sort the info displayed on the info_pizza page by the size of the pizza.
