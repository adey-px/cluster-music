## 1.0 Project Name: Cluster Music
The aim of the project is to develop a custom application for user to listen to audio music, similar to existing popular audio apps like Spotify, Amazon music & YouTube music among others. The application consists of a home page displaying audio and a search bar where user can search for audio music to play. There is also a navigation panel on the left side and it appears on all pages of the site

The project is deployed to Python Anywhere on ............


## 2.0 UX
The web Application is developed for any user who enjoys playing audio music for relaxation or any other reason

### 2.1 User stories
As a user, I want to:
1. click on any audio to play it 
2. search for audio to play in the search bar
3. create an account and login successfully 
4. upload my own audio to the site to allow other users to listen to it
5. view list of my own audios and be able to edit or delete them
6. save favourite audio as a playlist

As a Pro user, I want to:
1. download audio from the site to my computer

### 2.2 Wireframes
In order to bring the idea of this project to life, wireframes were produced with the use of marker & paper. The folder named "wireframes" has been uploaded in this project's GitHub repository. The folder contains images of the wireframes designed to show Desktop, Tablet and Mobile views of various pages of the application


## 3.0 Features
### 3.1 Existing Features
1. The site has top navigation bar having name logo on the right, a search bar at the center and user account account on the left side
2. The search bar allows user to search for audio to play
3. The user account icon consists of Register and Login links which allow user to register new account and login existing account respectively
4. There is also a navigation panel on left side which consists of links that allow user to navigate to inner pages of the site
5. When user clicks on an audio object, it opens in now_playing page and the audio is played from beginning to end
6. While audio is playing, it can be paused or fast-forwarded by user
7. Audio has functionality which allows user to select previous or next audio to play
8. On now_playing page, there is a right panel which loops over all audio in database. This makes it easy for user to have access to select any audio of their choice to play
9. Registered user has the previledge to upload their own audio and they can see the list of their audio in "Your Audio" page
10. Pro user who has made once-off payment using Stripe payment link provided, has the previledge for unlimited download of audio from the site

### 3.2 Features Left to Implement
1. Add autoplay functionality to audios in the player
2. Functionality to check audio format and automatically detect audio length/duration during uploading
3. Random display of various audios from database on the home page and the right panel on now_playing page
4. Allow user to be able to share audio on Social media platforms and email through button link attached to each audio
5. Allow authenticated user to see their play history on History page accessible via the History button link located on left panel
6. Use coding to implement Stripe payment for Pro users rather than the Payment link used due to constraint of project submission time
7. Improve the UI/UX design of the application for better user experience

### 3.3 Languages and Technologies Used
1. <a href="https://en.wikipedia.org/wiki/HTML" target="_blank">HTML5:</a>  This project uses HTML5 as the backbone and main markup language
2. <a href="https://mdbootstrap.com/docs/b4/jquery/" target="_blank">Material Design:</a> It uses Material Design for Bootstrap 4 Standard as Frontend Framework to design its layout and user interface
3. <a href="https://en.wikipedia.org/wiki/CSS" target="_blank">CSS3:</a> The project uses CSS3 for additional styling
4. <a href="https://fontawesome.com/" target="_blank">Font Awesome:</a> It uses Font Awesome for form input fields and button icons
5. <a href="https://www.javascript.com/" target="_blank">JavaScript:</a> It uses vanilla JavaScript for audio player functionality
6. <a href="https://www.djangoproject.com/" target="_blank">Django:</a>  It uses Django framework based on Python Language. The Django technology is to develop the site's dynamic content, CRUD Operations, user authentication and other programming functionalities
7. <a href="https://www.sqlite.org/index.html" target="_blank">SQLite:</a> It uses default SQLite database engine in Django to store data
8. <a href="https://www.pythonanywhere.com/" target="_blank">Python Anywhere:</a> It uses Python Anywhere platform as a Service for deployment to make the application visible and available for the public


## 4.0 Testing
All the internal and external links including menu items on navigation bar works well and the application looks good on Chrome, Mozilla and Edge browsers. The site is responsive on mobile devices

