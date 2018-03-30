
## MongoDB Tutorial

**THIS IS A DRAFT AND NOT COMPLETED YET**

Some steps are copied from <https://www.tutorialspoint.com/mongodb/mongodb_environment.htm/>

If you already learned about Mysql, you can jump to the last section "Comparison of MySQL and MongoDB Design Examples" to get some simple idea about MongoDB.

The example in Section ~\ref{s:comparison} is copied from <https://huoding.com/2011/06/08/84> 


### Overview
The definition is retrieved from <https://docs.mongodb.com/manual/introduction/>

"MongoDB is an open-source document database that provides high performance, high availability, and automatic scaling.  MongoDB documents are similar to JSON objects. The values of fields may include other documents, arrays, and arrays of documents."

Generally, there are four kinds of database, key-value stores, big table clones, document database abd graph databases. And MongoDB is one of the Document Database. In key-value stores database, we have to use key to do read and wrtie. Although mongodb has a set of key-value pairs in its document, we do not know keys to read and get data.  The following table shows the diffience between MongoDB and regular RDMBS(Relational database management system).

### MongoDB Conceptual Analysis

| RDBMS      | MongoDB            | 
| -----------| ------------------ |
| Database   | Database           | 
| Table      | Collection         |
| Tuple/Row  | Document           |
| column     | Field              |
| Table Join | Embedded Documents |
| Primary Key| Primary Key        | 

DataBase
A mongodb can create multiple database. The default database in MongoDB is "db", which is stored in the data directory. A single instance of MongoDB can accommodate multiple independent databases, each with its own set and permissions, and different databases are also placed in different files.
"show dbs" can show all database list.


### Advantages of MongoDB over RDBMS 

- Schema less − MongoDB is a document database in which one collection holds different documents. Number of fields, content and size of the document can differ from one document to another.

- Structure of a single object is clear.

- No complex joins.

- Deep query-ability. MongoDB supports dynamic queries on documents using a document-based query language that's nearly as powerful as SQL.

- Tuning.

- Ease of scale-out − MongoDB is easy to scale.

- Conversion/mapping of application objects to database objects not needed.

- Uses internal memory for storing the (windowed) working set, enabling faster access of data.

### Install MongoDB on Ubuntu

Run the following command to import the MongoDB public GPG key

    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
    
 
Create a /etc/apt/sources.list.d/mongodb.list file using the following command.

    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
    
Now issue the following command to update the repository

    sudo apt-get update
    
Next install the MongoDB by using the following command

    apt-get install mongodb-10gen = 2.2.3
    
Start MongoDB

    sudo service mongodb start
    
Stop MongoDB

    sudo service mongodb stop
    
Restart MongoDB

    sudo service mongodb restart

### Start Using MongoDB
Following commands are retrieved from <https://docs.mongodb.com/manual/tutorial/getting-started/>
First, db.collection.insertMany() can insert multiple documents into a collection. Pass an array of documents to the method.
  
    db.inventory.insertMany([
    // MongoDB adds the _id field with an ObjectId if _id is not present
    { item: "journal", qty: 25, status: "A",
        size: { h: 14, w: 21, uom: "cm" }, tags: [ "blank", "red" ] },
    { item: "notebook", qty: 50, status: "A",
        size: { h: 8.5, w: 11, uom: "in" }, tags: [ "red", "blank" ] },
    { item: "paper", qty: 100, status: "D",
        size: { h: 8.5, w: 11, uom: "in" }, tags: [ "red", "blank", "plain" ] },
    { item: "planner", qty: 75, status: "D",
        size: { h: 22.85, w: 30, uom: "cm" }, tags: [ "blank", "red" ] },
    { item: "postcard", qty: 45, status: "A",
        size: { h: 10, w: 15.25, uom: "cm" }, tags: [ "blue" ] }
    ]);

In the terminal, we will get 

    {
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("5abe85cda3f0937642940210"),
                ObjectId("5abe85cda3f0937642940211"),
                ObjectId("5abe85cda3f0937642940212"),
                ObjectId("5abe85cda3f0937642940213"),
                ObjectId("5abe85cda3f0937642940214")
        ]
    }

Then, to select all documents in the collection, pass an empty document as the query filter document to the db.collection.find() method:

In the terminal, we will get

    db.inventory.find( {} )
    { "_id" : ObjectId("5abe85cda3f0937642940210"), "item" : "journal", "qty" : 25, "status" : "A", "size" : { "h" : 14
    , "w" : 21, "uom" : "cm" }, "tags" : [ "blank", "red" ] }
    { "_id" : ObjectId("5abe85cda3f0937642940211"), "item" : "notebook", "qty" : 50, "status" : "A", "size" : { "h" : 8
    .5, "w" : 11, "uom" : "in" }, "tags" : [ "red", "blank" ] }
    { "_id" : ObjectId("5abe85cda3f0937642940212"), "item" : "paper", "qty" : 100, "status" : "D", "size" : { "h" : 8.5
    , "w" : 11, "uom" : "in" }, "tags" : [ "red", "blank", "plain" ] }
    { "_id" : ObjectId("5abe85cda3f0937642940213"), "item" : "planner", "qty" : 75, "status" : "D", "size" : { "h" : 22
    .85, "w" : 30, "uom" : "cm" }, "tags" : [ "blank", "red" ] }
    { "_id" : ObjectId("5abe85cda3f0937642940214"), "item" : "postcard", "qty" : 45, "status" : "A", "size" : { "h" : 1
    0, "w" : 15.25, "uom" : "cm" }, "tags" : [ "blue" ] }
We can see that although we do not define keys for our documents, they have their own ObjectId when they are inserted into MongoDB. And we can eaily insert them and get them all. And we can also easily get data without knowing anything about objectID.

