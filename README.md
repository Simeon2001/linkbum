###### LIBUM

a linktree clone API which is use to put important links(product link,your new release song link, e.t.c) and social-media link in place, can be shared with friends and customers.

##### TUTORIAL

* TO CREATE AN ACCOUNT USE http://127.0.0.1:8000/api/register then with a post request containing the json data:
-----------------------------
{
    "username":"hartech",
    "password":"Linktree2021"
    "email":"hartech@gmail.com"

}
------------------------------
after registering it automatically create an authtoken.

* TO LOGIN USE http://127.0.0.1:8000/api/token to determine if the user have an account, you can pass this post request with this json data: 
----------
{
    "username":"hartech",
    "password":"Linktree2021"

}
------------------------------
if the user have created an account before it will response with an authtoken, else with an error

* TO VIEW USER PROFILE http://127.0.0.1:8000/api/profile pass a GET request and authorization in the header. 
the Authorization format is "Token (the user token)"

* TO CREATE A PROFILE http://127.0.0.1:8000/api/procreate pass a POST request and authorization in the header and json data:
-----------------------------
{
    "pics":"an image url",
    "info":"little personal details"

}
------------------------------

* TO ADD A LINK http://127.0.0.1:8000/api/links pass a POST request and authorization in the header and json data:
-----------------------------
{
    "url":"url u want to share",
    "info":"short info about the url"

}
------------------------------

* TO VIEW LINKS SHARED BY CERTAIN USER http://127.0.0.1:8000/USERNAME pass a GET request.

* TO ADD SOCIAL MEDIA LINK FOR A USER http://127.0.0.1:8000/api/slink/create pass a post request.

  pass the token to the header, then json data:

  ---------------------
  {
      "fbk":"http//facebook.com",
      "twr":"http//twitter.com",
      "ins":"http//instagram.com",
      "whp":"http//api.whatsapp.com",
      "snt":"http//snapchat.com",
      "gtb":"http//github.com",
  } 
-----