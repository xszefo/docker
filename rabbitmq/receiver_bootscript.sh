#!/bin/sh
cd /code
pip install -r requirements.txt
python /code/rabbit_receive_message.py
