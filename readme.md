# Microsoft Engage Mentorship program'22 Project   
## Algorithms (Recommendation Engine)
### 🚩 Overview 
The purpose of the project is to get Content based recommendation which ensures that the content you are are watching is appeasing.
This project is solely built during the period of **Microsoft Engage Mentorship program'22** conducted by Microsoft provide mentorship and to enrich freshmen with various software development techniques.  
#### Problem statement (as given)
Demonstrate through your app the different kinds of algorithms that a web-streaming app (like Netflix) or an audio-streaming app (like Spotify) may use for their Recommendation Engine.  

- [x] Status : Accomplised by making a KNN model which recommend movie based on given movie. 

##### Adopt feature:
To build a fully functional app which demonstrates algorithms take place in recommender system.   
- [x] Status : Accomplished   

<img width=49% src="readme_assets/homepage.png">
 <img width=49% src="readme_assets/moviepage.png">

<!-- under development -->
## 🔗 Links for project:
 Video link : [Not made](Not made)  

## 🌐 Web flow
<!-- under development -->
<img width=80% src="readme_assets/interface-flowchart.png">
<img width=80% src="readme_assets/dataapi-flowchart.png">



## 🚩 Agile methology and workflow:

Agile methology was followed by implementation of 
KNN algorithm on the PCA transformed data which is pre-processed in the jupyter-notebook.
The methods were performed using git version control system and successfully developed patches which were merged to main branch. Methods were performed according to priority scale.
Priority scale : P5 (maximum) to P1 (Least)
| Week | Task | Remarks |
|---|---|---|
| 1 | **Design app phase**  <br><br>P4: Build basic app layout in Django templates and exploring technologies for data analysis. <br>  P3: Exploring the data** | Problem statement analyzed roughly |
| 2 | **Design layout phase**<br><br>P4: Analysis of data <br> P3: Exploring data tools and methods <br> P2: Cleaning and parsing of data <br> P1: KNN Model creation | Data analysed and complexity evaluated  |
| 3 | **DataAPI Implementation phase** <br><br>P5: Model trained after StandardScaling and dimensionality reduction (PCA) <br> P4: Views (Django) for interface implemented <br> P4: Views (Dataapi) for API implemented <br> P3: Templates (Django) are laid for proper viewing in HTML.  | Major functionalities are added which consists of K Nearest Neighbours and other rating based sorting algorithms. |
| 4 | **CSS and Interface Implementation phase**<br><br>P5: Bugs reduced <br> P4: CSS Improved <br> P3: Non-Major Functionalities added | Overall improvement in UX/UI of the app |
## 🚩 Features:
List of Feature at [./features.md](features.md)
Features | Images
------------ | -------------
 **Homepage** <br>Interact with movies, watch movie details, made with CSS \| Javascript \| JQuery | Mouse hover<br>![image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/hoverviewindex.gif?raw=true)
 **Moviepage** <br> A dedicated page to movie where user can interact with ratings and affect the paging |White board ![image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/moviepage.png?raw=true) | 
Search movies in Navigation bar| ![Mute Unmute](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/search.png?raw=true) 
User authentication system | **Logged In** ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/loggedin.png?raw=true) <br> **Log Out from here** ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/logout.png?raw=true) <br> **Logged Out and can Sign in or Sign up again** ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/loggedout.png?raw=true)
 <br><center>**User logged in**<center> ![image](https://user-images.githubusercontent.com/56452820/125260613-225d5c80-e31e-11eb-868b-623f90b9a1a5.png)| <center>**User logged out**<center> ![image](https://user-images.githubusercontent.com/56452820/125260014-87fd1900-e31d-11eb-9839-72cf59a75020.png)

**Other Features :**
Users can independently:
1. chose to stop or resume video of any particpants 
2. mute or unmute its audio and decrease f increase volume
3. view on fullscreen as well  

##  🚩 Technologies used:
#### Programming Languages : <img alt="NodeJS" src="https://img.shields.io/badge/node.js-%2343853D.svg?style=for-the-badge&logo=node-dot-js&logoColor=white"/><img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/> <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/> <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/><img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/><img alt="jQuery" src="https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white"/>  
#### Version Control : <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>  
#### Hosting : <img alt="Azure" src="https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white"/> <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>
####  Frameworks/Libraries : Express , Ejs , Socket.io , Peerjs, UUID
###### You can also see the list of dependencies in the package.json file.
## 🚩Installation/Environment Setup 

  #### 1. Clone App
  
  * Make a new folder and open the terminal there.
  * Write the following command and press enter.
  
  ```
    $ git clone https://github.com/hkaur008/microsoft-engage-project.git
  ```
    
 #### 2. Install node packages
  * Write the following command and press enter to download all required node modules.
 
   ```
   $ npm install 
  ```
  
#### 3. Run Locally

 * While you are still inside the cloned folder, write the following command to run the website locally. 
 
 ```
   $ npm start
 ```
  
 ###### NOTE: The port by default will be ```http://localhost:443/```

## 🚩 Future Scopes:-
Feature | Explanation
------------ | -------------
Specific Team group Atmosphere manager| As Teams is a chat conversational platform as well, wanted to build a chat room positivity meter to analyse chat text to extract user sentiments and emotional state during the conversation using Microsoft Cognitive Services or ML APIs.    
Send Code integration | A microsoft teams inspired feature for developers to work in collabrative environment and code together.
Blind mode | Switching to this mode user will hear the tool description through audios, and can video call their families as well.

Thank you ! Microsoft Team for such a wonderful mentorship program ❤️
You can also check [My weekly record during this program](https://docs.google.com/document/d/17KTl62Htz-D9crD_tCRvy3G41SqS5Lw5Vvjkq5Fu2qM/edit?usp=sharing)
