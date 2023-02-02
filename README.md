# LAB - Class 33
## Project: Django REST Framework: Authentication & Production Server
### Author: Ian F. Shirley

### Tests
- There are no new unit tests. To test functionality of JWT requests (), go to Thunder Client:
  - in the URL bar type: `http://0.0.0.0:8000/api/token`
  - change from a GET to a POST request
  - in the request body, enter: `{"username":"username","password":"password"}` ("username" & "password" as the keys, your username & password as the values)
  - Click Send