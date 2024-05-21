## The Website Doc 

### Requirements 

Check the requirements.txt file for the specific versions - 
```
python3 
Flask 
mongodb 
nginx 
pymongo 
aws ec2 (static ip)
```

### File structure : - 

```
mongo (the files that are used for the mongo data hnadling and insertion)
    - mongo_helper (the file connects the mongo client and the data and the has the methods to add , insert , update, delete and show in the database, the database )
    - read_data_json (the file is used to read the data from the json for the insertion in the mongodb)
    - data_handling (the data handling file is used to add and update the database as per requirement)
    - bulk_data_insertion (The file is used for the addition of the data from the json file read it delete all and then write the lastest data , the problem is currently add the data by deletion of all rather than modifications)


static (The static files of the website are here )
    - images (all images as per sections of the website)
        - icons (all icons)
        - misc (the dummy images)
        - profile (The profile pic)
        - projects (The project images are in the respective project folder)
        - tech (The images for tech section of the website)
    - Projects (The project section files)
        - Academic-Webiste (The website project files)
    - resume ( The current resume file )
    - project_article_data (The project data of the articles )
    - route_template_map (not being used right now )
    - section_data (The section data from the section page with tech , life and proeject for card stucture)
    - tech_article_data ( The tech data of the articles )
    - style ( The css file for webiste )

templates (the templates of the sites that render in the front end)
    - base ( the base template for the staring templates has the cdm links and  file links)
    - components ( the pages are different section of the website that can be designed one for particular pages as per name explanamable)
    - projects ( The arrtice page to display the articles )
        - article-body (the body section that has heading, image, para , markdown )
        - article ( the artcile rendering file )
        - extra file ( the dummy files to test )
    - reusable ( the reusable components of the webiste template )
    - about ( the about page)
    - index ( the index page )
    - section ( the section display page ) find the diff in the two
    - showcase ( the showcase page ) might not be in use anymore, check the live version now 

app ( the main flask file for runner and making end points)

exp ( an experiment file can be changed anytime as per needed )

form_data (the file to store the data from the message fields)

read_data_mongo (read the data from the mongo and fetch it for render )
```

### Redis installation commands (Linux)

```
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis


#redis connector 
pip install redis

```

## The commands to use (mostly linux based)



### The nginx command 

```

sudo apt update
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx

sudo nginx -t
sudo systemctl reload nginx

```

### The mongo commands

```
mongosh 
use your_database_name
show collections
db.dropDatabase()  #delete the dropDatabase
db.<collection_name>.drop()  #drop the 
db.my_collection.find() #show all the data in collection
```

### cert bot commands 

```
sudo yum install certbot python3-certbot-nginx
sudo certbot --nginx -d meabhi.me -d www.meabhi.me
sudo certbot --nginx -d meabhi.me
```

### The Flask commands 

```
python3 app.py 

to run on the server 
flask run --host=0.0.0.0 --port=5000


kil flask by 
ps aux | grep flask
kil pid

run the flask in background 
flask run --host=0.0.0.0 --port=5000 > output.log 2>&1 & disown
```


##  Nginx Configurations 

The nginx configuration file is used to make the nginx connect to the certbot files , put the domain name as well. The file location - 




```

server {
    listen 80;
    server_name www.meabhi.me;

    # Redirect HTTP to HTTPS
    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name www.meabhi.me;

    ssl_certificate /etc/letsencrypt/live/meabhi.me/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/meabhi.me/privkey.pem;

    # Other SSL configuration directives (e.g., SSL protocols, ciphers, etc.)

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

```


### Hosting process 

- Make a ec2 or t2 micor with ubunut any instance in AWS 
- Assign the ip address 3.128.143.84 in the Ec2 instance. 
- Assign the ip address in godaddy dns management pannel
- The certbot certifiction is made for https 
- Add the nginx config file that has the DNS and certification link 
- The config file is in this link /etc/nginx/nginx.conf


## Some common logic for website 

### MongoDb (database)

- The data is stored in forms of the documents 
- Two data bases are made named "articles" and "section"
    - articles is the database to store the article data 
    - articles has 3 collection inside the database 
    - "project" to store the project article data
    - "tech" to store the tech article data 
    - "life" to store the life article data
- The section database to store the section data 
    - The collection "section_data" is used to store the section data 
    - The "section_data" is stored with the data from life, project and tech page


### The App file (main flask file)

- The main flask file is app.py that run the flask server 
- The imports are from mongo to read the data from mongodb and help it render in the front end 
- The db_name and collections is a list that have the names of the mongo database defined and the collections named defined as well 
- static foler is passed as well 
- the index and the about just render the data from the page nothing fetched from mongodb 
- section function render the data from the mongdb as per page 
- project and tech function works the same and just render the data from the database using the article.html and article_body.html
- the project_demo works with rendering the demo website which are made and render the website files 
- store_from_data is used to store the data from the front end to the back end and jsonify it and store it in file form_data.json


### The logics of the page 

- Some the pages are static as the index page and the about page 
- The mongosb plays the main role in the database storage and fetching the data is done from the mongodb 
- most of the components of the page are resualble and data can be passed to them either through mongodb or manually 
- The database has 2 database and 4 collections
- the articles database has 3 collections tech, project and life
- the section database has 1 collection section_data that stores the section data for section page with page can be tech,  life and project
- Some small css and JS logic are defined on the page where the code is written for the page on the go 
    - #### CSS classes 
    - background-color-body - it's used for the body color that on the upper body and on components 
    - main-container-color - the main container color is the blue color for the main components 
    - font-color-class - is the blue color as the main container color but darker tone 
    - bio-color - the background color the darker grey in the background color 
    - bio-font - used for heading 
    - arial-font - might not be used to check on that
    - ### The color design 
    - The background color - #ffffff
    - The blue body color - #19A7CE
    - The font color blue - #146C94
    - The container color is - #ffffff
    - The footer header color is - #e9ecef
    - The icon color is - black

























### Links 

```
https://www.digitalocean.com/community/tutorials/understanding-the-nginx-configuration-file-structure-and-configuration-contexts


```
