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
| Week | Task                                                                                                                                                                                                                                                                                | Remarks                                                                                                           |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1    | **Design app phase**  <br><br>P4: Build basic app layout in Django templates and exploring technologies for data analysis. <br>  P3: Exploring the data**                                                                                                                           | Problem statement analyzed roughly                                                                                |
| 2    | **Design layout phase**<br><br>P4: Analysis of data <br> P3: Exploring data tools and methods <br> P2: Cleaning and parsing of data <br> P1: KNN Model creation                                                                                                                     | Data analysed and complexity evaluated                                                                            |
| 3    | **DataAPI Implementation phase** <br><br>P5: Model trained after StandardScaling and dimensionality reduction (PCA) <br> P4: Views (Django) for interface implemented <br> P4: Views (Dataapi) for API implemented <br> P3: Templates (Django) are laid for proper viewing in HTML. | Major functionalities are added which consists of K Nearest Neighbours and other rating based sorting algorithms. |
| 4    | **CSS and Interface Implementation phase**<br><br>P5: Bugs reduced <br> P4: CSS Improved <br> P3: Non-Major Functionalities added                                                                                                                                                   | Overall improvement in UX/UI of the app                                                                           |
## 🚩 Features:
List of Feature at [./features.md](features.md)
| Features                                                                                                | Images                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Homepage** <br>Interact with movies, watch movie details, made with CSS \| Javascript \| JQuery       | Mouse hover<br>![image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/hoverviewindex.gif?raw=true)                                                                                                                                                                                                                                                                                                 |
| **Moviepage** <br> A dedicated page to movie where user can interact with ratings and affect the paging | White board ![image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/moviepage.png?raw=true)                                                                                                                                                                                                                                                                                                         |
| Search movies in Navigation bar                                                                         | ![Mute Unmute](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/search.png?raw=true)                                                                                                                                                                                                                                                                                                                  |
| User authentication system                                                                              | <br>**Logged In** ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/loggedin.png?raw=true) <hr><br> **Log Out from here** ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/logout.png?raw=true) <hr> <br>**Logged Out and can Sign in or Sign up again** ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/loggedout.png?raw=true) |
| Contact for queries of users                                                                            | ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/contact.png?raw=true)                                                                                                                                                                                                                                                                                                                       |
| Change password or overview your Profile                                                                | ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/overview.png?raw=true)                                                                                                                                                                                                                                                                                                                      |
| Rate movies                                                                                             | ![Image](https://github.com/prabhavagrawal7/watchnow/blob/master/readme_assets/ratemovie.png?raw=true)                                                                                                                                                                                                                                                                                                                     |

**Other Features :**
Users can
1. Change some sections of their profile (Email change).
2. Get recommendations based on which movies they rated well.
3. Contains administration section which can control other profiles. 
4. The data includes movies from 2000–2019, so users will know more about them.

##  🚩 Technologies used:
#### Programming Languages : ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
#### Version Control : ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)  

####  Frameworks/Libraries : ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
#### Refferences used : ![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white)
Data & API source: <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" height="16px">
#### Acknowledgements
========================

We would like to thank GroupLens for providing us with the dataset and code for the regression algorithm [Vig et al., 2012]. We would also like to thank organizations that supported publication of this dataset: the Academy of Finland, grant #309495 (the LibDat project) and the Academy of Finland Flagship programme: Finnish Center for Artificial Intelligence FCAI.

###### You can also see the list of python dependencies in requirements.txt file.

## 🚩Installation/Environment Setup 
  Note that python --version should be 3.6 and above
  #### 1. Clone App
  * Make a new folder and open the terminal there.
  * Write the following command and press enter.
  
  ```
    $ git clone https://github.com/prabhavagrawal7/watchnow.git
  ```
  ### 2. Get inside **watchnow** folder
  ``` 
  $ cd watchnow
  ``` 
  ### 3. Create and activate virtual environment with Virtualenv
  * For linux/unix users :  
```
$ python3 -m pip install --user virtualenv
$ python3 -m venv env
$ source env/bin/activate
``` 
  * For windows users : 
```
$ py -m pip install --user virtualenv
$ py -m venv env
$ .\env\Scripts\activate
```
  ### 4. Install python requirements by following command
  * For linux/unix users :  ```pip3 install -r requirements.txt```
  * For windows users : ```pip install -r requirements.txt```
  ### 5. Migrate database from manage.py
  * For linux/unix users
  ``` 
  $ python3 manage.py makemigrations
  ``` 
  * For windows users 
  ```
  $ python manage.py makemigrations
  ```
  ### 6. Now Run the server as usual
  * For linux/unix users
  ``` 
  $ python3 manage.py runserver
  ``` 
  * For windows users 
  ```
  $ python manage.py runserver
  ```
## 🚩 Future Scopes:-
| Feature                                                                                                                                                                                                                       | Explanation                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Links of subscription providers where you can rent or buy movie                                                                                                                                                               | It will help user to directly find the movie and watch it convinently |
| Instead of adding one trailer link, there are multiple trailers and teasers too                                                                                                                                               | It will eventually increase user convinence                           |
| The data is static, i.e. more movie data can't be added due to project size constraints, instead making it dynamic by fetching movies from internet using TMDb API and the ratings data is being taken directly from the user | The data will become dynamic so the project can be made for long run  |


Thank you ! Microsoft Team for such a wonderful mentorship program ❤️
