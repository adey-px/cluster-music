## 1.0 Project Name: Cluster Music
The aim of the project is to develop a custom application for user to listen to audio music, similar to existing popular audio apps like Spotify, Amazon music & YouTube music among others. The application consists of a home page displaying audio and a search bar where user can search for audio music to play. There is also a navigation panel on the left side and it appears on all pages of the site

The project is deployed to Heroku on https://dj-cluster-music.herokuapp.com/

## 2.0 UX
The web Application is developed for any user who enjoys playing audio music for relaxation or any other personal reason

### 2.1 User storiess
As a user, I want to:
1. click on any audio to play it 
2. create an account and login successfully 
3. upload my own audio to the site to allow other users to listen to it
4. view list of my own audios and be able to edit or delete them
5. save favourite audio as a playlist

As a Pro user, I want to:
1. make payment and download audio from the site to my computer

### 2.2 Wireframes
In order to bring the idea of this project to life, wireframes were produced with the use of marker & paper. The folder named "wireframes" has been uploaded in this project's GitHub repository. The folder contains images of the wireframes designed to show Desktop, Tablet and Mobile views of various pages of the application


## 3.0 Features
### 3.1 Existing Features
1. The site has top navigation bar having name logo on the right, a search bar at the center and user account account on the left side
2. The site has no footer so as to allow continuous scrolling down similar to Youtube site and Facebook
3. The user account icon consists of Register and Login links which allow user to register new account and login existing account respectively
4. There is also a navigation panel on left side which consists of links that allow user to navigate to inner pages of the site
5. When user clicks on an audio object, it opens in now_playing page and the audio is played from beginning to end
6. While audio is playing, it can be paused or fast-forwarded by user
7. Audio has functionality which allows user to select previous or next audio to play
8. On now_playing page, there is a right panel which loops over all audio in database. This makes it easy for user to have access to select any audio of their choice to play. The right panel is hidden is mobile view
9. Registered user has the previledge to upload their own audio and they can see the list of their audio in "Your Audio" page
10. Pro user who has made once-off payment using Stripe payment link provided, has the previledge for unlimited download of audio from the site per session

            Username: adey-px
            Paswword: adeyking1

### 3.2 Features Left to Implement
1. Fucntionality to search for audio by title or artist in the search bar
2. Add autoplay functionality to audios in the player
3. Functionality to check audio format and automatically detect audio length/duration during uploading
4. Random display of various audios from database on the home page and the right panel on now_playing page
5. Allow user to be able to share audio on Social media platforms and email through button link attached to each audio
6. Allow authenticated user to see their play history on History page accessible via the History button link located on left panel
7. Use coding to implement Stripe payment for Pro users rather than the Payment link used due to constraint of project submission time

### 3.3 Languages and Technologies Used
1. <a href="https://en.wikipedia.org/wiki/HTML" target="_blank">HTML5:</a>  This project uses HTML5 as the backbone and main markup language
2. <a href="https://mdbootstrap.com/docs/b4/jquery/" target="_blank">Material Design:</a> It uses Material Design for Bootstrap 4 Standard as Frontend Framework to design its layout and user interface
3. <a href="https://en.wikipedia.org/wiki/CSS" target="_blank">CSS3:</a> The project uses CSS3 for additional styling
4. <a href="https://fontawesome.com/" target="_blank">Font Awesome:</a> It uses Font Awesome for form input fields and button icons
5. <a href="https://www.javascript.com/" target="_blank">JavaScript:</a> It uses vanilla JavaScript for audio player functionality
6. <a href="https://www.djangoproject.com/" target="_blank">Django:</a>  It uses Django framework based on Python Language. The Django technology is to develop the site's dynamic content, CRUD Operations, user authentication and other programming functionalities
7. <a href="https://www.postgresql.org/" target="_blank">Postgres:</a> It uses  Postgres database to store data
8. <a href="https://www.heroku.com/" target="_blank">Heroku:</a> It uses Heroku platform as a Service for deployment to make the application visible and available for the public


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
2. create an account with email/username and password
3. Login into their account successfuly
4. upload audio to the site to allow other users to listen to it
5. view list of their uploaded audios and be able to edit or delete them
6. save favourite audio as a playlist

