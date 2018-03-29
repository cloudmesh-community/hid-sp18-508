
## MongoDB Tutorial

**THIS IS A DRAFT AND NOT COMPLETED YET**

Some steps are copied from <https://www.tutorialspoint.com/mongodb/mongodb_environment.htm/>


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

    
MongoDB is an open-source document database and NoSQL database, which is written in C++. A document is a set of key-value pairs. The table shows the difference between RDBMS terminology and MongoDB.
 
 

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

Run the following command to import the MongoDB public GPG key −

    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
    
 
Create a /etc/apt/sources.list.d/mongodb.list file using the following command.

    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
    
Now issue the following command to update the repository −

    sudo apt-get update
    
Next install the MongoDB by using the following command −

    apt-get install mongodb-10gen = 2.2.3
    
Start MongoDB

    sudo service mongodb start
    
Stop MongoDB

    sudo service mongodb stop
    
Restart MongoDB

    sudo service mongodb restart
  
### MongoDB Suitable Occasions
The main goal of mongodb is to build a bridge between key/value storage (providing high performance and high scalability) and traditional RDBMS systems (rich functions), combining the advantages of both. Mongo applies to the following scenarios:
1. Website data: Mongo is very suitable for real-time insert, update and query, and has the replication and high scalability required for real-time data storage on the website.
2. Cache: Because of its high performance, mongo is also suitable as a caching layer for information infrastructure. After the system restarts, the persistent cache built by mongo can avoid overloading the underlying data source.
3. Large-size, low-value data: Using traditional relational databases to store some data may be expensive. Before that, many programmers would choose traditional files for storage.
4. Highly scalable scenario: mongo is very suitable for a database consisting of tens or hundreds of servers.
5. Storage of objects and JSON data: The mongo BSON data format is very suitable for document formatted storage and query.

### MongoDB Unsuitable Occasions
1. A highly transactional system: for example, a bank or an accounting system. Traditional relational databases are still more suitable for applications that require a large number of atomic complex transactions.
2. Traditional business intelligence applications: BI databases that target specific issues can produce highly optimized queries. For such applications, data warehousing may be a more appropriate choice.
3. Requires SQL issue.

### Comparison of MySQL and MongoDB Design Examples
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