To query for documents that match specific equality conditions, pass the find() method a query filter document with the <field>: <value> of the desired documents. The following example selects from the inventory collection all documents where the status equals "D":
 
    db.inventory.find( { status: "D" } )
    
In the terminal, we will get:

    { "_id" : ObjectId("5abe85cda3f0937642940212"), "item" : "paper", "qty" : 100, "status" : "D", "size" : { "h" : 8.5
    , "w" : 11, "uom" : "in" }, "tags" : [ "red", "blank", "plain" ] }
    { "_id" : ObjectId("5abe85cda3f0937642940213"), "item" : "planner", "qty" : 75, "status" : "D", "size" : { "h" : 22
    .85, "w" : 30, "uom" : "cm" }, "tags" : [ "blank", "red" ] }

That was so easy to get all objects which status is "D".

    
### Types of Data
The definition is retrieved from <https://docs.mongodb.com/manual/reference/bson-types/>
"BSON is a binary serialization format used to store documents and make remote procedure calls in MongoDB. Each BSON type has both integer and string identifiers as listed in the following:"

MinKey (internal type)

Null

Numbers (ints, longs, doubles, decimals)

Symbol, String

Object

Array

BinData

ObjectId

Boolean

Date

Timestamp

Regular Expression

MaxKey (internal type)


### Working with Python -- PyMongo
This section is retrieved from <https://api.mongodb.com/python/current/>
"PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python."
We recommend using pip to install pymongo on all platforms:

    python -m pip install pymongo
  
To upgrade using pip:

    python -m pip install --upgrade pymongo

The first step when working with PyMongo is to create a MongoClient to the running mongod instance. Doing so is easy:

    from pymongo import MongoClient
    client = MongoClient()
    
The above code will connect on the default host and port. We can also specify the host and port explicitly, as follows:

    client = MongoClient('localhost', 27017)
    
A single instance of MongoDB can support multiple independent databases. When working with PyMongo you access databases using attribute style access on MongoClient instances:

    db = client.test_database
    collection = db.test_collection
    
Now we can easily connect to MongoDB from Python, read, write, update and any aggregation function are all easy to finish in PyMongo. For more details, please see PyMongo's API <https://api.mongodb.com/python/current/>.


### Working with Python -- MongoEngine
MongoEngine is based on PyMongo.

install MongoEngine

        pip install mongoengine

However unlike PyMongo, beforing using that, we need define a document pattern first.

    class Adult(DynamicDocument):
         meta = {
            'collection': 'student',
            'strict': False
        }
        id = IntField()
        age = IntField()
        education = StringField()
        race = StringField()
        sex = StringField()
        salary = StringField()
        
Then, we can easily insert, update, remove or find data. The most difference between PyMongo and MongoEngine is that MongoEngine is Object-Oriented, it needs document pattern, and it directly inherited from the DynamicDocument class. While Pymongo is non-object-oriented. 
For more details, please see MongoEngine's API <http://docs.mongoengine.org/apireference.html>.

    

### Comparison of MySQL and MongoDB Design Examples

\label{s:comparison}
This section is retrieved from <https://huoding.com/2011/06/08/84> 

If using MySQL, the basic information of the mobile phone is a separate table, and because the parameter information of different mobile phones is very different, it also needs a parameter table to be saved separately.

    CREATE TABLE IF NOT EXISTS `mobiles` (
        `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(100) NOT NULL,
        `brand` VARCHAR(100) NOT NULL,
        PRIMARY KEY (`id`)
    );

    CREATE TABLE IF NOT EXISTS `mobile_params` (
        `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `mobile_id` int(10) unsigned NOT NULL,
        `name` varchar(100) NOT NULL,
        `value` varchar(100) NOT NULL,
        PRIMARY KEY (`id`)
    );

    INSERT INTO `mobiles` (`id`, `name`, `brand`) VALUES
    (1, 'iPhoneX', 'Apple'),
    (2, 'E7'   , 'Nokia');

    
    INSERT INTO `mobile_params` (`id`, `mobile_id`, `name`, `value`) VALUES
    (1, 1, 'Standby time', '200'),
    (2, 1, 'Design', 'Straight board'),
    (3, 2, 'Standby time', '500'),
    (4, 2, 'Design', 'Slider');
    
If you want to query the standby time is greater than 100 hours, and the design is a straight mobile phone, you need to query as follows:
    
    SELECT * FROM `mobile_params` WHERE name = 'Standby time' AND value > 100;
    SELECT * FROM `mobile_params` WHERE name = 'Design' AND value = 'Straight board';
    SELECT * FROM `mobiles` WHERE mobile_id IN (MOBILE_IDS);
  
If using MongoDB, if can be combined into one:
    
    db.getCollection("mobiles").ensureIndex({
        "params.name": 1,
        "params.value": 1
    });

    db.getCollection("mobiles").insert({
        "_id": 1,
        "name": "iPhoneX",
        "brand": "Apple",
        "params": [
            {"name": "Standby time", "value": 200},
            {"name": "Design", "value": "Straight board"}
        ]
     });

    db.getCollection("mobiles").insert({
        "_id": 2,
        "name": "E7",
        "brand": "Nokia",
        "params": [
            {"name": "Standby time", "value": 500},
            {"name": "Design", "value": "Slider"}
        ]
    });

If you want to query the standby time is greater than 100 hours, and the design is a straight mobile phone, you need to query as follows:

    db.getCollection("mobiles").find({
        "params": {
            $all: [
                {$elemMatch: {"name": "Standby time", "value": {$gt: 100}}},
                {$elemMatch: {"name": "Design", "value": "Straight boar"}}
            ]
        }
    });
    
In all, MySQL requires multiple tables, multiple queries to get the problem, MongoDB only needs a table.
