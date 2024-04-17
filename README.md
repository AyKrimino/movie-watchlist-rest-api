# Movie Watchlist

````markdown
## Description
Movie Watchlist is a Django Rest Framework project where users can perform CRUD operations on a collection of movies. Each movie is defined by several fields in the database, including title, year, genre, director, cast, plot, rating, and poster.

## Installation
To install the required dependencies, run the following command after creating a Python virtual environment:
```
pip install -r requirements.txt  # Windows
python3 -m pip install -r requirements.txt  # Linux
```

## Usage
To run the server, activate the virtual environment and execute:
```
python manage.py runserver [port]  # Default port is 8000
```
Note: If you're using Linux, replace `python` with `python3`.

### API Overview
To get an overview of available movie-related API endpoints, navigate to `/api-overview/`. This endpoint provides a dictionary of available API endpoints along with the allowed HTTP methods for each endpoint.

## Endpoints
- **List Movies**: `/movies-list/` (GET)
- **Movie Detail**: `/movies-list/<str:pk>/` (GET, PUT, PATCH, DELETE)
- **Create Movie**: `/movie-create/` (POST)
- **Update Movie**: `/movie-update/<str:pk>/` (PUT, PATCH)
- **Delete Movie**: `/movie-delete/<str:pk>/` (DELETE)

## Authentication
This project does not include authentication. Users can implement their own authentication system, such as JWT, if desired.

## Contributions
Contributions are welcome! Please feel free to fork the repository and submit pull requests.

## License
[License information here] - You can choose a license that best fits your project. Common choices include MIT, Apache, and GPL licenses.
```markdown
```markdown

This should render correctly in markdown preview, with the entire content enclosed within a single code block. Let me know if this works for you!
# Movie Watchlist

````markdown
## Description
Movie Watchlist is a Django Rest Framework project where users can perform CRUD operations on a collection of movies. Each movie is defined by several fields in the database, including title, year, genre, director, cast, plot, rating, and poster.

## Installation
To install the required dependencies, run the following command after creating a Python virtual environment:
```
pip install -r requirements.txt  # Windows
python3 -m pip install -r requirements.txt  # Linux
```

## Usage
To run the server, activate the virtual environment and execute:
```
python manage.py runserver [port]  # Default port is 8000
```
Note: If you're using Linux, replace `python` with `python3`.

### API Overview
To get an overview of available movie-related API endpoints, navigate to `/api-overview/`. This endpoint provides a dictionary of available API endpoints along with the allowed HTTP methods for each endpoint.

## Endpoints
- **List Movies**: `/movies-list/` (GET)
- **Movie Detail**: `/movies-list/<str:pk>/` (GET, PUT, PATCH, DELETE)
- **Create Movie**: `/movie-create/` (POST)
- **Update Movie**: `/movie-update/<str:pk>/` (PUT, PATCH)
- **Delete Movie**: `/movie-delete/<str:pk>/` (DELETE)

## Authentication
This project does not include authentication. Users can implement their own authentication system, such as JWT, if desired.

## Contributions
Contributions are welcome! Please feel free to fork the repository and submit pull requests.

## License
[License information here] - You can choose a license that best fits your project. Common choices include MIT, Apache, and GPL licenses.
```markdown
```markdown

This should render correctly in markdown preview, with the entire content enclosed within a single code block. Let me know if this works for you!
