# GymManager


<img src='https://kivymd.readthedocs.io/en/1.0.1/_static/logo-kivymd.png' weight='300' height='300'>
<hr>

## Contents
 * <a href="#info"><strong>Info</strong></a><p>Information about the resources used in this project</p>
 * <a href="#GimManager"><strong>Gym Manager</strong></a><p>Android app for manage your gym experience written in KIVY python framework</p>
 * <a href="#clone_project"><strong>Clone and Run Project</strong></a><p>how run projects in your computer or in an telephone</p>

<hr>

<details><summary id="info" style="font-size: 30px;"> INFO</summary>
<h4>Information about the additional library, external Api used in this project and general information</h4>

<strong>KivyMD</strong> Kivy cross-platform graphical framework a framework for cross-platform, touch-enabled graphical applications.

<strong>Pillow</strong> The Python Imaging Library adds image processing capabilities to your Python interpreter.

<strong>Buldozer</strong> Buildozer is a tool that aim to package mobiles application easily. It automates the entire build process, download the prerequisites like python-for-android, Android SDK, NDK, etc.

<strong>sqlite3</strong> The standard Python Library to create and communicate with lite database.

</details>

<hr>
<center><h1 id="GimManager"> Gim Manager <span style='font-size:80px;'><img src="https://img.icons8.com/cotton/64/null/barbell.png"/></span></h1></center>

When opening the application, it will ask you to register (in the Play store version, this option is not available, because it is not necessary), then your profile will be saved in the database and saved in the session.csv file.

<img src='https://user-images.githubusercontent.com/97242088/208270902-c1e84a39-58fb-41f3-b738-157db364976e.png' alt='registration'>

Then you will have three screens to choose from, we will focus on the first one first. Enter your day's Name in the field and press 'add', the day will be created. You can add and remove how many days you want.

Then press the day you are interested in.

<img src='https://user-images.githubusercontent.com/97242088/208270908-0e65af8c-6d87-4409-b934-c6af9cfc7945.png' alt='add_new_day'>

Enter the name of your exercise weight and repits and click 'save'. When the next time you enter you can change whatever you want, just don't forget to press 'save'.

Now let's go to the midle screen 'stats'

<img src='https://user-images.githubusercontent.com/97242088/208270894-ac4f27a6-62e3-4c3b-a33b-7ffb27bc741d.png' alt='manage your day'>

Here will be your stats from the day of the exercise, which will be saved thanks to the screen we will see next.<br>
Stats divided by days and will display the date and time spent in the gym. And then you will be able to see the average time spent in the gym

<hr>

But to be able to see something in the statistics, you need to save something there, for this we click on the last screen with timers.<br>
This is where the most happens. The first timer counts the minutes, and the larger one counts your time spent that day in the gym.<br>
Click when you start training, and after training, if you want, click 'save' to show that day in the statistics.

<img src='https://user-images.githubusercontent.com/97242088/208270897-6aa0c3ed-ef0d-4fc4-98ea-bf71e4d2ec29.png' alt='timer1'>

<img src='https://user-images.githubusercontent.com/97242088/208270893-338e3a71-cb1e-4659-9992-73de2d8125a9.png' alt='timer2'>

<hr>

<center><h2 id="clone_project">Clone and Run a Project</h2></center>

Before diving let’s look at the things we are required to install in our system.

To run App prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source env/bin/activate`

Installing Kivy:-

`pip install kivy`

`pip install Pillow`

Also you need install KivyMD. Just clone the project from github and run pip:

```
git clone https://github.com/kivymd/KivyMD.git --depth 1
cd KivyMD
pip install .
```


Now, we need to clone my project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Install the project dependencies:

`pip install -r requirements.txt`

to run

`python main.py --size 250x500`

Or from 'bin' folder from this repository download file on your android app and install


Have fun
<p style="font-size:100px">&#129409;</p>




