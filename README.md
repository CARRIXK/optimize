# optimize
---

[Source code can be found here](https://github.com/CARRIXK/optimize)

[The live project can be viewed here](https://optimize-800f80d21807.herokuapp.com/)

# Purpose of Project
---
Optimize is a web-based fitness app that allows users to create and edit workouts tailored to their needs. Users can build personalized workout routines by adding exercises and specifying sets with reps for each. Whether you're tracking strength progress, designing structured training plans, or simply organizing your workouts, Optimize provides a streamlined and intuitive interface to make workout planning effortless.

# Links to content
---
## Links to content
- [Features](#features)
- [User Experience](#user-experience)
- [Design](#design)
- [Fonts](#fonts)
- [Colour](#colour)
- [Wireframes](#wireframes)
- [Development Process](#development-process)
  - [Project Planning](#project-planning)
  - [Inline JavaScript](#inline-javascript)
  - [Data Model](#data-model)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Feature Testing](#feature-testing)
  - [Responsiveness](#responsiveness)
  - [Browser Compatibility](#browser-compatibility)
  - [Lighthouse](#lighthouse)
  - [Code Validation](#code-validation)
  - [Python](#python)
  - [JavaScript](#javascript)
  - [HTML](#html)
  - [CSS](#css)
  - [User Stories](#user-stories)
  - [Automated Testing](#automated-testing)
  - [Django Testing](#django-testing)
  - [Selenium Testing](#selenium-testing)
  - [Bugs](#bugs)
- [Libraries and Programs Used](#libraries-and-programs-used)
- [Deployment](#deployment)
  - [Deploying the App on Heroku](#deploying-the-app-on-heroku)
  - [Making a Local Clone](#making-a-local-clone)
  - [Running the App in Your Local Environment](#running-the-app-in-your-local-environment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

# Features
* Dashboard : After logging in, users are directed to the Dashboard Page, which provides an overview of their most recent activities and workouts. The main purpose of this page is to give users quick access to their recent progress and a streamlined way to track their fitness journey.

* Workouts : The Workouts page is where users can view a list of all the workouts they have created, providing an organized way to manage their fitness routines. Each workout is displayed with its title, number of excersises in that workout and date it was created. Users can interact with any workout by pressing the options button next to it, which opens a modal offering several options: starting the workout, editing the workout, or deleting it. 

* Create Workout : Creating a workout on the platform is an easy, customizable process that allows users to design routines tailored to their goals. Users begin by providing a title for their workout, such as "Leg Day" or "Upper Body Strength," then select exercises from a pre-defined list, which includes various movements targeting different muscle groups. After selecting exercises, users add sets and reps for each, determining the number of sets and reps per set. Users can then review and adjust the exercises, sets, and reps before saving the workout to their profile for future use. This process empowers users to create highly personalized workouts, track their progress, and stay on top of their fitness goals.


* Edit Workout: Editing a workout allows users to customize and adjust their exercises to better suit their needs. After selecting a workout to edit, users can add or remove exercises from the workout by selecting exercises from the list or deleting unwanted ones. For each exercise, users can add sets, specifying the number of repetitions . Additionally, if a user adds a new exercise, they can immediately add sets to it, ensuring that the workout is tailored to their specific training goals. .


* Future Features: In the future, functionality for starting a workout will be added to allow users to track their progress during the workout. This feature will enable users to begin their workout session directly from the workouts page, marking the start of their training. Once a workout is started, the app will track the completion of each exercise and set, recording important data such as the number of reps performed, the weight lifted, and any other relevant metrics. This tracking will provide users with real-time feedback on their performance, helping them to monitor their progress and adjust their workout intensity as needed. Additionally, the app will save these workout sessions, allowing users to review past workouts, track improvements over time, and make informed decisions about their future training routines.


# User Experience
## Design

### Fonts


### Colour


### Wireframes


# Development Process


# Data Model


# Testing
* Manual testing
* Automated testing
* In-app testing
* User story testing
* Validator testing

## Manual Testing
**Feature Testing**


**Responsiveness**
Here's screenshots taken with the Chrome dev tools device toolbar, set to the iPhone 12 Pro. They are, in order, the Workouts page, Create workout page, Add excersises page, workout set reps page:

iphone12_homepage iphone12_editor iphone12_instrument iphone12_review surfacepro_loop_detail

Here's the same five pages on the Surface Pro 7:

And finally the same five pages on a desktop monitor (1920x1080): 


**Browser Compatibility**
| Feature                                      | Chrome | Firefox | Safari (mobile) |
|----------------------------------------------|--------|---------|-----------------|
| Audio playback upon first user interaction  |    |     |             |
| Fonts render correctly                       |    |     |             |
| All elements visible                         |    |     |             |
| Pages are responsive at all screen sizes     |   |     |             |

### Lighthouse
Here are the lighthouse reports for the site's main pages :

**Workouts**

**Create workouts**

**Add Excersises**

**Edit workouts**


### Code Validation

**Python code** :

* Python code is yet to be validated by both the Flake8 linter (installed in VSCode) and the external CodeInstitute validator @ https://pep8ci.herokuapp.com/.

**JavaScript code** :



**HTML Validation** :



**CSS Validation** :


**User Stories**



## Automated Testing

**Testing django views, models and forms.**
 

# Bugs


Return to top

# Libraries and Programs Used

* Heroku
* Heroku was used to deploy the project
* Git
* Version control was implemented using Git through the Github terminal.
* Github
* Github was used to store the projects after being pushed from Git and its cloud service Github Pages was used to serve the project on the web. GitHub Projects was used to track the User Stories.
* Visual Studio Code

# Credits


# Acknowledgements

