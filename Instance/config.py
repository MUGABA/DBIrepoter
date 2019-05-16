import os


class Baseconfig:

	DEBUG = False
	TESTING = False
	SECRET = os.getenv('SECRET')
	# print(SECRET)
	DATABASE_URI = 'postgres://postgres:rashid123@localhost:5432/dbireporter'


class Developmentconfig(Baseconfig):
	DEBUG = True
	TESTING = False
	ENV = 'Development'
	DATABASE_URI = 'postgresL://postgres:rashid123@localhost:5432/dbireporter'

class Testingconfig(Baseconfig):
	DEBUG = True
	TESTING = True
	ENV = 'Testing'
	DATABASE_URI = 'postgres://postgres:rashid123@localhost:5432/test_ireporter'


app_config = {
	"Development":Developmentconfig,
	"Testing": Testingconfig
}