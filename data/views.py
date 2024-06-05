# myapp/views.py

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .table import Session, MyModel

# Example values
name = 'John Doe'
created_at = datetime.utcnow()

# Create a new session
session = Session()

# Create a new Developer instance
new_developer = MyModel(name=name, created_at=created_at)

# Add the new instance to the session and commit
session.add(new_developer)
session.commit()



