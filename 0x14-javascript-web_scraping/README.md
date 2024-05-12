# 0x14. JavaScript - Web scraping
## Resources
* [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://www.medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
* [request module](https://github.com/request/request)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)
* [Star Wars API](https://swapi-api.hbtn.io/)
## Project Objectives
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
## Tasks
### [0.Readme]():
A script that reads and prints the content of a file.
File path is passed as first argument and the content of the file is 
read in `utf-8`. If an error occurs, during the reading the error 
object is printed.
**Usage:**
```
eyakenojnr@ubuntu:~/0x14$ cat cisfun
C is super fun!
eyakenojnr@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

eyakenojnr@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
eyakenojnr@ubuntu:~/0x14$ 
```
