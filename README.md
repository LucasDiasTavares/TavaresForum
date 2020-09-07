### Login
* Vefiry account email disabled.
  * If wanna enable email vefirycation you can find read this documentation: [django-registration](https://django-registration.readthedocs.io/en/3.1/activation-workflow.html)

### Core directory
* In the core directory you can find:
  * views.py: a file that return a base template from my vue.js app
  * utils.py: method generate_random_string, used within questoes.signals to generate my slug automatically

### Questions app
- The slug from Question model is create automatically from a custom signal (add_slug_to_question)

### Login & Register
* You can use this 2 endpoints to help to test if don't wanna to test with the front web app.
  * http://127.0.0.1:8000/accounts/register/
  * http://127.0.0.1:8000/accounts/login/
  * Or via shell: python3 manage.py createsuperuser
