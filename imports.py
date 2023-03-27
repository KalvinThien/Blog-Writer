import os
import io

from flask import Request
from flask import Flask, render_template, request, redirect, url_for

from datetime import datetime


def write_file(folder_name, filename, content):
    filepath = os.path.join(folder_name, filename)
    with open(filepath, 'w') as f:
        f.write(content)


def read_file(folder_name, filename):
    filepath = os.path.join(folder_name, filename)
    with open(filepath, 'r') as f:
        return f.read()