The following user story was tested for Pro user:
1. download audio from the site to my computer successfully after making payment

### 4.5 Testing Existing Features
1. All the navigation links and buttons on the application work as expected
2. User can add/upload audio into the database
3. They can also create/read (play audio), edit/update and delete their audio successfully and these complete CRUD functionalities
4. All the forms including Register form, Login form and all other forms work as expected
5. They can create account and login sucessfully with their username and password
6. Authenticated user can  upload audio and view the list of their audio in "Your Audio" page
7. They can save audio and create a playlist of their favorite audios
8. They can click forward or backward button to play next or previous audio respectively
9. They can click to play/pause, fastward or rewind audio on now_playing page
10. Pro user can download unlimited audio to their personal computer

### 4.6 Bugs
While developing this application, I encountered some bugs and fixed them as follow:
1. When I clicked any audio to play on home page, it always displayed the first audio on the page whereas it was supposed to display and play
the specific audio that I clicked. I fixed this bug by using Coditional Expressions with Case & When, to make the selected audio object
to always show on top of the iteration in the paginator. I learnt this concept from <a href="https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator">Stack Overflow</a>
2. I used Stripe payment link provided on the Stripe website to implement payment for Pro user with feedback provided. However, Test mode from Stripe does not allow recurrent subscription. It was stated that I need to activate my Stripe account to be able to send Live subscription to users. Hence the need to make user payment active only when they remain logged in. Users have to make another payment to have access to the download page, if they logout of their Cluster account or close and reopen their browser again next time
3. During deployment to heroku, I got an error at the terminal "AssertionError: database connection isn’t set to UTC”. I searched Google for solution and I got this site <a href="https://exerror.com/assertionerror-database-connection-isnt-set-to-utc/">to downgrade psycopg2</a> installation to 2.8.6 and that fixed the issue
4. After successful deployment to heroku, created and connected to amazon S3 bucket to serve static files, the whole data (imgaes & audio) in my database did not show in live site on heroku but showing normally on development site through gitpod and all my user logins including admin login refused to work. I contacted tutor support and they guided me in following ways: <br>
    i. I manually created enviroment variable named DATABASE_URL (from heroku config var) in gitpod setting and added postgres db url as its value. Other option is to create env.py file and specify the enviroment variable key/value. <br>
    ii. I closed and restarted my gitpod workspace to reset the connected databse but the issue not still resolved at this time <br>
    iii. Next, I cut out the unneccessary requirements that gitpod added to my requirements.txt using this site https://lechien73.github.io/reqfix/ filter out the unrequired input. I noticed those unrequired files got listed after I installed boto3 and django-storages and then freeze the requirements.txt at gitpod terminal. I copied the filtered requirements and use it to replace the content inside requirements,txt file <br>
    iv. After that was done, I saved my requirements.txt file, Then I ran these two commands at the terminal <br>
        pip3 uninstall -y -r <(pip3 freeze) followed by pip3 install -r requirements.txt <br>
    v. At this time, I was able to create new super user and I logged into live site admin through https://dj-cluster-music.herokuapp.com/admin. Then I noticed that all my Audio database fileds were migrated and I just uploaded new fresh data into database and both the development site and live site worked normally <br>
