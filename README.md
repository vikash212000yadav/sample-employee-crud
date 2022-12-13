# Sample Employee CRUD

Sample Employee CRUD based on Flask restful web framework.

## Features available:
- The Employee details are ```Name, Email, Phone, Employee ID, Country, Department```
- The Employee ID must be auto generated with UUID-V4
- The Department is an enumeration of ```Technology, Marketing, Sales, HR, Business, Management```
- While creating the phone number and email must be validated with proper Regex
- All the CRUD operations must have relevant GET, POST, PUT, and DELETE APIs
- Every API must validate header "x-api-key" with "<given_key>" must use Flask Middleware to authenticate
- The backend must be using Psycopg with PostgreSQL on the free hosted version on https://www.elephantsql.com/ and the Connection URL must be used from the same.

## Steps to install and run in local system:-

- Create a virtual environment
    ```python3 -m venv <env_name>```
    
- Activate virtual environment
    ```source <env_name>/bin/activate```
    
- Install requirements in venv
    ```pip install -r requirements.txt```
    
- Init migrate
    ```flask db init```

- Migrate the changes
    ```flask db migrate```

- After successfully setting them up upgrade flask migrations
    ```flask db upgrade``` 

- Run the server
    ```flask run``` or ```python app.py``` 


