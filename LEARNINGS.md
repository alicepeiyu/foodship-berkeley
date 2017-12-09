Foodship –where you meed new friends
Info 253 Final Project
Group Members: Alice Yang, Jason Zhixuan Dai, Jiaxun Song, Muxuan Lyu, Zihao Fan

ϖ	URL:  http://berkeley-foodship.herokuapp.com/

ϖ	Project Summary
A web-based application where people can find dining partners online. Our recommendations are based on user’s basic(default) information upon registration as well as their real-time dining request input. Our user interface features simplistic and cohesive design that allow handy usage for both new and registered users. The backend server and system design incorporate database management, self-developed API, external API(Yelp) connection, and machine learning algorithms(for recommendations). 


ϖ	Use Case:

1.	User Register. System performs email check with database to see if the email is already registered. After clicking on submit, one user record is inserted into the database.

2. User logs in. System performs email/password matching check. If not correct, webpage flags the specific error. Browser remembers the user if user chooses ‘Remember Me’.
Web Server remembers the logged user with session module under Flask.

3. As the user logs in, the web page will remember the user and has a welcome logo on the right with User’s name.


4. The browse page will show up once the user successfully logged in. System pops up five meal recommendations based on user’s cuisine preference ( an information provided during register). A meal recommendation is a record that some other user has created. For each meal recommendation, web server retrieves the meal information such as Initiator, Cuisine, Budget, Time and render the html providing these parameters.

5. Now user has two options:
	A: Five dining recommendations corresponding to that user’s three dining preference (default information) will be retrieved from dining_option table. The user can join the recommended dining schedule by clicking the “join” button. Once the button is clicked, the system will automatically send email notifications to both the dining initiator and that user. In the backend, the API will update the matching status to “matched” in the dining_option table. Also, the user can choose to create his/her own dining plan.

	B: A user creates his/her own dining plan by entering preferred cuisine type(American, Chinese, Ethiopian, French, Indian, Italian, Japanese, Korean, Mexican, Mediterranean, Russian, Spanish or Thai), time preference (Breakfast, Lunch, Dinner either Today or Tomorrow) and budget range ($ 0-15, $$ 15-40, $$$ 40+). The system matches this information to find three optimal recommendations based on allocating different weights to cuisine, time, budget (0.3,0.5,0.2 accordingly) to compute the weighted I2 norm Euclidean distance between user own input with all other entries. If user chooses to join one of the three recommended dining plans,  the system will notifies both users following the same procedure. If not, the user can choose to create an unmatched dining option and waits for other users to join him/her. 

6. User Dining History:
The View Your Meal tab on the navigation bar displays all the dining history of the user. A user can view the information of matched and unmatched dining plan (Date, Meal, Cuisine, Status, Restaurant and Companion). This function helps the user to keep track of upcoming dining program and enables the system to find active users and popular dining option.  


ϖ	List of Technology:

HTML--It builds the outline of the web application and functions as external infrastructure

CSS--It defines what each block/part of the webpage looks like

JavaScript--It provides the webpage the ability to interact with the end users, also sometimes talk to the database with the assistance of Ajax.

Python--It is the language  in which the Web Server and the API Server are written

Flask--It is the web application framework which we use to build a web server from scratch

HTTP--HTTP functions as a request–response protocol between a client and server. The client(web browser) submits an HTTP request message to the server. The server, which provides resources such as HTML files and other content, or performs other functions on behalf of the client, returns a response message to the client. The response contains completion status information about the request and may also contain requested content in its message body.

JSON-- JSON is the format of transmitting data between webserver and API.

SQLite-- SQLite is the database we use to store data.

TCP--TCP is a set of the transmission control protocol which every step of the data transmission 
in my application abides by. It provides reliable, ordered, and error-checked  delivery of a 
stream of octets between applications running on hosts communicating by an IP network.

IP-- IP is a set of protocols which defines the basic units and formats of data transmission, also 
the delivery methods and routing path.

Content Type-- The content type tells the receiver (in our case API) what the content type of 
the expected content actually is. So the receiver can decides what method to process the 
content.

Cloud-- our application is deployed on the cloud. Specifically, we are using PaaS Heroku to host our web server and API server. The users can get access to the application through the domain address Heroku assigned to us.
