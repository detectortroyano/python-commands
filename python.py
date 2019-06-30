# Creamos un directorio base para almacenar repositorios, se recomienda a la altura de HOME,
# Instalamos virtualenv Entornos virtuales (Una caja para cada proeycto que peuda tener)
# Instalar siempre sobre un entorno activado, caso contrario estas afectando las lib globales de python
#(Activa el Entorno, el Promt Cambia)
$ source ~/.virtualenvs/as400Drive/Scripts/activate
$ source ~/.virtualenvs/integrity/Scripts/activate
$ source ~/.virtualenvs/descargas/Scripts/activate


python repositorios/as400Drive/jt400fs.py
python repositorios/as400Drive/jt400call.py
python repositorios/as400Drive/jt400spool.py
python repositorios/as400Drive/files/ftp.py


python ~/git/integrity-iaccess/database/crud_select.py
python ~/git/integrity-iaccess/database/stored.py
python ~/git/integrity-iaccess/database/transaction.py
python ~/git/integrity-iaccess/database/stored_select.py
python ~/git/integrity-iaccess/database/stored_out.py



----INSTALL JAVA IF NOT EXISTS----
$ sudo apt-get update
$ java -version
if returns "The program java can be found in the following packages" you need install JAVA
$ sudo apt-get install default-jdk
or
$ sudo apt-get install python-software-properties
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer

----CONFIGURAR JAVA_HOME----
$ sudo update-alternatives --config java
$ sudo nano /etc/environment
edit el archivo /etc/environment
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java"
Ctrl-X and then Y to save the changes, finally Enter
$ source /etc/environment
$ echo $JAVA_HOME

----INSTALL C++ COMPILER IN UBUNTU----
$ python -version
$ sudo apt-get install python3 python-dev python3-dev
$ sudo apt-get install python-dev

----PIP INSTALL----
$ sudo apt-get install python-pip


----INSTALL VIRTUALENV
$ sudo apt-get install virtualenv python-virtualenv
Pip => $ pip install virtualenv
$ cd ~
$ mkdir .virtualenvs
$ cd .virtualenvs
$ virtualenv as400Drive
$ source ~/.virtualenvs/as400Drive/bin/activate
Windows => $ source ~/.virtualenvs/as400Drive/Scripts/activate 

----INSTALL JAYDEBEAPI----
$ pip install JayDebeApi

----CLONE REMOTE BRANCH REPOSITORY----
$ cd Downloads
$ git clone -b avega git@gitlab.com:nomiservicios/integrity-iaccess.git
$ cd integrity-iaccess


----DESACTIVATE VIRTUALENV----
$ deactivate

----CHANGE PYTHON VERSION----
$ python --version
$ alias python='/usr/bin/python3'
$ python --version


----INSTALL JAYDEBEAPI IN VIRTUALENV WITH PIP, PYTHON_COMPILER AND JAVA_HOME EXISTS----
$ cd ~
$ mkdir .virtualenvs
$ cd .virtualenvs
$ virtualenv venv
$ source ~/.virtualenvs/venv/bin/activate
$ pip install JayDebeApi

----EJEMPLO JAYDEBEAPI IN UBUNTU
vmubuntu@ubuntu:~$ cd ~
vmubuntu@ubuntu:~$ mkdir .virtualenvs
mkdir: cannot create directory ‘.virtualenvs’: File exists
vmubuntu@ubuntu:~$ cd .virtualenvs
vmubuntu@ubuntu:~/.virtualenvs$ virtualenv venv
Running virtualenv with interpreter /usr/bin/python2
New python executable in /home/vmubuntu/.virtualenvs/venv/bin/python2
Also creating executable in /home/vmubuntu/.virtualenvs/venv/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
vmubuntu@ubuntu:~/.virtualenvs$ source ~/.virtualenvs/venv/bin/activate
(venv) vmubuntu@ubuntu:~/.virtualenvs$ pip install JayDebeApi
Collecting JayDebeApi
  Using cached https://files.pythonhosted.org/packages/87/e2/a84253efa32c104256d44731513b8d8b7e47a890b6e44fb42c54688a5dc2/JayDeBeApi-1.1.1-py2-none-any.whl
Collecting JPype1 (from JayDebeApi)
Installing collected packages: JPype1, JayDebeApi
Successfully installed JPype1-0.6.3 JayDebeApi-1.1.1
(venv) vmubuntu@ubuntu:~/.virtualenvs$ 

----RUN WEB APP----
$ pip install django==1.8
$ pip install django-cors-headers==2.1.0
$ pip install djangorestframework==3.1.0
$ pip install django-wkhtmltopdf==2.0.2
$ pip install polib==1.0.7
$ pip install django-filter==0.10.0
$ pip install python-dateutil==2.4.2
$ pip install suds-jurko==0.6
$ pip install zeep==2.5.0
$ pip install xlrd==0.9.3

$ python manage.py runserver