5. However, out my curiosity and in further attempt to load existing data from previous database (sqlite) to current database (postgres), I contacted tutor support for help nad they guided me through even though few errors/issues were also encountered as below: <br>
    i. At the terminal, I used this command python3 manage.py dumpdata music > music.json but importError error showing <br>
    ii. Due to various showing at terminal, I opened new gitpod workspace for my existing project repo <br>
    iii. In the new workspace, I commented out postgres and activated sqlite to be database <br>
    iv. I ran python3 manage.py migrate to ensure latest migration before sending data to postgres <br>
    v. I installed the missing module pip3 install psycopg2-binary and then tried to load data to postgres using python3 manage.py loaddata music <br>
    vi. I got integrityError because the data files (images & audios) are connected to Userprofile and had to use commands to migrate users and userprofile model as well <br>
    vii. Then connected Gitpod back to Postgres by uncommenting it out, so that we can loaddata <br>
    viii. However, since the app automatically creates UserProfiles as soon as a User is created, I had to first upload Users, then check what UserProfiles have been created, and then check their PKs so I can adjust them in the audio dump <br>
    ix. When that was fixed, I was able to loaddata audio and my sqlite database content was fully transfered to postgres on Live site <br>
    x. At this time, all previous user logins started working again since users and userprofiles have been migrated along with their data into postgres. Thus, the site technically runs on two servers - development server in gitpod and Live server on heroku. The latter server uses sqlite while live server uses postgres. Each time code is git pushed to GitHub, the live site database gets updated.


## 5.0 Deployment
1. At the terminal, install Heroku cli and login to it using registered email & password on heroku site
2. Pip3 install required packages which are psycopg2-binary and gunicorn
3. Freeze the requirements and direct them to requirements.txt
4. Create new app on heroku using the commad: heroku apps:create dj-cluster-music
5. Open heroku dashboard, check to see the new app listed and select it
6. Click Resources tab - Add-ons, search for server-based database "Postgres" and select free version
7. Click Settings tab - Reveal Config Vars to see Postgres has been added as the app database
8. At the terminal, connect to the remote Postgres by pip3 install dj_databse_url
9. Again, freeze the requirements using pip3 freeze --local > requirements.txt
10. At terminal, type heroku config to get database url, which can also be gotten on heroku web ui
11. In the project, open settings.py/DATABASES. duplicate the existing code and comment out the previous
12. In the new code, set the direct value of 'default' to dj_database_url.parse('')
13. Copy and paste inside (''), the Database_url from heroku - already shown at the terminal in Step 10
14. At the top of settings.py, import dj_database_url
15. Run migration using python3 manage.py migrate to transfer data from default sqlite3 to remote Postgres on heroku
16. Uncomment the default database setting and remove heroku dj_database_url setting so it won't end up in version cotrol
17. Next, use git commands to push project code to GitHub to update the remote repo
18. Use if statement to determine which database to run, either default sqlite or heroku (postgres) dj_database_url
19. Create file named Procfile inside project main directory, which tells heroku to create web dyno that runs gunicorn
20. Login to heroku cli at terminal and temporarily disable collectstatic so heroku won't try to collect static files
21. Add heroku url for the app to be value of allowed host [] in settings.py
22. Use git commands to push code to GitHub and immediately type git push to heroku main - the app is deployed now
23. Open AWS account, create S3 bucket, User Group, IAM role policy and attach the role to S3 bucket
23. Create User under User Group and download security keys
24. Install boto3 and django-storages at Gitpod terminal and add 'storages' to the installed apps in settings.py and also add setting for django to connect to aws S3 bucket
24. Update setting in heroku by adding the security keys downloaded from aws and remove DISABLE_COLLECTSTATIC key/valu from the Config Vars
25. Create file named custom_storages.py in project directory to hold future static & media files uploaded by user. Add setting in settings.py to apply the custom_storages file
26. Use git commands to add and push code to Github which automatically update the deployed app on heroku


## 6.0 Credits
### 6.1 Content
1. This project used Bootstrap 4.4 for its User Interface <a href="https://getbootstrap.com/docs/4.4/getting-started/introduction/">Bootstrap</a> 
2. Code for main header with Search bar and Django message levels were copied from Code Institute Boutique Ado project
3. I got idea for JavaScript code to play audio and html code for audio display from <a href="https://www.section.io/engineering-education/how-to-build-a-music-player-using-django/">Onojakpor Ochuko</a> 

### 6.2 Media
The images used for the audio labels were obtained from <a href="images.google.com">Google images</a>

### 6.3 Acknowledgement
I got inspiration for this project from YouTube website and Spotify music app