### 4.1 Code Validation
1. HTML codes were tested with <a href="https://validator.w3.org/#validate_by_input" target="_blank">W3C MarkUp Validation Service</a>. The codes returned with no error
2. CSS codes were tested with <a href="https://jigsaw.w3.org/css-validator/" target="_blank">W3C CSS Validation Service</a>. The codes returned with no error
3. JavaScript codes were tested with <a href="https://jshint.com/" target="_blank">JSHint</a>. The codes returned with no error
4. Python codes were tested with <a href="http://pep8online.com/" target="_blank">PEP8</a>. The codes returned with no error

### 4.2 Testing Responsiveness
All the pages of this application are well responsive on all devices including dektop, tablet and mobile devices. See images below for results
<img src="readme/capture-one.png" alt="responsiveness-result">
<img src="readme/capture-two.png" alt="responsiveness-result">
<img src="readme/capture-three.png" alt="responsiveness-result">
<img src="readme/capture-four.png" alt="responsiveness-result">
<img src="readme/capture-five.png" alt="responsiveness-result">

### 4.3 Testing Browser Compatibility
This application is compatible on popular browsers including Chrome, Edge, Safari and Firefox.
<img src="readme/browser-compatibility.png" alt="browser-compatibility-result"> 

### 4.4 Testing User Story 
The following user stories were tested for user: 
1. select an audio and play it successfully 
2. search for an audio in search bar to play
3. create an account with email/username and password
4. Login into their account successfuly
5. upload audio to the site to allow other users to listen to it
6. view list of their uploaded audios and be able to edit or delete them
7. save favourite audio as a playlist

The following user story was tested for Pro user:
1. download audio from the site to my computer successfully

### 4.5 Testing Existing Features
1. All the navigation links and buttons on the application work as expected
2. User can add/upload audio into the database
3. They can also create/read (play audio), edit/update and delete their audio successfully and these complete CRUD functionalities
4. All the forms including Register form, Login form and all other forms work as expected
5. User can search for audio in search bar and click on it to play
6. They can create account and login sucessfully with their username and password
7. Authenticated user can  upload audio and view the list of their audio in "Your Audio" page
8. They can save audio and create a playlist of their favorite audios
9. They can click forward or backward button to play next or previous audio respectively
10. They can click to play/pause, fastward or rewind audio on now_playing page
11. Pro user can download unlimited audio to their personal computer

### 4.6 Bugs
While developing this application, I encountered some bugs and fixed them as follow:
1. When I clicked any audio to play on home page, it always displayed firts audio on the page whereas it supposed to display and play
the specific audio that I clicked. I fixed this bug by using Coditional Expressions with Case & When, to make the selected audio object
to always show on top of the iteration in the paginator. I learnt this concept from <a href="https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator">Stack Overflow</a>
2. I tried using coding to implement Stripe payment for Pro user but it was not working as expected. However dur to time constraint, I used Stripe payment link provided on their website to implement payment for Pro user
3. During deployment to heroku, I got an error at the terminal "AssertionError: database connection isn’t set to UTC”. I searched Google for solution and I got an idea to <a href="https://exerror.com/assertionerror-database-connection-isnt-set-to-utc/">downgrade psycopg2</a> installation to 2.8.6 and that fixed the issue



## 5.0 Deployment
This project is hosted on Python Anywhere using this procedure:






## 6.0 Credits
### 6.1 Content
1. This project used Bootstrap 4.4 for its User Interface <a href="https://getbootstrap.com/docs/4.4/getting-started/introduction/">Bootstrap</a> 
2. Code for main header with Search bar and Django message levels were copied from Code Institute Boutique Ado project
3. I got idea for JavaScript code to play audio and html code for audio display from <a href="https://www.section.io/engineering-education/how-to-build-a-music-player-using-django/">Onojakpor Ochuko</a> 

### 6.2 Media
The images used for the audio labels were obtained from <a href="images.google.com">Google images</a>

### 6.3 Acknowledgement
I got inspiration for this project from YouTube website and Spotify music app
