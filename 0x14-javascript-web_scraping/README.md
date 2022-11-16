# 0x14. JavaScript - Web scraping
## Resources
### Read or watch:
* [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://www.medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
* [request module](https://github.com/request/request)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)
* [Star Wars API](https://swapi-api.hbtn.io/)
## General
* Why JavaScript programming is amazing
* How to manipulate JSON data
* How to use `request` and fetch API
* How to read and write a file using `fs` module
## More Info
### Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```
### Install `request` module and use it
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
**N/B**: _Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry)._
