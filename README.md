
**1.API Data Retrieval and Storage:**

First run the API (python sample_API.py)
Now the External API is ready at the endpoint ("http://127.0.0.1:5000/books")
Now run the main file (python main.py)
It will check whether the local database is exist or not, if not it will create a local SQLite database with a table to store books data in it.
The it will retrieve the books data from our external API by using the GET request.
It will display the data on the console and save it to the local database.
