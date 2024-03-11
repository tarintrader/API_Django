# Loan Requests API
This is a Django REST Framework project that provides a web API for receiving loan requests from different sources (Origin1 and Origin2) in JSON format with different structures, which are normalized and stored in a database.

## JSON Structures
### Origen1
- **nombre**: Name of the applicant.
- **apellidos**: Surname of the applicant, separated by a space.
- **fechaNacimiento**: Birthdate of the applicant in dd/MM/yyyy format.
- **cantidad**: Amount requested for the loan.
### Origen2
- **nombreCompleto**: Full name of the applicant.
- **fechaNacimiento**: Birthdate of the applicant in yyyy/MM/dd format.
- **cantidadSolicitada**: Amount requested for the loan.

## Request Normalization
The normalization of requests will store the following information in the **'LoanApplication'** model:

- **origin**: Source of the received information (1 or 2).
- **full_name**: Name and surnames of the applicant, separated by spaces.
- **name**: Name of the applicant.
- **surname**: Surnames of the applicant.
- **birthdate**: Birthdate of the applicant.
- **amount**: Amount requested for the loan.
- **created**: Date when the request was received.

All information from each source, both normalized and received, will be stored.


## Installation 

1. Open your terminal and navigate to the directory where you want to clone the repository.
2. Clone the repository from GitHub:
~~~ 
git clone https://github.com/tarintrader/Technical_Test_Python
~~~
3. Once cloned, navigate to the project directory:
~~~ 
cd django_api 
~~~
4. Install project dependencies using pip:
~~~ 
pip install -r requirements.txt
~~~
5. Run database migrations:
~~~ 
python manage.py migrate
~~~
6. Start the development server:
~~~ 
python manage.py runserver
~~~
7. The API will be available at http://localhost:8000.

## Contact

If you have any questions or suggestions, feel free to contact me at [tarintrader@gmail.com](tarintrader@gmail.com).