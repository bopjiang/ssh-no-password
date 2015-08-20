# ssh-no-password

a [Fabric](http://www.fabfile.org/) script configurates remote SSH servers, to support login using SSH Keys.

### usage
- generate SSH keys locally
~~~bash
$ssh-keygen  -t rsa -C "your_email@youremail.com" 
~~~
- install Fabric
- change ssh user/password in config.py, add host and ip

- go
~~~
$fab nopassword
~~~
