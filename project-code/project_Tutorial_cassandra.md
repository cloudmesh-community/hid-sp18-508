
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
    cqlsh:dev> create table train(uid int primary key,mid int,rate int); 
    cqlsh:dev> insert into train(uid,mid,rate) values(1,2,3);


### Using Cassandra with Python

Some steps are retrieved from <https://datastax.github.io/python-driver/>

To install the driver

    pip install cassandra-driver
    
   
