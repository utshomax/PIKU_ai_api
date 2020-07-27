<p align='center'><a href="https://pikuai.herokuapp.com"><img src="https://i.ibb.co/TBS16nM/piku-logo.png" alt="piku-logo" border="0"></a></p>

<h2 align="center">Piku API with flask </h2>

<p align="center"> GET REPLAY FROM PIKU - DEEPLEARNING CHATBOT WITH API</p>

<p align='center'>
 <a href="https://pikuai.herokuapp.com"><img src="https://img.shields.io/badge/API-YES-lightgrey" alt="API" border="0"></a>
 <a href="https://github.com/utshomax/PIKU_ai_api/releases/tag/1.0.1"><img src="https://img.shields.io/badge/VERSION-v1.0.1-yellowgreen" alt="Version" border="0"></a>
 <a href="https://www.tensorflow.org/versions/r1.15/api_docs/python/tf"><img src="https://img.shields.io/badge/Tensorflow-v1.8.0-brightgreenI" alt="Version" border="0"></a>
 <a href="https://devcenter.heroku.com/articles/git"><img src="https://img.shields.io/badge/Heroku-success-blue" alt="piku" border="0"></a>
 </p> 
 <p align="center">
    <a href="#usage">Usages</a>
    ·
    <a href="https://github.com/utshomax/PIKU_ai_api/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/utshomax/PIKU_ai_api/issues/new/choose">Request Feature</a>
  </p>
  



## 🧬PIKU is an implementation of Deeplearning Model with Tensorflow and Flask

**API Feature implemented with Flask**
<!-- ABOUT THE PROJECT -->
## About The Project

PIKU is a chatboot which can reply to your Question with the help of Deeplearning. Also it can be diployed to Heroku directly with the help of Gunicorn.

⛱️Features
* Direct conversetion
* API Feature
* On web(For embed code)

ℹ️ Documentetion and Info

- **Website:** https://pikuai.herokuapp.com
- **Documentation:** https://pikuai.herokuapp.com
- **Source code:** https://github.com/utshomax/piku_ai
- **Bug reports:** https://github.com/utshomax/piku_ai/issues
<!-- GETTING STARTED -->
## Getting Started

**Piku can run on your local machine or You can use redimate API**



### ⚠️Prerequisites

Full list Avilabe in requirements.txt file.

* TensorFlow == 1.8.0
* Tflearn ==0.3.2
* **Python == 3.6.10**
* Nltk == 3.3
* Numpy == 1.16.4(To avoid Wornings)
* Flask
* Flask-SqlAlchemy

To install All prerequisites, nevigate to Project Folder. Then:

```sh
pip install -r requirements.txt
```

### 💽Installation
**Ignore if you want to use the redimate API . See ```Usage``` for Simple Use**

 🖥️**Local Machine Installation**

**Clone or Download the Repo**

```sh
git clone https://github.com/utshomax/piku_ai.git
```

1. Install All Prerequisties First

2. Nevigate to project folder

3. Train piku 

```sh
python train.py
```
4. Strat App 

```sh
python app.py
```
**App will run on your computer's ip address with the port 5000**

To get your IP:

Windows User:

https://support.microsoft.com/en-in/help/4026518/windows-10-find-your-ip-address

Mac User:

https://www.macworld.co.uk/how-to/mac/ip-address-3676112/

Linux User:

You know that

[![codecov](https://img.shields.io/badge/Heroku-success-blue)](
    https://devcenter.heroku.com/articles/git)
### **☁️Heroku Deploy**

Download of clone the Repo and Follow the instruction from bellow link to deploy using Heroku CLI.

[Instructions](https://devcenter.heroku.com/articles/git)

## Usage

**🤵Devloper**

**1.** Get a API key at [https://pikuai.herokuapp.com](https://pikuai.herokuapp.com)

**2.** Getting a reply from piku:

Method:GET

```sh
https://pikuai.herokuapp.com/conv/your_api_key?getReply=your_message
```
Response:JSON

```sh
{
  "reply": "a_reply_from_piku"
}
```
Example:
```sh
https://pikuai.herokuapp.com/conv/UgbnTrbkKPRqJt0wEEFqyGRbv2w?getReply=hi
```
Response:JSON

```sh
{
  "reply": "Hi there, how can I help?"
}
```
**👨‍💻Advenced Devloper(On local machine)**

Replace your_ip_address with your ip address

**1.** Get a API key at [https://pikuai.herokuapp.com](https://pikuai.herokuapp.com)

**2**. Getting a reply from piku:

Method:GET

```sh
https://your_ip_address_with_port/conv/your_api_key?getReply=your_message
```
Response:JSON

```sh
{
  "reply": "a_reply_from_piku"
}
```
Example:
```sh
http://192.168.198.104:5000/conv/UgbnTrbkKPRqJt0wEEFqyGRbv2w?getReply=hi
```
Response:JSON
```sh
{
  "reply": "Hi there, how can I help?"
}
```
**3.** Getting your info:

Method:GET

```sh
http://192.168.198.104:5000/info/your_api_key
```
Response:JSON

```sh
{
  "user": {
    "api_key": "your_api_key",
    "password": "your_password",
    "username": "your_uusername"
  }
}
```
Example:
```sh
http://192.168.198.104:5000/info/UgbnTrbkKPRqJt0wEEFqyGRbv2w
```
Response:JSON

```sh
{
  "user": {
    "api_key": "UgbnTrbkKPRqJt0wEEFqyGRav2w",
    "password": "123456",
    "username": "utsho"
  }
}
```
**4.** Createing A User

Method:POST

```sh
http://192.168.198.104:5000/reg?uname=your_username&password=your_password
```
Response:JSON

```sh
{
  "api": "your_api_key",
  "message": "user created!"
}
```
**For more follow the Documentation**

**Save your API key in a safe place.**

### 📝TO DO

- [ ] Add More Training Data
- [x] API Intrigation with Flask
- [x] Getting user API with username and password
- [x] User Registration with API
- [ ] Fontend For train with custom training data
- [ ] Web Interface
- [ ] Android App Interface
- [ ] Try with Django
- [ ] On web(embed code)
- [ ] Desktop GUI

### 🛠️Contributions

Feel free to contribute

<!-- LICENSE -->
### ⚖️License

Distributed under the Apache License 2.0 . See `LICENSE` for more information.



<!-- CONTACT -->
### 📧Contact

Utsab Utsho - [FACEBOOK](https://fb.com/utsabutsho) - utsho9009@gmail.com

Project Link: [https://github.com/utshomax/piku_ai](https://github.com/utshomax/piku_ai)
