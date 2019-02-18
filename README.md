<p align="center">   
<img src="https://raw.githubusercontent.com/anongrp/hyperlite/master/docs/assets/logos/Hyperlite%20logo%20500x500.png">
</p>

<h align="center">
 
 [![Status](https://img.shields.io/badge/hyperlite-underdevelopment-blue.svg)](https://github.com/anongrp/hyperlite/releases)
 [![Build Status](https://travis-ci.org/anongrp/hyperlite.svg?branch=master)](https://travis-ci.org/anongrp/hyperlite)
 [![Version](https://img.shields.io/pypi/v/nine.svg)]
 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

 </h>


Hyperlite is an event based and NoSql realtime database that provides a simple way to store and manage complex data. It works on non blocking mechanism. In Hyperlite, data is stored into objects, fields, and collections, and it is auto indexed to make it easier to find relevant information.
It works on RIDU Operation which can be done by **HyperQl**, the standard Hyperlite database query language that makes it easier to communicate with the database. Hyperlite offers excellent concurrency, high performance, and powerful language support for storage and subscriptions. It can be used in any complex and real time production systems.

## Why Hyperlite ?...
* Lightweight 
* Simple languge for querying Complex data (HyperQl)
* Fast and Secure 
* Complex data that Roar 
* No Document size limit
* Provide Realtime communication out of the Box 
* No server required (it can work as a backend) 
* Schema and Schema-Less
* Works asynchronously

## Introduction To HyperQl
`Like a query language unlike sql language`
HyperQl(Hyper Query Language) is an official query laguage for comunicating with database. hyperQl is specially designed for Hyperlite database.
#### Types of HyperQl
* Selective HyperQl
    : In this type of query, user write a query for selecting the fields. It is same as WHERE clause in SQL.
* View HyperQl
    : In this type of query, user write a query for viewing the data. It is same as SELECT in SQL.

for more info, check out Hyperql official document.

### Operations
 As we know, that Hyperlite works on RIDU, instead of CRUD operations. RIDU means read, insert, update and delete, and one more extra operation is 'Subscriptions'. That means, in hyperlite total five types of operations are available for client, so we can say that it works on RIDUS right! YES! ...BUT No, you can't, because officially we don't include it as an operation even though it is an operation but it is not quick operation, it's a long running opertion that runs forever while client has not unsubscribed it or server is not responding or may crash (system, not server; because hyperlite server will never crash). 
 for more info check out Subscriptions in official documentation.

| Operation | Description |
| ----------- | ----------- |
| R | Read : query the data |
| I | Insert : Insert or store data |
| D | Delete : Delete or drop data |
| U | Update : Update or patch already stored data|

## License

Hyperlite is GNU GPL v3.0 licensed, as found in the LICENSE file.
