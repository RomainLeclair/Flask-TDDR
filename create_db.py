# create db

from project.app import db
from project.models import Post

# create the database and the db table
db.create_all()

# commit change
db.session.commit()
