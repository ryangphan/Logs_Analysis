# PROJECT 3: Logs Analysis

### by Ryan Phan

Project Logs Analysis is a part of the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

The project consist of the following files:
  - newsdb.py : the python file contains the source code of this project
  - output.txt : a sample output this project will generate
  - README.md : guideline to run this project

### Installation

To run this project, you will need to successfully install these following software:
  - [Python 3](https://www.python.org/downloads/)
  - [Vagrant](https://www.vagrantup.com/)
  - [VirtualBox](https://www.virtualbox.org/)

Additionally, you need to have these files as well:
  - Download or clone this [repository](https://github.com/udacity/fullstack-nanodegree-vm)
  - Download, unzip this [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    and put it in the same folder as the one used to install the virtual machine

### How To Run This Project

  - Download and install Python3, and VirtualBox
  - Open the terminal on your computer and direct it to vagrant sub-directory inside the udacity-fullstack-vm folder
  - Installing Vagrant in the previous folder by using the following command
  ```sh
  $ vagrant up
  ```
  - It will took a while to install the virtual machine base on the speed of your internet.
  - After successfully installing the virtual machine, you can log in by using the command
  ```sh
  $ vagrant ssh
  ```
  - Redirect your virtual machine's vagrant folder by using command:
  ```sh
  $ cd /vagrant
  ```
  - To load the database, please use the following command:
  ```sh
  psql -d news -f newsdata.sql
  ```
  - Finally, to run the project, please use the following command:
  ```sh
  python3 newsdb.py
  ```

### Miscellaneous
This README document is based on a template suggested by PhilipCoach in this Udacity forum [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524/2)
