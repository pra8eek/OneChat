# Chat

>A multi user chat application based on socket programming

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-sharks.svg)](https://forthebadge.com)

[![PRs](https://img.shields.io/badge/PRs-Welcome-informational)](https://github.com/pra8eek/OneChat/)
[![Python3.6](https://img.shields.io/badge/python-3.6-success?logo=python)](https://www.python.org/downloads/release/python-360/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://github.com/pra8eek/OneChat/)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/pra8eek/OneChat/)  

## What is this?
This is a small chatroom type application which enables systems on the same network to communicate with each other.

## How it looks like!
Let's see a conversation between 2 stoners, Ramesh and Suresh. This is how Ramesh sees the chat (Username is mentioned in the title of the window)

<img src="/images/Screenshot from 2020-05-01 14-13-04.png" alt="Ramesh's chatscreen">

The chat window for Suresh is almost the same. 

And all the chats get logged on the console too.

<img src="/images/Screenshot from 2020-05-01 14-14-10.png" alt="logs">

## How to use it
- Just clone the repository and execute ```server.py``` on your terminal
- And in client_gui.py, change line 180 with your server's IP Address
- Install dependencies, ```pip install Pillow ```.
- Connect the server with upto 5 systems in the same network, and execute ```client_gui.py``` for endless fun

*P.S- This program can be extended to work from just LAN to the entire internet. Any PR in this direction would be highly appreciated*
