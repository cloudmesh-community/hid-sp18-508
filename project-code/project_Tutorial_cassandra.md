
## Cassandra Tutorial


Some steps are retrieved from <https://www.datastax.com/2012/01/working-with-apache-cassandra-on-mac-os-x/>

### Install Apache Cassandra on Mac OS X

Download Cassandra

    curl -OL http://downloads.datastax.com/community/dsc.tar.gz
    
 
Install Cassandra

    tar -xzf dsc.tar.gz
    
Then switch to the new Cassandra bin directory and start up Cassandra:

    cd dsc-cassandra-1.2.2/bin
    sudo ./cassandra
    
Now that you have Cassandra running, the next thing to do is connect to the server and begin creating database objects. 
This is done with the Cassandra Query Language (CQL) utility. CQL is a very SQL-like language that lets you create objects 
as you’re likely used to doing in the RDBMS world.

    ./cqlsh
    Connected to Test Cluster at localhost:9160.
    
For this brief introduction, we’ll just create a basic keyspace to hold some example data objects we’ll create:

    cqlsh> create keyspace dev
    ... with replication = {'class':'SimpleStrategy','replication_factor':1};
    
Let’s create a base table to hold train data:

    cqlsh> use dev;
    cqlsh:dev> create table test(uid varchar primary key); 
    cqlsh:dev> insert into test(uid) values('1');

### Install Apache Cassandra on Ubuntu 14.04
Some steps are retrieved from <https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-04>

Installing Cassandra

    echo "deb http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list

Add the public key using this pair of commands, which must be run one after the other
    
    gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
    gpg --export --armor F758CE318D77295D | sudo apt-key add -
    
Update the package database once again:
 
    sudo apt-get update

Finally, install Cassandra:

    sudo apt-get install cassandra
    
Starting Cassandra:
        
    sudo service cassandra status
    
 You will see:
    
    Cassandra is running
    
Connecting to the Cluster:

    sudo nodetool status
    
    cqlsh

### Using Cassandra with Python

Some steps are retrieved from <https://datastax.github.io/python-driver/>

To install the driver

    pip install cassandra-driver
    
   
