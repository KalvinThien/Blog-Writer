import os
import io

from flask import Request
from flask import Flask, render_template, request, redirect, url_for
# from google.oauth2._credentials_async import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from google.auth.transport.requests import Request
# from googleapiclient.http import MediaIoBaseDownload
# from googleapiclient.http import MediaFileUpload

from datetime import datetime

from langchain import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms import OpenAIChat


def write_file(folder_name, filename, content):
    filepath = os.path.join(folder_name, filename)
    with open(filepath, 'w') as f:
        f.write(content)


def read_file(folder_name, filename):
    filepath = os.path.join(folder_name, filename)
    with open(filepath, 'r') as f:
        return f.read()
