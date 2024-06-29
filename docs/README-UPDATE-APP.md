
## Deploy the Updated application

ssh into the server:

ssh root@aq-qaida-sanctions.com

Clone the git repo (using HTTPS):

git clone https://github.com/johnfkraus/al-qaida-sanctions.git

cd into project

install dependencies

npm i

wait..wait..wait

??
sudo npm i pm2 -g

pm2 start index.js

sudo service nginx restart


## Minor update: deploy the data.js file

scp data.js root@al-qaida-sanctions.son:/root

ssh root@al...

cp data.js az-list-viz/

sudo service nginx restart

