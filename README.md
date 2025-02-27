# AreaCode
Flask group project
## Author
- John Njau
- Florence Wangechi
- Susan Mageto
- Gladys Wambura
- 
## Description
- This is a Social media website which connects individuals within a geographical area to discuss, update, socialize and network within the confines of the specific area code.
![image](https://user-images.githubusercontent.com/97955649/169469461-9a369d6f-09f8-4590-9c75-c5f26f71f0db.png)

![image](https://user-images.githubusercontent.com/97955649/169468370-2c2096ca-8999-4e4e-9fcd-7e1bb51f1c50.png)

## User Story in Pictures
####  User view
* User can register and login into the site
* User can create posts on the site
* User can comments on the posts
* User can create a profile
* User can update their profile
* 
## Behavior Driven Development             |
| user register && login      | Take you to home page           | Redirect you to the Homepage                 |
| Create a blog post by filling post form          | Write your  post it     | Your blog is displayed  in home page                     |
| User comment on the post  | Write your feedback and post it | Your feedback is displayed under the blog post   |                 |             |
## Technologies Used
* Python
* Flask
* PostgreSQL
* SQLAlchemy
* HTML5
* CSS3
* Javascript
* Bootstrap
* jQuery
## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example:
    * **`pip install flask`**
    ## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/catherine244/Blog.git**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL databse client.
* **Step 5** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
    * Create a file in your root directory called start.sh and store a generated SECRET key like so **`export SECRET_KEY="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`**
* **Step 6** : On your terminal, run the following command, **`chmod a+x start.sh`**
    * You can now launch the application locally by running the command **`./start.sh`**
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.
## Contacts
**gladyswahito7@gmail.com**
**gflorencewambui@gmail.com**
**johnnjaunjoroge@gmail.com**
**susanmageto.mageto@gmail.com**

## live link
[https://.herokuapp.com/](https://areacodesz.herokuapp.com/)
## License
#### [*GNU License*](LICENSE)
