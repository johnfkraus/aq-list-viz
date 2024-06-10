
## Deploy the Updated application

ssh into the server:

ssh root@aq-qaida-sanctions.com

Clone the git repo:

git clone https://github.com/johnfkraus/aq-list-viz.git

cd into project

install dependencies

npm i

wait..wait..wait

??
sudo npm i pm2 -g

sudo service nginx restart


## Minor update: deploy the data.js file

scp data.js root@al-qaida-sanctions.son:/root

ssh root@al...

cp data.js az-list-viz/

sudo service nginx restart

