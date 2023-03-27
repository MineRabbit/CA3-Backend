The chairs module is tested

For urls :
Each url is reversed and resolved back with an assertion testing if resolving the reverse url calls the correct view

For views :
A testing client is made before all the test cases
For views with no arguments the response code is directly tested to make sure it is equal to 200, not equal to 404
and that the correct template is used
For views with arguments a testing Owner and Chair are created, and the view is called similarly to the ones without
arguments but with the testing chair linked to the testing owner as the argument

The website was set to https using SECURE_SSL_REDIRECT = True
To prevent HTTP header attacks, the allowed hosts have been limited to 'localhost' and '127.0.0.1'