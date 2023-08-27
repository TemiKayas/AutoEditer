# AutoEditor

Given a long movie, AutoEditor will transcribe, Identify key aspects and edit the movie to include the important concepts.

## installation Guide

Make sure to install the following Python packages:

```bash
pip install moviepy
pip install ffmpeg
brew install ffmpeg
pip install openai
```

## launching the server

Our api server is based on [Django](https://docs.djangoproject.com/). The server management file is [manage.py](./manage.py) and the source code is located in [summarizer](./summarizer/).

To develop the server make sure django is installed:

```bash
python -m django --version
pip install Django
```

To run the server:

```bash
python manage.py runserver
```
