from api import create_app
from api.database.db import Database 

app = create_app('Production')
db = Database(app.config['DATABASE_URI'])

db.create_tables()

if __name__ == '__main__':
	app.run()