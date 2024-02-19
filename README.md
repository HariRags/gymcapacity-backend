Hey kanika,
I wrote this just simple user login as we discussed earlier using bulti-in django authentication system.

I dont know about serializers.   Views i had to test it so many times so i added it please check if anything is wrong this is very basic login system.

# How to test it
http://localhost:8000/user/signup/ - Sigup page after clicking this you will be redirected to login page

http://localhost:8000/user/login/  - after clicking login you will be redirected to welcome page


http://localhost:8000/user/welcome/ - it shows welcome to gym app you are successfully logged in


# Problems
1. http://localhost:8000/user/welcome/ - if the user goes straightly to this url he will see welcome to gym app without login or signup which should not happen ideally.

2. And after you signup if you click same sigup page twice it will show forbidden error

And there are more errors like that.

Let me know if anything has to be changed or to improve for now.
