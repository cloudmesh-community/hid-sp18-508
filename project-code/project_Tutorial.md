
## MongoDB Tutorial


Some steps are retrieved from <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>

### Install MongoDB Community on Ubuntu

Import the public key used by the package management system

    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
    
 
Create a list file for MongoDB

   echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
    
Reload local package database

    sudo apt-get update
    
Install the MongoDB packages, Install the latest stable version of MongoDB.

    sudo apt-get install -y mongodb-org
    
Run MongoDB Community Edition

    sudo service mongod start
    
Stop MongoDB

    sudo service mongod stop
    
Restart MongoDB

    sudo service mongod restart

### Start Using MongoDB in ubuntu

Batch processing

    mongoimport --type csv --headerline --file songs_id.csv
    
    we get following 
    
        2018-04-15T11:06:07.675-0400	no collection specified
        2018-04-15T11:06:07.675-0400	using filename 'songs_id' as collection
        2018-04-15T11:06:07.719-0400	connected to: localhost
        2018-04-15T11:06:10.717-0400	[########................] test.songs_id	7.63MB/21.1MB (36.2%)
        2018-04-15T11:06:13.683-0400	[#################.......] test.songs_id	15.3MB/21.1MB (72.9%)
        2018-04-15T11:06:16.042-0400	[########################] test.songs_id	21.1MB/21.1MB (100.0%)
        2018-04-15T11:06:16.044-0400	imported 419781 documents




